import time
import tkinter as tk
from tkinter import Canvas, Button, PhotoImage


class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def show(self):
        self.lift()




class HomePage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Home Page")
        label.pack(padx=10, pady=10)

        about_button = tk.Button(self, text="Go to About Page", command=lambda: controller.show_page(AboutPage))
        about_button.pack()


class AboutPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)


        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=0,
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


        image_image_1_path = r"C:\Users\mruna\hactoberfest\frame1\image_1.png"

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
            text="First name ",
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

        login_button_path = r"C:\Users\mruna\hactoberfest\frame0\button_1.png"
        button_image_2_path = r"C:\Users\mruna\hactoberfest\frame0\entry_1.png"
        button_image_3_path = r"C:\Users\mruna\hactoberfest\frame0\entry_2.png"
        button_image_4_path = r"C:\Users\mruna\hactoberfest\frame0\entry_3.png"
        button_image_5_path = r"C:\Users\mruna\hactoberfest\frame0\entry_4.png"

        self.login_button = PhotoImage(file=login_button_path)
        button_1 = tk.Button(self, image=self.login_button, command=lambda: controller.show_page(LoginSuccesful))
        button_1.image = self.login_button
        button_1.place(x=777, y=622, width=137, height=58)

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        self.entry_2 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=0)
        self.entry_2.image = self.button_image_2
        self.entry_2.place(x=586, y=223, width=367, height=45)

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        self.entry_3 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=0)
        self.entry_3.image = self.button_image_3
        self.entry_3.place(x=586, y=325, width=367, height=45)

        self.button_image_4 = PhotoImage(file=button_image_4_path)
        self.entry_4 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=0)
        self.entry_4.image = self.button_image_4
        self.entry_4.place(x=586, y=427, width=367, height=45)

        self.button_image_5 = PhotoImage(file=button_image_5_path)
        self.entry_5 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=0)
        self.entry_5.image = self.button_image_5
        self.entry_5.place(x=586, y=529, width=367, height=45)

        def clear_entries(self):
            self.entry_2.delete(0, tk.END)
            self.entry_3.delete(0, tk.END)
            self.entry_4.delete(0, tk.END)
            self.entry_5.delete(0, tk.END)



class ContactPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_text(
            347.0,
            66.0,
            anchor="nw",
            text="Welcome User!",
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )


        image_image_1_path = r"C:\Users\mruna\hactoberfest\frame1\image_1.png"

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

        button_image_1_path = r"C:\Users\mruna\hactoberfest\frame1\button_1.png"
        button_image_2_path = r"C:\Users\mruna\hactoberfest\frame1\button_2.png"
        button_image_3_path = r"C:\Users\mruna\hactoberfest\frame1\button_3.png"
        button_image_4_path = r"C:\Users\mruna\hactoberfest\frame1\button_4.png"
        button_image_5_path = r"C:\Users\mruna\hactoberfest\frame1\button_5.png"

        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Button(self, image=self.button_image_1, command=lambda: controller.show_page(HomePage))
        button_1.image = self.button_image_1
        button_1.place(x=830, y=563, width=137, height=58)

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        button_2 = tk.Button(self, image=self.button_image_2, command=lambda: controller.show_page(AddProductPage))
        button_2.image = self.button_image_2
        button_2.place(x=347, y=232, width=281, height=69)

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        button_3 = tk.Button(self, image=self.button_image_3, command=lambda: print("Button 3 clicked"))
        button_3.image = self.button_image_3
        button_3.place(x=686, y=232, width=281, height=69)

        self.button_image_4 = PhotoImage(file=button_image_4_path)
        button_4 = tk.Button(self, image=self.button_image_4, command=lambda: print("Button 4 clicked"))
        button_4.image = self.button_image_4
        button_4.place(x=347, y=365, width=281, height=69)

        self.button_image_5 = PhotoImage(file=button_image_5_path)
        button_5 = tk.Button(self, image=self.button_image_5, command=lambda: controller.show_page(UpdateProductPage))
        button_5.image = self.button_image_5
        button_5.place(x=686, y=365, width=281, height=69)

class AddProductPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Services Page")
        label.pack(padx=10, pady=10)

        # Add a button to switch to the home page
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=1024,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        canvas.create_text(
            56.0,
            334.0,
            anchor="nw",
            text="What are the stocks:",
            fill="#000000",
            font=("Inter SemiBold", 32 * -1)
        )

        image_image_1_path = r"C:\Users\mruna\hactoberfest\frame2\image_1.png"

        # Add images to buttons
        self.image_1 = PhotoImage(file=image_image_1_path)
        image_1 = canvas.create_image(
            720.0,
            512.0,
            image=self.image_1
        )

        canvas.create_text(
            56.0,
            451.0,
            anchor="nw",
            text="Please enter the price:",
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
            56.0,
            217.0,
            anchor="nw",
            text="What’s the product:",
            fill="#000000",
            font=("Inter SemiBold", 32 * -1)
        )

        button_image_1_path = r"C:\Users\mruna\hactoberfest\frame2\entry_1.png"
        button_image_2_path = r"C:\Users\mruna\hactoberfest\frame2\entry_2.png"
        button_image_3_path = r"C:\Users\mruna\hactoberfest\frame2\entry_3.png"
        button_image_4_path = r"C:\Users\mruna\hactoberfest\frame2\button_1.png"
        button_image_5_path = r"C:\Users\mruna\hactoberfest\frame2\button_2.png"

        # Add images to buttons
        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=0)
        button_1.image = self.button_image_1  # Keep a reference to prevent garbage collection
        button_1.place(x=443.0, y=211.5, width=480.0, height=52.0)

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        button_2 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=0)
        button_2.image = self.button_image_2  # Keep a reference to prevent garbage collection
        button_2.place(x=443.5, y=331.5, width=480.0, height=52.0)

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        button_3 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=0)
        button_3.image = self.button_image_3  # Keep a reference to prevent garbage collection
        button_3.place(x=443.0, y=445.5, width=480.0, height=52.0)

        self.button_image_4 = PhotoImage(file=button_image_4_path)
        button_4 = tk.Button(self, image=self.button_image_4, command=lambda: controller.show_page(HomePage))
        button_4.image = self.button_image_4  # Keep a reference to prevent garbage collection
        button_4.place(x=56.0, y=583.0, width=392.0, height=62.0)

        self.button_image_5 = PhotoImage(file=button_image_5_path)
        button_5 = tk.Button(self, image=self.button_image_5, command=lambda: print("Button 5 clicked"))
        button_5.image = self.button_image_5  # Keep a reference to prevent garbage collection
        button_5.place(x=531.0, y=583.0, width=392.0, height=62.0)

class UpdateProductPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Update Product Page")
        label.pack(padx=10, pady=10)

        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)

        image_image_3_path = r"C:\Users\mruna\hactoberfest\frame3\image_1.png"

        self.image_1 = PhotoImage(file=image_image_3_path)
        image_1 = canvas.create_image(
            720.0,
            512.0,
            image=self.image_1
        )

        canvas.create_text(
            45.0,
            361.0,
            anchor="nw",
            text="What’s the product:",
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )

        canvas.create_text(
            45.0,
            503.0,
            anchor="nw",
            text="How much is the stock:",
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )

        canvas.create_text(
            55.0,
            218.0,
            anchor="nw",
            text="Please enter the id:",
            fill="#000000",
            font=("Inter SemiBold", 40 * -1)
        )

        button_image_1_path = r"C:\Users\mruna\hactoberfest\frame3\entry_1.png"
        button_image_2_path = r"C:\Users\mruna\hactoberfest\frame3\entry_3.png"
        button_image_3_path = r"C:\Users\mruna\hactoberfest\frame3\entry_4.png"
        button_image_4_path = r"C:\Users\mruna\hactoberfest\frame3\button_1.png"
        button_image_5_path = r"C:\Users\mruna\hactoberfest\frame3\button_2.png"
        

        # Add images to buttons
        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=0)
        button_1.image = self.button_image_1  # Keep a reference to prevent garbage collection
        button_1.place(x=443.0, y=211.5, width=480.0, height=52.0)

        self.button_image_2 = PhotoImage(file=button_image_2_path)
        button_2 = tk.Entry(self, bd=0, bg="#EDEDED", fg="#000716", highlightthickness=0)
        button_2.image = self.button_image_2  # Keep a reference to prevent garbage collection
        button_2.place(x=443.5, y=331.5, width=480.0, height=52.0)

        self.button_image_3 = PhotoImage(file=button_image_3_path)
        button_3 = tk.Entry(self, bd=0, bg= "#EDEDED", fg= "#000716", highlightthickness=0)
        button_3.image = self.button_image_3  # Keep a reference to prevent garbage collection
        button_3.place(x=443.0, y=445.5, width=480.0, height=52.0)
        
        self.button_image_4 = PhotoImage(file=button_image_4_path)
        button_4 = tk.Button(self, image=self.button_image_4, command=lambda: controller.show_page(HomePage))
        button_4.image = self.button_image_4  # Keep a reference to prevent garbage collection
        button_4.place(x=56.0, y=583.0, width=392.0, height=62.0)

        self.button_image_5 = PhotoImage(file=button_image_5_path)
        button_5 = tk.Button(self, image=self.button_image_5, command=lambda: print("Button 5 clicked"))
        button_5.image = self.button_image_5  # Keep a reference to prevent garbage collection
        button_5.place(x=531.0, y=583.0, width=392.0, height=62.0)


class ServicesPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Services Page")
        label.pack(padx=10, pady=10)

        home_button = tk.Button(self, text="Go to Home Page", command=lambda: controller.show_page(ContactPage))
        home_button.pack()


class GalleryPage(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)
        label = tk.Label(self, text="Gallery Page")
        label.pack(padx=10, pady=10)

        home_button = tk.Button(self, text="Go to Home Page", command=lambda: controller.show_page(ServicesPage))
        home_button.pack()

class LoginSuccesful(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=728,
            width=1024,
            bd=0,
            highlightthickness=0,
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


        succes_image_path = r"C:\Users\mruna\hactoberfest\succesframe\image_1.png"

        self.image_1 = PhotoImage(file=succes_image_path)
        image_1 = canvas.create_image(
            512.0,
            316.0,
            image=self.image_1,

        )

        button_image_1_path = r"C:\Users\mruna\hactoberfest\succesframe\next.png"
        self.button_image_1 = PhotoImage(file=button_image_1_path)
        button_1 = tk.Button(self, image=self.button_image_1, command=lambda: controller.show_page(ContactPage))
        button_1.image = self.button_image_1
        button_1.place(x=830, y=563, width=137, height=58)



class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1024x724")  # Set the initial size of the window to 800x600 pixels

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for PageClass in (HomePage, AboutPage, ContactPage, ServicesPage, GalleryPage, LoginSuccesful,AddProductPage, UpdateProductPage):
            page = PageClass(container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(AboutPage)

    def show_page(self, page):
        self.pages[page].show()



if __name__ == "__main__":
    app = Application()
    app.mainloop()
