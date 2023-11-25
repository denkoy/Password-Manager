from tkinter import Entry,Label,Button,messagebox
import tkinter
import random
import json
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0","1","2","3","4","5","6","7","8","9"]
special_symbol = ["@","$","%","*"]


def generate_clicked(object):
    password = ""
    length = random.randint(10, 12)
    for i in range(0, length):
        type = random.randint(1, 3)
        if type == 1:
            password += random.choice(letters)
        elif type == 2:
            password += random.choice(numbers)
        else:
            password += random.choice(special_symbol)
    object.password.delete(0, tkinter.END)  # Clear the existing content
    object.password.insert(0, password)

def data_search(data_instance):

    site = data_instance.site_name.get()
    try:
        file_read = open("data.json", "r")
    except FileNotFoundError:
        raise FileNotFoundError("There is nothing to search of.")
    else:
        data = json.load(file_read)
        if site in data:
            secure_data=data[site]
            message=messagebox.showinfo(title=site,message=f"email: {secure_data["email"]}\n password: {secure_data["password"]}")
        else:
            message=messagebox.showinfo(title=site,message=f"No such site in the manager!")

        file_read.close()



        file_read.close()
def data_save(data_instance):
    email = data_instance.email.get()
    password = data_instance.password.get()
    site = data_instance.site_name.get()

    new_data = {
        site: {
            "email": email,
            "password": password
        }
    }

    is_ok = messagebox.askokcancel(title=site,
                                   message=f"Are you sure those are the details?\n email: {email}\n password: {password}\n")

    if is_ok:
        try:
            file_read = open("data.json", "r")
        except FileNotFoundError:
            file_write = open("data.json", "w")
            json.dump(new_data, file_write, indent=4)
            file_write.close()
        else:
            data = json.load(file_read)
            data.update(new_data)
            file_write = open("data.json", "w")
            json.dump(data, file_write, indent=4)
            file_write.close()
            file_read.close()

        # Clear the entries after saving data
        data_instance.email.delete(0, tkinter.END)
        data_instance.password.delete(0, tkinter.END)
class Data:
    def __init__(self):
        self.site_name=Entry(width=50)
        self.site_name.place(x=180,y=250)
        self.site_label = Label(text="Site:", font=("Arial", 10,"bold"),bg="gray",fg="white")
        self.site_label.place(x=80, y=250)

        self.email = Entry(width=50)
        self.email.place(x=180, y=280)
        self.email_label = Label(text="Email:", font=("Arial", 10, "bold"), bg="gray", fg="white")
        self.email_label.place(x=80, y=280)

        self.password = Entry(width=20)
        self.password.place(x=180, y=310)
        self.password_label = Label(text="Password:", font=("Arial", 10, "bold"), bg="gray", fg="white")
        self.password_label.place(x=80, y=310)

        self.button_generate = Button(text="Generate",command=lambda: generate_clicked(self))
        self.button_generate.place(x=425, y=310)

        self.button_add = Button(text="Add",width=42,command=lambda: data_save(self))
        self.button_add.place(x=180, y=340)

        self.button_search = Button(text="Search",command=lambda:data_search(self))
        self.button_search.place(x=365,y=310)





