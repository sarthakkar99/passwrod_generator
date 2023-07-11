from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters=random.randint(8, 10)
    nr_symbols=random.randint(2, 4)
    nr_numbers=random.randint(2, 4)

    password_list=[]

    """for char in range(nr_letters):
      password_list.append(random.choice(letters))"""
    password_list1=[random.choice(letters) for char in range(nr_letters)]
    """for char in range(nr_symbols):
      password_list += random.choice(symbols)"""
    password_list2=[random.choice(symbols) for char in range(nr_symbols)]
    """for char in range(nr_numbers):
      password_list += random.choice(numbers)"""
    password_list3=[random.choice(numbers) for char in range(nr_numbers)]
    password_list=password_list1 + password_list2 + password_list3
    random.shuffle(password_list)

    password=""
    for char in password_list:
        password+=char
    input3.insert(0,f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def button_clicked():
    name=input.get()
    web_pass=input3.get()
    email=input1.get()
    new_data={name:{"email": email, "password": web_pass}}
    if len(name)==0 or len(web_pass)==0:
        messagebox.showinfo(title="Wrong website Name", message="No Empty\n ")
    else:
        try:
            with open("data.json", "r") as f:
                data=json.load(f)
                data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
                input.delete(0, END)
                input3.delete(0, END)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
                input.delete(0, END)
                input3.delete(0, END)


def Search():
    name=input.get()
    with open("data.json", "r") as f:
        data=json.load(f)
        print(data)
        for name1 in data.keys():
            print(name1)
            if name1==name:
                #email=name1['email']
                #print(email)
                messagebox.showinfo(f"{data[name1]['email']} and {data[name1]['password']}")
            else:
                messagebox.showinfo("None")
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
canvas=Canvas(width=200, height=200, highlightthickness=0)
logo=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)
mylabel=Label(text="Website", font=("courier", 12, "bold"))
mylabel.grid(row=1, column=0)
input=Entry(width=21)
print(input.get())
button1=Button(text="Search", command=Search)
button1.config(width=15)
button1.grid(column=2, row=1)
input.grid(column=1, row=1, columnspan=2)
mylabel1=Label(text="Email/Username", font=("courier", 12, "bold"))
mylabel1.grid(row=2, column=0)
input1=Entry(width=35)
print(input1.get())
input1.insert(0, "sarthak.kar21@gmail.com")
input1.grid(column=1, row=2, columnspan=2)
mylabel2=Label(text="Password", font=("courier", 12, "bold"))
mylabel2.grid(row=3, column=0)
button=Button(text="Generate Password", command=password)
button.grid(column=2, row=3)
input3=Entry(width=20)
print(input3.get())
input3.grid(column=1, row=3)
button=Button(text="Add", command=button_clicked)
button.config(width=36)
button.grid(column=0, row=4, columnspan=3)

# canvas.pack()
window.mainloop()
