from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import json


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x700+100+50")
        self.root.resizable(False, False)



        def main_page():
            # Login Frame
            frame_login = Frame(self.root, bg="white")
            frame_login.place(x=330, y=150, width=500, height=400)

            # Title & subtitle
            Label(frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(
                x=90, y=30)
            Label(frame_login, text="Members Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
                  bg="white").place(x=90, y=100)

            # Username
            Label(frame_login, text="ID", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                x=90, y=140)
            self.username = Entry(frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
            self.username.place(x=90, y=170, width=320, height=35)

            # Password
            Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",
                  bg="white").place(x=90, y=210)
            self.password = Entry(frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
            self.password.place(x=90, y=240, width=320, height=35)




            # Button
            Button(frame_login, text="forgot password?", command=forgot_password, bd=0, cursor="hand2",
                   font=("Goudy old style", 12), fg="#6162FF", bg="white").place(x=90, y=280)
            Button(frame_login, cursor="hand2", text="Login", bd=0,command=logging_in,
                   font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y=320, width=180,
                                                                                 height=40)



            # register Button
            Button(frame_login, text="Register", command=register_function, bd=0, cursor="hand2",
                   font=("Goudy old style", 12), fg="#6162FF", bg="white").place(x=350, y=320)

        def End_Page():
            # Login Frame
            frame_login = Frame(self.root, bg="white")
            frame_login.place(x=330, y=150, width=500, height=400)

            # Title & subtitle
            Label(frame_login, text="Congratulations", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(
                x=90, y=30)

        def register_function():
            Register = Frame(self.root, bg="white", )
            Register.place(x=330, y=150, width=500, height=400)
            Label(text="Register", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=420, y=180)
            # Username
            Label(text="ID", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=420, y=290)
            self.username = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.username.place(x=420, y=320, width=320, height=35)

            # Password
            Label(text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
                x=420, y=360)
            self.password = Entry(font=("Goudy old style", 15), bg="#E7E6E6", show='*')
            self.password.place(x=420, y=390, width=320, height=35)

            def reg():
                con = True
                username = self.username.get()
                password = self.password.get()
                data = {"username": username, "password": password}

                with open('accounts.json', 'r+') as cred_file:
                    table_json = json.load(cred_file)

                for acc in table_json["accounts"]:
                    if self.username.get() == "" or self.password.get() == "":
                        messagebox.showerror("Error", "Please Fill The Required info")
                        con = False
                        break

                    if data["username"] in acc["username"]:
                        messagebox.showerror("Error", "User already Exists")
                        con = False
                        break

                if con is True:
                    table_json["accounts"].append(data)
                    with open('accounts.json', 'w') as cred_file:
                        json.dump(table_json, cred_file, indent=4)
                        messagebox.showinfo(message='Account created successfully')
                        main_page()

                        # Confirm

            Button(cursor="hand2", text="Confirm", command=reg, bd=0, font=("Goudy old style", 15), bg="#6162FF",
                   fg="white").place(x=420, y=475, width=180, height=40)
            # return button
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=620, y=475, width=100, height=40)

        def forgot_password():
            Ptitle = Frame(self.root, bg="white")
            Ptitle.place(x=330, y=150, width=500, height=400)
            Label(text="Password Reset", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=420,
                                                                                                      y=180)

            # Password
            Label(text="New Password", font=("Goudy old style", 14, "bold"), fg="grey", bg="white").place(
                x=420, y=320)
            self.newpass = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.newpass.place(x=420, y=350, width=320, height=35)

            # Username
            Label(text="ID", font=("Goudy old style", 14, "bold"), fg="grey", bg="white").place(x=420, y=255)
            self.ID = Entry(font=("Goudy old style", 15), bg="#E7E6E6")
            self.ID.place(x=420, y=285, width=320, height=35)

            # confirm_new_pass
            Label(text="Confirm", font=("Goudy old style", 15, "bold"), fg="grey",
                  bg="white").place(x=420, y=385)
            self.confirm_new_pass = Entry(font=("Goudy old style", 14), bg="#E7E6E6")
            self.confirm_new_pass.place(x=420, y=415, width=320, height=35)

            def pass_change():
                ID = self.ID.get()
                password = self.newpass.get()
                cpassword = self.confirm_new_pass.get()
                data = {"username": ID, "password": password}
                cond = True

                with open('accounts.json', 'r') as cred_file:
                    table_json = json.load(cred_file)


                for acc in table_json["accounts"]:

                    if data["username"] == acc["username"]:
                        cond = False

                if cond:
                    messagebox.showerror("Error", "User Dont Exists!")

                if cpassword != password:
                    messagebox.showerror("Error", "Passwords Dont Match")
                    cond = False
                else:
                    cond = True

                if cond:
                 for acc in table_json["accounts"]:
                     if data["username"] == acc["username"]:
                        acc["password"] = password
                        print(acc)

                        with open('accounts.json', 'w') as cred_file:
                            json.dump(table_json, cred_file, indent=4)
                            main_page()

            # Confirm
            Button(cursor="hand2", text="Confirm", command=pass_change, bd=0, font=("Goudy old style", 15),
                   bg="#6162FF",
                   fg="white").place(x=420, y=475, width=180, height=40)
            # return button
            Button(cursor="hand2", text="Return", bd=0, command=main_page, font=("Goudy old style", 15),
                   bg="#6162FF", fg="white").place(x=620, y=475, width=100, height=40)

        # Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=330, y=150, width=500, height=400)

        # Title & subtitle
        Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90,
                                                                                                           y=30)
        Label(Frame_login, text="Members Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
              bg="white").place(x=90, y=100)

        # Username
        Label(Frame_login, text="ID", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(
            x=90, y=140)
        self.username = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320, height=35)

        # Password
        Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",
              bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

        def logging_in():
            username = self.username.get()
            print(username)
            password = self.password.get()
            print(password)
            data = {"username": username, "password": password}
            with open('accounts.json', 'r+') as cred_file:
                table_json = json.load(cred_file)

            add = True

            for acc in table_json["accounts"]:
                if data["username"] == acc["username"] and data["password"] == acc["password"]:
                    messagebox.showinfo(" ","Logged In")
                    add = False
                    End_Page()
            if add:
                messagebox.showerror("Error","ID or Password are wrong , please try again")



        # Button
        Button(Frame_login, text="forgot password?", command=forgot_password, bd=0, cursor="hand2",
               font=("Goudy old style", 12), fg="#6162FF", bg="white").place(x=90, y=280)
        Button(Frame_login, cursor="hand2", text="Login", command= logging_in,  bd=0,  # command=self.check_function
               font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y=320, width=180, height=40)

        # register Button
        Button(Frame_login, text="Register", command=register_function, bd=0, cursor="hand2",
               font=("Goudy old style", 12), fg="#6162FF", bg="white").place(x=350, y=320)


root = Tk()
# Open Image
bg_pic = Image.open(r"idk.jpg")
# Resized Image
# resized = bg_pic.resize((1199, 850), Image.ANTIALIAS)

bg = ImageTk.PhotoImage(bg_pic)
label_bgImage = Label(root, image=bg)
label_bgImage.place(x=0, y=0)
obj = Login(root)
root.mainloop()
