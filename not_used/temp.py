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
        button_4 = tk.Button(self, image=self.button_image_4) #, command = clear_fields)
        button_4.image = self.button_image_4  # Keep a reference to prevent garbage collection
        button_4.place(x=56.0, y=583.0, width=392.0, height=62.0)

        self.button_image_5 = PhotoImage(file=button_image_5_path)
        button_5 = tk.Button(self, image=self.button_image_5, command = add_product)
        button_5.image = self.button_image_5  # Keep a reference to prevent garbage collection
        button_5.place(x=531.0, y=583.0, width=392.0, height=62.0)


#####
class AddProductPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Services Page")
        label.pack(padx=10, pady=10)
initialise class like this