import time
import re
import sqlite3
from datetime import datetime
from datetime import date
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
from tkinter import Canvas, Button, PhotoImage
timestamp = time.time()
formatted_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

today = date.today()

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
                    p_id INTEGER PRIMARY KEY,
                    p_name TEXT NOT NULL,
                    p_description TEXT,
                    p_price REAL,
                    p_quantity INTEGER
                )''')

# Create the orders table
cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY,
                    product_id INTEGER,
                    quantity INTEGER,
                    order_date DATE,
                    FOREIGN KEY (product_id) REFERENCES products(id)
                )''')

# Create the purchase_orders table
cursor.execute('''CREATE TABLE IF NOT EXISTS purchase_orders (
                    id INTEGER PRIMARY KEY,
                    supplier_id INTEGER NOT NULL,
                    products TEXT NOT NULL,
                    status TEXT,
                    FOREIGN KEY(supplier_id) REFERENCES suppliers(id)
                )''')




####################################################################
        

# USER
def display_all_products():
    global connector, cursor
    global tree

    tree.delete(*tree.get_children())

    curr = connector.execute('SELECT * FROM products')
    data = curr.fetchall()

    for records in data:
        tree.insert('', END, values=records)






    

# Front-end Start
class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.current_page = None

    def show(self):
        self.lift()
        self.current_page = self

    def get_current_page(self):
        return self.current_page
    

# Keep Inventory
class SplashScreen(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Update Product Page")
        label.pack(padx=10, pady=10)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        image_image_3_path = r"splashscreen\image_1.png"

        self.image_1 = PhotoImage(file=image_image_3_path)
        image_1 = canvas.create_image(
            512.0,
            364.0,
            image=self.image_1
        )

        button_image_b2_path = r"splashscreen\button_1.png"
        self.button_image_5 = PhotoImage(file=button_image_b2_path)
        button_5 = tk.Button(self, image=self.button_image_5, command=lambda: controller.show_page(LoginPage))
        button_5.image = self.button_image_5  # Keep a reference to prevent garbage collection
        button_5.place(x=536.0, y=602.0, width=217.0, height=75.0)

        button_image_b2_path = r"splashscreen\button_2.png"
        self.button_image_5 = PhotoImage(file=button_image_b2_path)
        button_5 = tk.Button(self, image=self.button_image_5,bd=0, highlightthickness=0, command=lambda: controller.show_page(SignUp))
        button_5.configure(bg="white")
        button_5.image = self.button_image_5  # Keep a reference to prevent garbage collection
        button_5.place(x=265.0, y=602.0, width=217.0, height=75.0)

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_product(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def get_all_products(self):
        return list(self.items.values())

class AddToCart(Page):
    def __init__(self, parent, controller):

        Page.__init__(self, parent, controller)
        self.cart = Cart()
        self.cart = {}
        self.label = tk.Label(self, text="Services Page")
        self.label.pack(padx=10, pady=10)

        # Add a button to switch to the home page
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        image_image_1_path = r"addtocartpage\image_1.png"
        self.image_1 = PhotoImage(file=image_image_1_path)
        image_1 = canvas.create_image(
            512.0,
            364.0,
            image=self.image_1
        )

        canvas.create_text(
            373.0,
            21.0,
            anchor="nw",
            text="Add To Cart",
            fill="#000000",
            font=("Inter SemiBold", 48 * -1)
        )

        canvas.create_rectangle(
            367.9991149902344,
            81.492919921875,
            651.0009181501591,
            86.492919921875,
            fill="#000000",
            outline="")

        canvas.create_text(
            69.0,
            241.0,
            anchor="nw",
            text="Enter Quantity:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        canvas.create_text(
            82.0,
            149.0,
            anchor="nw",
            text="Enter Product:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        button_image_1_path = r"addtocartpage\entry_1.png"
        button_image_2_path = r"addtocartpage\entry_2.png"
        button_image_3_path = r"addtocartpage\button_1.png"
        button_image_4_path = r"addtocartpage\button_2.png"
        button_image_5_path = r"addtocartpage\button_3.png"

        backbutton_path = "backbutton/back_button.png"
        self.backbuttonimage = PhotoImage(file=backbutton_path)
        backbutton = tk.Button(self, image=self.backbuttonimage, command=lambda: controller.show_page(SignUp))
        backbutton.image = self.backbuttonimage  # Keep a reference to prevent garbage collection
        backbutton.place(x=0.0, y=0.0, width=83.0, height=54.0)

        # Add images to buttons
        self.button_image_1 = PhotoImage(file=button_image_1_path)
        self.product_entry = Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        self.product_entry.image = self.button_image_1  # Keep a reference to prevent garbage collection
        self.product_entry.place(x=401.4, y=139.5, width=405.0, height=58.0)
        self.product_entry.get()

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        self.quantity_entry = Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        self.quantity_entry.image = self.button_image_2  # Keep a reference to prevent garbage collection
        self.quantity_entry.place(x=401.5, y=234.5, width=405.0, height=58.0)
        self.quantity_entry.get()

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        self.add_to_cart_button = Button(self, image=self.button_image_3, command = lambda: controller.show_page(ViewAllProductsPage))
        self.add_to_cart_button.image = self.button_image_3  # Keep a reference to prevent garbage collection
        self.add_to_cart_button.place(x=93.0, y=598.0, width=308.0, height=69.0)

        self.button_image_4 = PhotoImage(file=button_image_4_path)
        self.clear_button = Button(self, image=self.button_image_4, command=self.viewcart)
        self.clear_button.image = self.button_image_4  # Keep a reference to prevent garbage collection
        self.clear_button.place(x=651.0, y=598.0, width=308.0, height=69.0)

        self.button_image_5 = PhotoImage(file=button_image_5_path)
        self.search_button = Button(self, image=self.button_image_5, command=self.add_to_cart)
        self.search_button.image = self.button_image_5  # Keep a reference to prevent garbage collection
        self.search_button.place(x=613.0, y=324.0, width=192.0, height=69.0)

    def add_to_cart(self):
        # Get product and quantity
        product = self.product_entry.get()
        quantity = self.quantity_entry.get()

        cursor.execute("SELECT MAX(id) FROM orders")
        max_id = cursor.fetchone()[0]

        cursor.execute("SELECT MAX(p_id) FROM products")
        max_pid = cursor.fetchone()[0]

        cursor.execute("SELECT p_quantity FROM products WHERE p_id = ?", (product,))
        prod_q = cursor.fetchone()

        if not int(product) <= max_pid:
            mb.showerror("Error", "Product not available in inventory.")
        else:
            if not quantity.isdigit() or int(quantity) >= prod_q[0]:
                mb.showerror("Error", "Required quantity exceeds stock.")
            else:
                if max_id is None:
                    id = 100
                else:
                    id = max_id + 1
                    print(quantity)
                    updated_quantity = prod_q[0] - int(quantity)
                    print(updated_quantity)
                    print(product)

                cursor.execute(
                    'INSERT INTO orders (id, product_id, quantity, order_date) VALUES (?, ?, ?, ?)',
                    (id, product, quantity, today))
                connector.commit()

                # Update the cart dictionary with product and quantity
                if product in self.cart:
                    self.cart[product] += int(quantity)
                else:
                    self.cart[product] = int(quantity)

                mb.showinfo("Success", f"{quantity} {product}(s) added to cart!")
                self.clear_fields()

    def clear_fields(self):
        self.quantity_entry.delete(0, tk.END)
        self.product_entry.delete(0, tk.END)

    def viewcart(self):
        cart_window = Toplevel(self)
        cart_window.title("View Cart")

        # Styling
        cart_window.configure(bg="#f0f0f0")
        table_frame_bg = "#ffffff"
        header_font = ("Arial", 12, "bold")
        data_font = ("Arial", 11)
        header_bg = "#007bff"
        header_fg = "#ffffff"
        data_bg = "#f8f9fa"
        data_fg = "#000000"


        table_label = Label(cart_window, text="Cart Items", bg="#f0f0f0", font=("Arial", 16, "bold"))
        table_label.pack(pady=10)


        table_frame = tk.Frame(cart_window, bg=table_frame_bg)
        table_frame.pack()


        headers = ["Product ID", "Quantity"]
        for col, header in enumerate(headers):
            header_label = Label(table_frame, text=header, bg=header_bg, fg=header_fg,
                                 font=header_font, width=20, padx=10, pady=5, relief=tk.RAISED)
            header_label.grid(row=0, column=col, sticky=tk.NSEW)


        for row, (product, quantity) in enumerate(self.cart.items(), start=1):
            product_label = Label(table_frame, text=product, bg=data_bg, fg=data_fg,
                                  font=data_font, width=20, padx=10, pady=5, relief=tk.RAISED)
            product_label.grid(row=row, column=0, sticky=tk.NSEW)

            quantity_label = Label(table_frame, text=quantity, bg=data_bg, fg=data_fg,
                                   font=data_font, width=20, padx=10, pady=5, relief=tk.RAISED)
            quantity_label.grid(row=row, column=1, sticky=tk.NSEW)


        close_button = Button(cart_window, text="Close", command=cart_window.destroy,
                              bg="#dc3545", fg="#ffffff", font=("Arial", 12, "bold"),
                              width=10, padx=10, pady=5, relief=tk.RAISED)
        close_button.pack(pady=20)


        table_frame.columnconfigure(0, weight=1)
        table_frame.columnconfigure(1, weight=1)


        for i in range(row + 1):
            table_frame.rowconfigure(i, weight=1)



'''
    def view_cart(self):
        product = self.product_entry.get().lower()
        all_products = self.cart.get_all_products()

        if not product:
            # Assuming you have an empty list to store product IDs
            all_products = []

            # Function to add product IDs provided by the user
            def add_product_id(product_id):
                # Convert the product_id to string before adding to all_products
                all_products.append(str(product_id))

            # Example usage:
            # Suppose the user provides product IDs as input
            user_input_ids = [1, 2, 3, 4]

            # Add each ID to all_products using the add_product_id function
            for id in user_input_ids:
                add_product_id(id)

            # Show the message box with all_products
            mb.showinfo("All Products", "Available Products:\n" + '\n'.join(all_products))


            
        else:
            search_results = [p for p in all_products if product in p.lower()]
            if search_results:
                mb.showinfo("Search Results", "Search Results:\n" + '\n'.join(search_results))
            else:
                mb.showinfo("Search Results", "No products found matching the search criteria.")
'''





class LoginPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)


        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_text(
            347.0,
            66.0,
            anchor="nw",
            text="Enter Login details",
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )


        image_image_1_path = r"frame0\image_1.png"

        self.image_1 = PhotoImage(file=image_image_1_path)
        image_1 = canvas.create_image(
            153.0,
            364.0,
            image=self.image_1
        )

        canvas.create_rectangle(
            341.9992980957031,
            131.5,
            680.0007019042969,
            136.5,
            fill="#000000",
            outline="")

        canvas.create_text(
            347.0,
            227.0,
            anchor="nw",
            text="Name: ",
            fill="#000000",
            font=("Inter Bold", 36 * -1)
        )

        canvas.create_text(
            347.0,
            329.0,
            anchor="nw",
            text="Password: ",
            fill="#000000",
            font=("Inter Bold", 36 * -1)
        )



        login_button_path = r"frame0\button_1.png"
        button_image_2_path = r"frame0\entry_1.png"
        button_image_3_path = r"frame0\entry_2.png"
        button_image_4_path = r"frame0\entry_3.png"
        button_image_5_path = r"frame0\entry_4.png"

        backbutton_path = "backbutton/back_button.png"
        self.backbuttonimage = PhotoImage(file=backbutton_path)
        backbutton = tk.Button(self, image=self.backbuttonimage, command=lambda: controller.show_page(SplashScreen))
        backbutton.image = self.backbuttonimage  # Keep a reference to prevent garbage collection
        backbutton.place(x=0.0, y=0.0, width=83.0, height=54.0)

        self.login_button = PhotoImage(file=login_button_path)
        button_1 = tk.Button(self, image=self.login_button, command=lambda: login_password())
        button_1.image = self.login_button
        button_1.place(x=777, y=422, width=137, height=58)

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        self.entry_2 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        self.entry_2.image = self.button_image_2
        self.entry_2.place(x=586, y=223, width=367, height=45)

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        self.entry_3 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        self.entry_3.image = self.button_image_3
        self.entry_3.place(x=586, y=325, width=367, height=45)

        name = self.entry_3.get

        def login_password():
            global connector

            password = self.entry_3.get()
            if password == "a":
                controller.show_page(LoginSuccesful)
            else:
                controller.show_page(LoginDenied)


'''
            def print_entry_text():
            entry_texts = [
                self.entry_2.get(),
                self.entry_3.get(),
                self.entry_4.get(),
                self.entry_5.get()
            ]
            for index, text in enumerate(entry_texts, start=2):
                print(f"Entry {index} text: {text}")


        print_button = tk.Button(
            self,
            text="Print Entry Text",
            command=print_entry_text
        )
        print_button.place(x=100, y=622, width=200, height=40)
'''
class SignUp(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)


        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_text(
            347.0,
            66.0,
            anchor="nw",
            text="Enter Sign Up details",
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )


        image_image_1_path = r"frame0\image_1.png"

        self.image_1 = PhotoImage(file=image_image_1_path)
        image_1 = canvas.create_image(
            153.0,
            364.0,
            image=self.image_1
        )

        canvas.create_rectangle(
            341.9992980957031,
            131.5,
            680.0007019042969,
            136.5,
            fill="#000000",
            outline="")

        canvas.create_text(
            347.0,
            227.0,
            anchor="nw",
            text="First name",
            fill="#000000",
            font=("Inter Bold", 36 * -1)
        )

        canvas.create_text(
            347.0,
            329.0,
            anchor="nw",
            text="Last name ",
            fill="#000000",
            font=("Inter Bold", 36 * -1)
        )

        canvas.create_text(
            347.0,
            431.0,
            anchor="nw",
            text="Email ",
            fill="#000000",
            font=("Inter Bold", 36 * -1)
        )

        canvas.create_text(
            347.0,
            533.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("Inter Bold", 36 * -1)
        )

        login_button_path = r"SignUp\sign_up_button.png"
        button_image_2_path = r"frame0\entry_1.png"
        button_image_3_path = r"frame0\entry_2.png"
        button_image_4_path = r"frame0\entry_3.png"
        button_image_5_path = r"frame0\entry_4.png"

        backbutton_path = "backbutton/back_button.png"
        self.backbuttonimage = PhotoImage(file=backbutton_path)
        backbutton = tk.Button(self, image=self.backbuttonimage, command=lambda: controller.show_page(SplashScreen))
        backbutton.image = self.backbuttonimage  # Keep a reference to prevent garbage collection
        backbutton.place(x=0.0, y=0.0, width=83.0, height=54.0)

        self.login_button = PhotoImage(file=login_button_path)
        button_1 = tk.Button(self, image=self.login_button, command=self.add_user)
        button_1.image = self.login_button
        button_1.place(x=777, y=622, width=181, height=58)

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        self.entry_2 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        self.entry_2.image = self.button_image_2
        self.entry_2.place(x=586, y=223, width=367, height=45)


        self.button_image_3 = PhotoImage(file=button_image_3_path)
        self.entry_3 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        self.entry_3.image = self.button_image_3
        self.entry_3.place(x=586, y=325, width=367, height=45)


        self.button_image_4 = PhotoImage(file=button_image_4_path)
        self.entry_4 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        self.entry_4.image = self.button_image_4
        self.entry_4.place(x=586, y=427, width=367, height=45)


        self.button_image_5 = PhotoImage(file=button_image_5_path)
        self.entry_5 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        self.entry_5.image = self.button_image_5
        self.entry_5.place(x=586, y=529, width=367, height=45)

 #   def on_button_click(self):
 #       self.add_user()

    def add_user(self):
        global connector

        try:
            firstname = self.entry_2.get()
            email = self.entry_4.get()
            password = self.entry_5.get()

            # Email validation using regular expressions
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                mb.showerror('Invalid Email', 'Please enter a valid email address')
                return

            cursor.execute("SELECT MAX(id) FROM users")
            max_id = cursor.fetchone()[0]

            # If no users yet, start from 1, otherwise increment the max_id by 1
            if max_id is None:
                id = 1
            else:
                id = max_id + 1

            cursor.execute(
                'INSERT INTO users (id, username, password, email, created_at) VALUES (?, ?, ?, ?, ?)',
                (id, firstname, password, email, formatted_time)
            )
            connector.commit()

            mb.showinfo('User Added', 'The new user was successfully added to your database')
            self.controller.show_page(AddToCart)

        except sqlite3.Error as e:
            mb.showerror('Error', f'Failed to add user: {str(e)}')


# Button 1 Remaining
class ProductMenu(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )

        lp1 = LoginPage(parent,controller)
        name1 = lp1.entry_3.get()

        canvas.place(x=0, y=0)
        canvas.create_text(
            347.0,
            66.0,
            anchor="nw",
            text="Welcome " + name1,
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )

        canvas.create_text(
            527.0,
            66.0,
            anchor="nw",
            text = 'User1',
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )


        image_image_1_path = r"frame0\image_1.png"

        self.image_1 = PhotoImage(file=image_image_1_path)
        image_1 = canvas.create_image(
            153.0,
            364.0,
            image=self.image_1
        )

        canvas.create_rectangle(
            346.9668579101562,
            120.12744140625,
            640.0079040527344,
            123.12744140625,
            fill="#000000",
            outline=""
        )

        button_image_1_path = r"frame1\button_1.png"
        button_image_2_path = r"frame1\button_2.png"
        button_image_3_path = r"frame1\button_3.png"
        button_image_4_path = r"frame1\button_4.png"
        button_image_5_path = r"frame1\button_5.png"

        # Not neede this button
        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Button(self, image=self.button_image_1, command=lambda: controller.show_page(MainMenu))
        button_1.image = self.button_image_1
        button_1.place(x=830, y=563, width=137, height=58)

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        button_2 = tk.Button(self, image=self.button_image_2, command=lambda: controller.show_page(AddProductPage))
        button_2.image = self.button_image_2
        button_2.place(x=347, y=232, width=281, height=69)

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        button_3 = tk.Button(self, image=self.button_image_3, command=lambda: controller.show_page(ViewAllProductsPage))
        button_3.image = self.button_image_3
        button_3.place(x=686, y=232, width=281, height=69)

        self.button_image_4 = PhotoImage(file=button_image_4_path)
        button_4 = tk.Button(self, image=self.button_image_4, command =lambda: controller.show_page(DeleteProductPage))
        button_4.image = self.button_image_4
        button_4.place(x=347, y=365, width=281, height=69)

        self.button_image_5 = PhotoImage(file=button_image_5_path)
        button_5 = tk.Button(self, image=self.button_image_5, command=lambda: controller.show_page(UpdateProductPage))
        button_5.image = self.button_image_5
        button_5.place(x=686, y=365, width=281, height=69)

# Can change text font and size which is from user
class AddProductPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Services Page")
        label.pack(padx=10, pady=10)

        def add_product():
            global connector

            try:

                adp_name = button_1.get()
                adp_desc = button_2.get()
                adp_price = button_3.get()
                adp_quantity = button_6.get()

                cursor.execute("SELECT MAX(p_id) FROM products")
                max_id = cursor.fetchone()[0]

                # If no products yet, start from 1, otherwise increment the max_id by 1
                if max_id is None:
                    adp_id = 1
                else:
                    adp_id = max_id + 1
                cursor.execute(
                    'INSERT INTO products (p_id, p_name, p_description, p_price, p_quantity) VALUES (?, ?, ?, ?, ?)',
                    (adp_id, adp_name, adp_desc, adp_price, adp_quantity))
                connector.commit()

                # clear_and_display()

                mb.showinfo('Product added', 'The new product was successfully added to your database')
            except sqlite3.Error as e:
                mb.showerror('Error', f'Failed to add product: {str(e)}')

        def reset_fields():
            button_1.delete(0, tk.END)  # Clear the entry for product name
            button_2.delete(0, tk.END)  # Clear the entry for product description
            button_3.delete(0, tk.END)  # Clear the entry for product price
            button_6.delete(0, tk.END)  # Clear the entry for product quantity


        # Add a button to switch to the home page
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )
        canvas.place(x=0, y=0)



        image_image_1_path = r"frame2\image_1.png"

        # Add images to buttons
        self.image_1 = PhotoImage(file=image_image_1_path)
        image_1 = canvas.create_image(
            520.0,
            360.0,
            image=self.image_1
        )

        canvas.create_text(
            172.0,
            406.0,
            anchor="nw",
            text="Price(per unit): ",
            fill="#000000",
            font=("Inter SemiBold", 32 * -1)
        )

        canvas.create_text(
            174.0,
            312.0,
            anchor="nw",
            text="Description: ",
            fill="#000000",
            font=("Inter SemiBold", 32 * -1)
        )

        canvas.create_text(
            247.0,
            56.0,
            anchor="nw",
            text="Add the details in database",
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )

        canvas.create_text(
            174.0,
            218.0,
            anchor="nw",
            text="Product Name: ",
            fill="#000000",
            font=("Inter SemiBold", 32 * -1)
        )

        canvas.create_text(
            662.0,
            406.0,
            anchor="nw",
            text="Qty: ",
            fill="#000000",
            font=("Inter SemiBold", 32 * -1)
        )

        button_image_1_path = r"frame2\entry_1.png"
        button_image_2_path = r"frame2\entry_2.png"
        button_image_3_path = r"frame2\entry_3.png"
        button_image_4_path = r"frame2\button_1.png"
        button_image_5_path = r"frame2\button_2.png"

        # Add images to buttons
        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_1.image = self.button_image_1  # Keep a reference to prevent garbage collection
        button_1.place(x=443.0, y=211.5, width=480.0, height=52.0)
        #global adp_name
        #adp_name = button_1.get()

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        button_2 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_2.image = self.button_image_2  # Keep a reference to prevent garbage collection
        button_2.place(x=443.5, y=305.5, width=480.0, height=52.0)
        global adp_desc
        adp_desc = button_2.get()

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        button_3 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_3.image = self.button_image_3  # Keep a reference to prevent garbage collection
        button_3.place(x=443.0, y=399.5, width=176.0, height=52.0)
        global adp_price
        adp_price = button_3.get()

        self.button_image_6 = PhotoImage(file=button_image_3_path)
        button_6 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_6.image = self.button_image_6  # Keep a reference to prevent garbage collection
        button_6.place(x=747.0, y=399.5, width=176.0, height=52.0)
        global adp_quantity
        adp_quantity = button_6.get()

        self.button_image_4 = PhotoImage(file=button_image_4_path)
        button_4 = tk.Button(self, image=self.button_image_4, command = reset_fields) #, command = clear_fields)
        button_4.image = self.button_image_4  # Keep a reference to prevent garbage collection
        button_4.place(x=56.0, y=583.0, width=392.0, height=62.0)

        self.button_image_5 = PhotoImage(file=button_image_5_path)
        button_5 = tk.Button(self, image=self.button_image_5, command = add_product)
        button_5.image = self.button_image_5  # Keep a reference to prevent garbage collection
        button_5.place(x=531.0, y=583.0, width=392.0, height=62.0)

from tkinter import ttk

class ViewAllProductsPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        label = tk.Label(
            self,
            text="View All Products",
            bg="#FFFFFF",
            fg="#000000",
            font=("Inter SemiBold", 40)
        )
        label.place(x=320.0, y=56.0)

        backbutton_path = "backbutton/back_button.png"
        self.backbuttonimage = PhotoImage(file=backbutton_path)
        backbutton = tk.Button(self, image=self.backbuttonimage, command=lambda: controller.show_page(AddToCart))
        backbutton.image = self.backbuttonimage  # Keep a reference to prevent garbage collection
        backbutton.place(x=0.0, y=0.0, width=83.0, height=54.0)

        # Create a Treeview widget with style
        style = ttk.Style()
        style.configure("Treeview", background="#FFFFFF", foreground="#000000", rowheight=30, fieldbackground="#FFFFFF")
        style.map("Treeview", background=[("selected", "#0078D7")])

        tree = ttk.Treeview(self, columns=("ID", "Name", "Description", "Price", "Quantity"), show="headings", style="Treeview")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Description", text="Description")
        tree.heading("Price", text="Price")
        tree.heading("Quantity", text="Quantity")

        # Set column alignments and lines
        tree.column("ID", anchor="center", width=100)
        tree.column("Name", anchor="center", width=200)
        tree.column("Description", anchor="center", width=300)
        tree.column("Price", anchor="center", width=150)
        tree.column("Quantity", anchor="center", width=100)

        style.configure("Treeview.Heading", font=("Helvetica", 16, "bold"))

        tree.place(x=90.0, y=150.0)

        scrollbar = Scrollbar(self, orient=VERTICAL, command=tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.config(yscrollcommand=scrollbar.set)

        try:
            cursor.execute("SELECT p_id, p_name, p_description, p_price, p_quantity FROM products")
            products_data = cursor.fetchall()

            for idx, product in enumerate(products_data):
                if idx % 2 == 0:
                    tree.insert("", "end", values=product, tags=("evenrow",))
                else:
                    tree.insert("", "end", values=product, tags=("oddrow",))

        except sqlite3.Error as e:
            mb.showerror('Error', f'Failed to fetch products: {str(e)}')

class ViewUsers(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        # Create Canvas
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Label for User Database
        label = tk.Label(
            self,
            text="User Database",
            bg="#FFFFFF",
            fg="#000000",
            font=("Inter SemiBold", 40)
        )
        label.place(x=320.0, y=56.0)

        # Back Button
        backbutton_path = "backbutton/back_button.png"
        self.backbuttonimage = PhotoImage(file=backbutton_path)
        backbutton = tk.Button(self, image=self.backbuttonimage, command=lambda: controller.show_page(AddToCart))
        backbutton.image = self.backbuttonimage  # Keep a reference to prevent garbage collection
        backbutton.place(x=0.0, y=0.0, width=83.0, height=54.0)

        # Create a Treeview widget with style
        style = ttk.Style()
        style.configure("Treeview", background="#FFFFFF", foreground="#000000", rowheight=30, fieldbackground="#FFFFFF")
        style.map("Treeview", background=[("selected", "#0078D7")])

        tree = ttk.Treeview(self, columns=("ID", "Name", "Password", "Email", "Created At"), show="headings", style="Treeview")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Password", text="Password")
        tree.heading("Email", text="Email")
        tree.heading("Created At", text="Created At")

        # Set column alignments and lines
        tree.column("ID", anchor="center", width=100)
        tree.column("Name", anchor="center", width=200)
        tree.column("Password", anchor="center", width=150)
        tree.column("Email", anchor="center", width=250)
        tree.column("Created At", anchor="center", width=160)

        style.configure("Treeview.Heading", font=("Consolas", 16, "bold"))

        tree.place(x=90.0, y=150.0)

        # Scrollbar
        scrollbar = Scrollbar(self, orient=VERTICAL, command=tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.config(yscrollcommand=scrollbar.set)

        # Fetch and Display Users
        try:
            cursor.execute("SELECT id, username, password, email, created_at FROM users")
            users_data = cursor.fetchall()

            for idx, user in enumerate(users_data):
                if idx % 2 == 0:
                    tree.insert("", "end", values=user, tags=("evenrow",))
                else:
                    tree.insert("", "end", values=user, tags=("oddrow",))

        except sqlite3.Error as e:
            mb.showerror('Error', f'Failed to fetch users: {str(e)}')



# Remove it
class ServicesPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Services Page")
        label.pack(padx=10, pady=10)

        home_button = tk.Button(self, text="Go to Home Page", command=lambda: controller.show_page(MainMenu))
        home_button.pack()


# Remove it
class GalleryPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Gallery Page")
        label.pack(padx=10, pady=10)

        home_button = tk.Button(self, text="Go to Home Page", command=lambda: controller.show_page(ServicesPage))
        home_button.pack()


# done
class LoginSuccesful(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_text(
            274.0,
            424.0,
            anchor="nw",
            text="Log In Succesful",
            fill="#48D05E",
            font=("Inter Black", 64 * -1)
        )


        succes_image_path = r"succesframe\image_1.png"

        self.image_1 = PhotoImage(file=succes_image_path)
        image_1 = canvas.create_image(
            512.0,
            316.0,
            image=self.image_1,
        )



        button_image_1_path = r"succesframe\next.png"
        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Button(self, image=self.button_image_1, command=lambda: controller.show_page(MainMenu))
        button_1.image = self.button_image_1
        button_1.place(x=830, y=563, width=137, height=58)


# Done
class LoginDenied(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_text(
            317.0,
            436.0,
            anchor="nw",
            text="Log In Denied",
            fill="#D04848",
            font=("Inter Black", 64 * -1)
        )

        denied_image_path = r"deniedframe\image_1.png"

        self.image_1 = PhotoImage(file=denied_image_path)
        image_1 = canvas.create_image(
            512.0,
            316.0,
            image=self.image_1,
        )

        button_image_1_path = r"deniedframe\back.png"
        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Button(self, image=self.button_image_1, command=lambda: controller.show_page(LoginPage))
        button_1.image = self.button_image_1
        button_1.place(x=830, y=563, width=137, height=58)

# Remaining
class UpdateProductPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Update Product Page")
        label.pack(padx=10, pady=10)

        def get_product_details():
            # Get the ID entered by the user
            upd_id = button_1.get()

            # Fetch the product details from the database based on the ID
            cursor.execute("SELECT p_name, p_description, p_price, p_quantity FROM products WHERE p_id=?", (upd_id,))
            product_data = cursor.fetchone()

            if product_data:
                # Set the fetched data in the respective entry fields
                button_2.delete(0, tk.END)
                button_2.insert(0, product_data[1])  # p_description
                button_3.delete(0, tk.END)
                button_3.insert(0, product_data[2])  # p_price
                button_4.delete(0, tk.END)
                button_4.insert(0, product_data[3])  # p_quantity
            else:
                mb.showerror('Error', 'Product not found')

        def update_product():
            global connector, cursor

            try:
                upd_id = button_1.get()
                upd_desc = button_2.get()
                upd_price = button_3.get()
                upd_quantity = button_4.get()

                cursor.execute(
                    'UPDATE products SET p_description=?, p_price=?, p_quantity=? WHERE p_id=?',
                    ( upd_desc, upd_price, upd_quantity, upd_id))
                connector.commit()

                mb.showinfo('Product updated', 'The product was successfully updated in your database')
            except sqlite3.Error as e:
                mb.showerror('Error', f'Failed to update product: {str(e)}')


        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        image_image_3_path = r"updateframe\image_1.png"

        self.image_1 = PhotoImage(file=image_image_3_path)
        image_1 = canvas.create_image(
            512.0,
            364.0,
            image=self.image_1
        )

        canvas.create_rectangle(
            320.9892578125,
            113.0,
            697.0108337402344,
            118.0,
            fill="#000000",
            outline="")

        canvas.create_text(
            326.0,
            56.0,
            anchor="nw",
            text="Database Updation",
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )

        canvas.create_text(
            109.0,
            215.0,
            anchor="nw",
            text="Please enter the id:",
            fill="#000000",
            font=("Inter SemiBold", 32 * -1)
        )

        canvas.create_text(
            109.0,
            307.0,
            anchor="nw",
            text="Description:",
            fill="#000000",
            font=("Inter SemiBold", 32 * -1)
        )

        canvas.create_text(
            109.0,
            400.0,
            anchor="nw",
            text="Price: ",
            fill="#000000",
            font=("Inter SemiBold", 32 * -1)
        )

        canvas.create_text(
            109.0,
            491.0,
            anchor="nw",
            text="Quantity: ",
            fill="#000000",
            font=("Inter SemiBold", 32 * -1)
        )

        button_image_1_path = r"updateframe\entry_1.png"
        button_image_2_path = r"updateframe\entry_2.png"
        button_image_3_path = r"updateframe\entry_3.png"
        button_image_4_path = r"updateframe\entry_4.png"
        button_image_b1_path = r"updateframe\button_1.png"
        button_image_b2_path = r"updateframe\button_2.png"

        # Add images to buttons
        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_1.image = self.button_image_1  # Keep a reference to prevent garbage collection
        button_1.place(x=498.0, y=208.5, width=424.0, height=52.0)

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        button_2 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_2.image = self.button_image_2  # Keep a reference to prevent garbage collection
        button_2.place(x=498.0, y=300.5, width=424.0, height=52.0)

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        button_3 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_3.image = self.button_image_3  # Keep a reference to prevent garbage collection
        button_3.place(x=498.0, y=392.5, width=424.0, height=52.0)

        self.button_image_4 = PhotoImage(file=button_image_4_path)
        button_4 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_4.image = self.button_image_4  # Keep a reference to prevent garbage collection
        button_4.place(x=498.0, y=485.5, width=424.0, height=52.0)

        self.button_image_6 = PhotoImage(file=button_image_b1_path)
        button_6 = tk.Button(self, image=self.button_image_6, command = get_product_details)
        button_6.image = self.button_image_4  # Keep a reference to prevent garbage collection
        button_6.place(x=775.0, y=208.0, width=147.0, height=52.0)

        self.button_image_5 = PhotoImage(file=button_image_b2_path)
        button_5 = tk.Button(self, image=self.button_image_5, command = update_product)
        button_5.image = self.button_image_5  # Keep a reference to prevent garbage collection
        button_5.place(x=531.0, y=583.0, width=392.0, height=62.0)

        
class OrderList(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.a1 = AddToCart(parent,controller)
        self.controller = controller

        label = tk.Label(self, text="Update Product Page")
        label.grid(row=0, column=0, padx=80, pady=10)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        backbutton_path = "backbutton/back_button.png"
        self.backbuttonimage = PhotoImage(file=backbutton_path)
        backbutton = tk.Button(self, image=self.backbuttonimage, command=lambda: controller.show_page(MainMenu))
        backbutton.image = self.backbuttonimage  # Keep a reference to prevent garbage collection
        backbutton.place(x=0.0, y=0.0, width=83.0, height=54.0)

        common_font = ("Inter SemiBold", 80)
        common_color = "#000000"

        headers = ["Order ID", "Product", "Quantity", "Order Date", "Approve","Decline"]
        for col, header in enumerate(headers):
            label = tk.Label(self, text=header, borderwidth=1, relief=tk.RAISED,
                             font=("Helvetica", 24, "bold"),  # Adjust font size here
                             fg=common_color, padx=7, pady=10)  # Adjust padding here
            label.grid(row=1, column=col, sticky="ew")

        self.display_orders()

    def display_orders(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()

        for row_idx, order in enumerate(orders, start=2):
            for col, value in enumerate(order):
                label = tk.Label(self, text=value, borderwidth=1, relief=tk.GROOVE, font=("Helvetica", 16),
                                 fg="#000000")
                label.grid(row=row_idx, column=col, sticky="ew")

            # Using a default argument to capture 'oid' and 'cursor'
            btn_action = ttk.Button(self, text="Approve", command=lambda oid=order[0]: self.approve_order(oid))
            btn_action.grid(row=row_idx, column=len(order), sticky="ew")

            # Using a default argument to capture 'oid'
            btn_decline = ttk.Button(self, text="Decline", command=lambda oid=order[0]: self.perform_action(oid))
            btn_decline.grid(row=row_idx, column=len(order) + 1, sticky="ew")

        conn.close()

    def approve_order(self, oid):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        cursor.execute("SELECT product_id FROM orders WHERE id = ?", (oid,))
        product_id = cursor.fetchone()[0]

        cursor.execute("SELECT quantity from orders WHERE id = ?", (oid,))
        quantity = cursor.fetchone()[0]

        cursor.execute("SELECT p_quantity FROM products WHERE p_id = ?", (product_id,))
        original_quantity = cursor.fetchone()[0]

        updated_quantity = int(original_quantity) - int(quantity)

        cursor.execute("UPDATE products SET p_quantity = ? WHERE p_id = ?", (updated_quantity, product_id))
        cursor.execute("DELETE FROM orders WHERE id = ?", (oid,))

        conn.commit()
        conn.close()

    def perform_action(self, order_id):
        # Define your action here, for example:
        print("Performing action for order ID:", order_id)


    def show(self):
        self.lift()

class DeleteProductPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        def get_product_details():
            # Get the ID entered by the user
            upd_id = button_1.get()

            # Fetch the product details from the database based on the ID
            cursor.execute("SELECT p_name, p_description, p_price, p_quantity FROM products WHERE p_id=?", (upd_id,))
            product_data = cursor.fetchone()

            if product_data:
                # Set the fetched data in the respective entry fields
                button_2.delete(0, tk.END)
                button_2.insert(0, product_data[1])  # p_name
                button_3.delete(0, tk.END)
                button_3.insert(0, product_data[2])  # p_quantity
            else:
                mb.showerror('Error', 'Product not found')

        def delete_product():
            # Get the ID entered by the user
            del_id = button_1.get()

            # Fetch the product details from the database based on the ID
            cursor.execute("SELECT p_name, p_quantity FROM products WHERE p_id=?", (del_id,))
            product_data = cursor.fetchone()

            if product_data:
                if not button_2.get():  # Check if entry_2 is empty
                    # Delete the entire record from the database based on the ID
                    cursor.execute("DELETE FROM products WHERE p_id=?", (del_id,))
                    connector.commit()

                    mb.showinfo('Product deleted', 'The product was successfully deleted from your database')
                elif button_3.get().lower() == 'all':  # Check if entry_3 is 'all'
                    # Update quantity to 0 in the database based on the ID
                    cursor.execute("UPDATE products SET p_quantity=0 WHERE p_id=?", (del_id,))
                    connector.commit()

                    mb.showinfo('Quantity updated', 'Quantity set to 0 for the product in your database')
                else:
                    mb.showerror('Error', 'Invalid operation')
            else:
                mb.showerror('Error', 'Product not found')


        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        image_image_3_path = r"updateframe\image_1.png"

        self.image_1 = PhotoImage(file=image_image_3_path)
        image_1 = canvas.create_image(
            512.0,
            364.0,
            image=self.image_1
        )

        canvas.create_rectangle(
            320.9892578125,
            113.0,
            697.0108337402344,
            118.0,
            fill="#000000",
            outline="")

        canvas.create_text(
            326.0,
            56.0,
            anchor="nw",
            text="Database Updation",
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )

        canvas.create_text(
            27.0,
            234.0,
            anchor="nw",
            text="What’s the product:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        canvas.create_text(
            27.0,
            329.0,
            anchor="nw",
            text="How much stock to be deleted:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        canvas.create_text(
            30.0,
            135.0,
            anchor="nw",
            text="Please enter the id:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        button_image_1_path = r"deleteframe\entry_1.png"
        button_image_2_path = r"deleteframe\entry_2.png"
        button_image_3_path = r"deleteframe\entry_3.png"
        button_image_b1_path = r"deleteframe\button_1.png"
        button_image_b2_path = r"updateframe\button_1.png"


        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_1.image = self.button_image_1  # Keep a reference to prevent garbage collection
        button_1.place(x=388.0, y=129.5, width=405.0, height=60.0)

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        button_2 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_2.image = self.button_image_2  # Keep a reference to prevent garbage collection
        button_2.place(x=388.0, y=234.5, width=405.0, height=60.0)

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        button_3 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=1)
        button_3.image = self.button_image_3  # Keep a reference to prevent garbage collection
        button_3.place(x=388.0, y=410.5, width=405.0, height=60.0)

        self.button_image_4 = PhotoImage(file=button_image_b1_path)
        button_4 = tk.Button(self, image=self.button_image_4, command = delete_product)
        button_4.image = self.button_image_4  # Keep a reference to prevent garbage collection
        button_4.place(x=652.0, y=522.0, width=308.0, height=78.0)

        self.button_image_6 = PhotoImage(file=button_image_b2_path)
        button_6 = tk.Button(self, image=self.button_image_6, command = get_product_details)
        button_6.image = self.button_image_4  # Keep a reference to prevent garbage collection
        button_6.place(x=775.0, y=129.5, width=147.0, height=60.0)

class MainMenu(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=1,
            relief="ridge"
        )

        lp1 = LoginPage(parent,controller)
        name1 = lp1.entry_3.get()

        canvas.place(x=0, y=0)


        image_image_1_path = r"adminmenu\image_1.png"

        self.image_1 = PhotoImage(file=image_image_1_path)
        image_1 = canvas.create_image(
            205.0,
            364.0,
            image=self.image_1
        )



        canvas.create_text(
            500.0,
            46.0,
            anchor="nw",
            text='Welcome Admin',
            fill="#000000",
            font=("Inter SemiBold", 30 * -1)
        )

        button_image_1_path = r"adminmenu\button_1.png"
        button_image_2_path = r"adminmenu\button_2.png"
        button_image_3_path = r"adminmenu\button_3.png"
        button_image_4_path = r"adminmenu\button_4.png"
        button_image_5_path = r"frame1\button_5.png"

        # Not neede this button
        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Button(self, image=self.button_image_1, command=lambda: controller.show_page(OrderList))
        button_1.image = self.button_image_1
        button_1.place(x=494, y=121, width=221, height=180)

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        button_2 = tk.Button(self, image=self.button_image_2, command=lambda: controller.show_page(ProductMenu))
        button_2.image = self.button_image_2
        button_2.place(x=748, y=121, width=221, height=180)

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        button_3 = tk.Button(self, image=self.button_image_3, command=lambda: controller.show_page(SupplierManagementSystem))
        button_3.image = self.button_image_3
        button_3.place(x=494, y=319, width=221, height=180)

        self.button_image_4 = PhotoImage(file=button_image_4_path)
        button_4 = tk.Button(self, image=self.button_image_4, command=lambda: controller.show_page(ViewUsers))
        button_4.image = self.button_image_4
        button_4.place(x=748, y=319, width=221, height=180)

        backbutton_path = r"backbutton\back_button.png"
        self.backbuttonimage = PhotoImage(file=backbutton_path)
        backbutton = tk.Button(self, image=self.backbuttonimage, command=lambda: controller.show_page(LoginPage))
        backbutton.image = self.backbuttonimage  # Keep a reference to prevent garbage collection
        backbutton.place(x=865.0, y=602.0, width=83.0, height=54.0)
class SupplierManagementSystem(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        label = tk.Label(self, text="Supplier Management System")
        label.pack(padx=10, pady=10)

        self.connector = sqlite3.connect('supplier.db')
        self.cursor = self.connector.cursor()

        self.connector.execute(
            'CREATE TABLE IF NOT EXISTS Supplier (SUP_NAME TEXT, SUP_ID TEXT PRIMARY KEY NOT NULL, PRODUCT_NAME TEXT, PRODUCT_QUANTITY INTEGER)'
        )

        backbutton_path = "backbutton/back_button.png"
        self.backbuttonimage = PhotoImage(file=backbutton_path)
        backbutton = tk.Button(self, image=self.backbuttonimage, command=lambda: controller.show_page(MainMenu))
        backbutton.image = self.backbuttonimage  # Keep a reference to prevent garbage collection
        backbutton.place(x=0.0, y=0.0, width=83.0, height=54.0)

        # StringVars
        self.sup_name = StringVar()
        self.sup_id = StringVar()
        self.product_name = StringVar()
        self.product_quantity = StringVar()

        self.initialize_gui()

    def initialize_gui(self):
        # Frames
        left_frame = Frame(self, bg='LightSkyBlue')
        left_frame.place(x=0, y=30, relwidth=0.3, relheight=0.96)

        RT_frame = Frame(self, bg='DeepSkyBlue')
        RT_frame.place(relx=0.3, y=30, relheight=0.2, relwidth=0.7)

        RB_frame = Frame(self)
        RB_frame.place(relx=0.3, rely=0.24, relheight=0.785, relwidth=0.7)

        # Left Frame
        Label(left_frame, text='Supplier Name', bg='LightSkyBlue', font=('Georgia', 13)).place(x=98, y=25)
        Entry(left_frame, width=25, font=('Times New Roman', 12), textvariable=self.sup_name).place(x=45, y=55)

        Label(left_frame, text='Supplier ID', bg='LightSkyBlue', font=('Georgia', 13)).place(x=110, y=105)
        Entry(left_frame, width=25, font=('Times New Roman', 12), textvariable=self.sup_id).place(x=45, y=135)

        Label(left_frame, text='Product Name', bg='LightSkyBlue', font=('Georgia', 13)).place(x=90, y=185)
        Entry(left_frame, width=25, font=('Times New Roman', 12), textvariable=self.product_name).place(x=45, y=215)

        Label(left_frame, text='Product Quantity', bg='LightSkyBlue', font=('Georgia', 13)).place(x=75, y=265)
        Entry(left_frame, width=25, font=('Times New Roman', 12), textvariable=self.product_quantity).place(x=45, y=295)

        submit = Button(left_frame, text='Add new record', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=20, command=self.add_record)
        submit.place(x=50, y=375)

        clear = Button(left_frame, text='Clear fields', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=20, command=self.clear_fields)
        clear.place(x=50, y=435)

        # Right Top Frame
        Button(RT_frame, text='Delete supplier record', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=17, command=self.remove_record).place(x=8, y=30)
        Button(RT_frame, text='Delete all suppliers', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=17, command=self.delete_all_suppliers).place(x=178, y=30)
        Button(RT_frame, text='Update supplier details', font=('Gill Sans MT', 13), bg='SteelBlue', fg='white', width=17, command=self.update_record).place(x=348, y=30)

        # Right Bottom Frame
        Label(RB_frame, text='SUPPLIER INVENTORY', bg='DodgerBlue', font=('Noto Sans CJK TC', 15, 'bold')).pack(side=TOP, fill=X)

        self.tree = ttk.Treeview(RB_frame, selectmode=BROWSE, columns=('Supplier Name', 'Supplier ID', 'Product Name', 'Product Quantity'))

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
        surety = mb.askyesno('Are you sure?', 'Are you sure you want to delete all suppliers?\n\nThis command cannot be reversed')

        if surety:
            self.tree.delete(*self.tree.get_children())

            self.cursor.execute('DELETE FROM Supplier')
            self.connector.commit()

            mb.showinfo('Done', 'All suppliers were successfully deleted from the database.')
        else:
            return

    def update_record(self):
        def update():
            self.cursor.execute('UPDATE Supplier SET SUP_NAME=?, PRODUCT_NAME=?, PRODUCT_QUANTITY=? WHERE SUP_ID=?',
                                (self.sup_name.get(), self.product_name.get(), self.product_quantity.get(),
                                 self.sup_id.get()))
            self.connector.commit()

            self.clear_and_display()

            edit_window.destroy()  # Destroying the edit window after updating the record

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

        # Create a new Toplevel window for editing
        edit_window = Toplevel(self)
        edit_window.title("Update Record")

        Label(edit_window, text='Supplier Name').grid(row=0, column=0)
        sup_name_entry = Entry(edit_window, textvariable=self.sup_name)
        sup_name_entry.grid(row=0, column=1)

        Label(edit_window, text='Supplier ID').grid(row=1, column=0)
        sup_id_entry = Entry(edit_window, textvariable=self.sup_id)
        sup_id_entry.grid(row=1, column=1)

        Label(edit_window, text='Product Name').grid(row=2, column=0)
        product_name_entry = Entry(edit_window, textvariable=self.product_name)
        product_name_entry.grid(row=2, column=1)

        Label(edit_window, text='Product Quantity').grid(row=3, column=0)
        product_quantity_entry = Entry(edit_window, textvariable=self.product_quantity)
        product_quantity_entry.grid(row=3, column=1)

        # Button to confirm update
        update_button = Button(edit_window, text="Update", command=update)
        update_button.grid(row=4, columnspan=2)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1024x724")  # Set the initial size of the window to 800x600 pixels

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for PageClass in (SplashScreen,OrderList, SignUp,AddToCart,ProductMenu,ViewUsers, LoginPage, MainMenu, ServicesPage, GalleryPage, LoginSuccesful , LoginDenied, AddProductPage, UpdateProductPage, DeleteProductPage, ViewAllProductsPage, SupplierManagementSystem):
            page = PageClass(container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(SplashScreen)



    def show_page(self, page):
        self.pages[page].show()



if __name__ == "__main__":
    app = Application()
    app.mainloop()   
# Front-end End