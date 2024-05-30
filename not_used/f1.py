

import sqlite3

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd





def clear_fields():
    global p_id, p_name, description, price, p_quantity

    for i in ['p_id', 'p_name', 'description', 'price', 'p_quantity']:
        exec(f"{i}.set('')")
        #id_entry.config(state='normal')
    try:
        tree.selection_remove(tree.selection()[0])
    except:
        pass


def clear_and_display():
    clear_fields()
    display_all_products()

#PRODUCTS

def add_product():
    global connector
    global p_id, p_name, description, price, p_quantity

    try:
        cursor.execute(
            'INSERT INTO products (p_id, p_name, description, price, p_quantity) VALUES (?, ?, ?, ?, ?)',
            (p_id.get(), p_name.get(), description.get(), price.get(), p_quantity.get()))
        connector.commit()

        clear_and_display()

        mb.showinfo('Product added', 'The new product was successfully added to your database')
    except sqlite3.Error as e:
        mb.showerror('Error', f'Failed to add product: {str(e)}')

# Function to view a record
def view_product_record():
    global p_id, p_name, description, price, p_quantity
    global tree

    if not tree.focus():
        mb.showerror('Select a row!',
                     'To view a record, you must select it in the table. Please do so before continuing.')
        return

    current_item_selected = tree.focus()
    values_in_selected_item = tree.item(current_item_selected)
    selection = values_in_selected_item['values']
    try:
        id.set(selection[0])
        name.set(selection[1])
        description.set(selection[2])
        price.set(selection[3])
        quantity.set(selection[4])
    except:
        id.set('')

def delete_product():
    display_all_products()

    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
        return

    current_item = tree.focus()
    values = tree.item(current_item)
    selection = values["values"]

    cursor.execute('DELETE FROM products WHERE p_id=?', (selection[1],))
    connector.commit()

    tree.delete(current_item)

    mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')

    clear_and_display()

# Display all Products
def display_all_products():
    global connector, cursor
    global tree

    tree.delete(*tree.get_children())

    curr = connector.execute('SELECT * FROM products')
    data = curr.fetchall()

    for records in data:
        tree.insert('', END, values=records)


####################################################################
        
#SUPPLIER

def add_supplier():
    global connector
    global s_id, s_name, company_name, contact, address

    try:
        cursor.execute(
            'INSERT INTO suppliers (s_id, s_name, company_name, contact, address) VALUES (?, ?, ?, ?, ?)',
            (s_id.get(), s_name.get(), company_name.get(), contact.get(), address.get()))
        connector.commit()

        mb.showinfo('Supplier Successfully Added', 'The new supplier is successfully added to your database')
    except sqlite3.Error as e:
        mb.showerror('Error', f'Failed to add user: {str(e)}')


def delete_supplier():
    global connector

    global s_id

    try:
        cursor.execute(
            'DELETE FROM suppliers WHERE condition id = s_id;',
            (s_id.get()))
        connector.commit()

        mb.showinfo('Supplier Deleted')
    except sqlite3.Error as e:
        mb.showerror('Error', f'Failed to add product: {str(e)}')
        
# USER

def login_password():
            password = self.entry_5.get()
            if password == "**admin**":
                controller.show_page(LoginSuccesful)
            else:
                controller.show_page(LoginDenied)


def add_user():
    global connector
    global id, username, password, email, created_at

    try:
        cursor.execute(
            'INSERT INTO users (id, username, password, email, created_at) VALUES (?, ?, ?, ?, ?)',
            (id.get(), username.get(), password.get(), email.get(), created_at.get()))
        connector.commit()

        mb.showinfo('User Added', 'The new user was successfully added to your database')
    except sqlite3.Error as e:
        mb.showerror('Error', f'Failed to add product: {str(e)}')


    


try:
    # Connect to the database
    connector = sqlite3.connect('inventory.db')
    cursor = connector.cursor()

    # Execute the SQL statement to create the users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # Create the products table
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        description TEXT,
                        price REAL,
                        quantity INTEGER
                    )''')

    # Create the orders table
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY,
                        product_id INTEGER,
                        quantity INTEGER,
                        order_date DATE,
                        FOREIGN KEY (product_id) REFERENCES products(id)
                    )''')

    # Create the suppliers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS suppliers (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        contact TEXT,
                        address TEXT
                    )''')

    # Create the purchase_orders table
    cursor.execute('''CREATE TABLE IF NOT EXISTS purchase_orders (
                        id INTEGER PRIMARY KEY,
                        supplier_id INTEGER NOT NULL,
                        products TEXT NOT NULL,
                        status TEXT,
                        FOREIGN KEY(supplier_id) REFERENCES suppliers(id)
                    )''')

    # Commit the changes
    connector.commit()
except sqlite3.Error as e:
    print("SQLite error:", e)
finally:
    if connector:
        connector.close()
