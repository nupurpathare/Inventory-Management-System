from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
import sqlite3

class SupplierManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('PythonGeeks Supplier Management System')
        self.root.geometry('1010x530')
        self.root.resizable(0, 0)

        self.connector = sqlite3.connect('supplier.db')
        self.cursor = self.connector.cursor()

        self.connector.execute(
            'CREATE TABLE IF NOT EXISTS Supplier (SUP_NAME TEXT, SUP_ID TEXT PRIMARY KEY NOT NULL, PRODUCT_NAME TEXT, PRODUCT_QUANTITY INTEGER)'
        )

        # StringVars
        self.sup_name = StringVar()
        self.sup_id = StringVar()
        self.product_name = StringVar()
        self.product_quantity = StringVar()

        self.initialize_gui()

    def initialize_gui(self):
        # Frames
        self.left_frame = Frame(self.root, bg='LightSkyBlue')
        self.left_frame.place(x=0, y=30, relwidth=0.3, relheight=0.96)

        self.RT_frame = Frame(self.root, bg='DeepSkyBlue')
        self.RT_frame.place(relx=0.3, y=30, relheight=0.2, relwidth=0.7)

        self.RB_frame = Frame(self.root)
        self.RB_frame.place(relx=0.3, rely=0.24, relheight=0.785, relwidth=0.7)

        # Left Frame
        Label(self.left_frame, text='Supplier Name', bg='LightSkyBlue', font=('Georgia', 13)).place(x=98, y=25)
        Entry(self.left_frame, width=25, font=('Times New Roman', 12), textvariable=self.sup_name).place(x=45, y=55)

        Label(self.left_frame, text='Supplier ID', bg='LightSkyBlue', font=('Georgia', 13)).place(x=110, y=105)
        Entry(self.left_frame, width=25, font=('Times New Roman', 12), textvariable=self.sup_id).place(x=45, y=135)

        Label(self.left_frame, text='Product Name', bg='LightSkyBlue', font=('Georgia', 13)).place(x=90, y=185)
        Entry(self.left_frame, width=25, font=('Times New Roman', 12), textvariable=self.product_name).place(x=45, y=215)

        Label(self.left_frame, text='Product Quantity', bg='LightSkyBlue', font=('Georgia', 13)).place(x=75, y=265)
        Entry(self.left_frame, width=25, font=('Times New Roman', 12), textvariable=self.product_quantity).place(x=45, y=295)

        submit = Button(self.left_frame, text='Add new record', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=20, command=self.add_record)
        submit.place(x=50, y=375)

        clear = Button(self.left_frame, text='Clear fields', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=20, command=self.clear_fields)
        clear.place(x=50, y=435)

        # Right Top Frame
        Button(self.RT_frame, text='Delete supplier record', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=17, command=self.remove_record).place(x=8, y=30)
        Button(self.RT_frame, text='Delete all suppliers', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=17, command=self.delete_all_suppliers).place(x=178, y=30)
        Button(self.RT_frame, text='Update supplier details', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=17, command=self.update_record).place(x=348, y=30)

        # Right Bottom Frame
        Label(self.RB_frame, text='SUPPLIER INVENTORY', bg='DodgerBlue', font=('Noto Sans CJK TC', 15, 'bold')).pack(side=TOP, fill=X)

        self.tree = ttk.Treeview(self.RB_frame, selectmode=BROWSE, columns=('Supplier Name', 'Supplier ID', 'Product Name', 'Product Quantity'))

        XScrollbar = Scrollbar(self.tree, orient=HORIZONTAL, command=self.tree.xview)
        YScrollbar = Scrollbar(self.tree, orient=VERTICAL, command=self.tree.yview)
        XScrollbar.pack(side=BOTTOM, fill=X)
        YScrollbar.pack(side=RIGHT, fill=Y)

        self.tree.config(xscrollcommand=XScrollbar.set, yscrollcommand=YScrollbar.set)

        self.tree.heading('Supplier Name', text='Supplier Name', anchor=CENTER)
        self.tree.heading('Supplier ID', text='Supplier ID', anchor=CENTER)
        self.tree.heading('Product Name', text='Product Name', anchor=CENTER)
        self.tree.heading('Product Quantity', text='Product Quantity', anchor=CENTER)

        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('#1', width=225, stretch=NO)
        self.tree.column('#2', width=70, stretch=NO)
        self.tree.column('#3', width=150, stretch=NO)

        self.tree.place(y=30, x=0, relheight=0.9, relwidth=1)

        self.clear_and_display()

    def display_records(self):
        self.tree.delete(*self.tree.get_children())

        curr = self.connector.execute('SELECT * FROM Supplier')
        data = curr.fetchall()

        for records in data:
            self.tree.insert('', END, values=records)

    def clear_fields(self):
        for var in [self.sup_name, self.sup_id, self.product_name, self.product_quantity]:
            var.set('')

    def clear_and_display(self):
        self.clear_fields()
        self.display_records()

    def add_record(self):
        surety = mb.askyesno('Are you sure?', 'Are you sure this is the data you want to enter?\nPlease note that Supplier ID cannot be changed in the future')

        if surety:
            try:
                self.cursor.execute(
                    'INSERT INTO Supplier (SUP_NAME, SUP_ID, PRODUCT_NAME, PRODUCT_QUANTITY) VALUES (?, ?, ?, ?)',
                    (self.sup_name.get(), self.sup_id.get(), self.product_name.get(), self.product_quantity.get()))
                self.connector.commit()

                self.clear_and_display()

                mb.showinfo('Record added', 'The new record was successfully added to your database')
            except sqlite3.IntegrityError:
                mb.showerror('Supplier ID already in use!', 'The Supplier ID you are trying to enter is already in the database, please alter that supplier\'s record or check any discrepancies on your side')

    def remove_record(self):
        if not self.tree.selection():
            mb.showerror('Error!', 'Please select an item from the database')
            return

        current_item = self.tree.focus()
        values = self.tree.item(current_item)
        selection = values["values"]

        self.cursor.execute('DELETE FROM Supplier WHERE SUP_ID=?', (selection[1],))
        self.connector.commit()

        self.tree.delete(current_item)

        mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')

        self.clear_and_display()

    def delete_all_suppliers(self):
        if mb.askyesno('Are you sure?', 'Are you sure you want to delete all suppliers?\n\nThis command cannot be reversed'):
            self.tree.delete(*self.tree.get_children())

            self.cursor.execute('DELETE FROM Supplier')
            self.connector.commit()

            mb.showinfo('Done', 'All suppliers were successfully deleted from the database.')
        else:
            return

    def update_record(self):
        def update():
            self.cursor.execute('UPDATE Supplier SET SUP_NAME=?, PRODUCT_NAME=?, PRODUCT_QUANTITY=? WHERE SUP_ID=?',
                                (self.sup_name.get(), self.product_name.get(), self.product_quantity.get(), self.sup_id.get()))
            self.connector.commit()

            self.clear_and_display()

            edit.destroy()

        if not self.tree.selection():
            mb.showerror('Error!', 'Please select an item from the database')
            return

        current_item_selected = self.tree.focus()
        values_in_selected_item = self.tree.item(current_item_selected)
        selection = values_in_selected_item['values']

        self.sup_name.set(selection[0])
        self.sup_id.set(selection[1])
        self.product_name.set(selection[2])
        self.product_quantity.set(selection[3])

        edit = Button(self.left_frame, text='Update Record', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=20, command=update)
        edit.place(x=50, y=375)

if __name__ == '__main__':
    root = Tk()
    app = SupplierManagementSystem(root)
    root.mainloop()
