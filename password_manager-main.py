from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# pyper clip helps in coping pasword directly to clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pswd_entry.insert(END, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    passwordd = pswd_entry.get()
    email = username_entry.get()
    website = web_entry.get()

    if len(website) == 0 or len(passwordd) == 0:
        messagebox.showwarning(message='please fill all the necessary fields')
    else:
        is_ok =messagebox.askokcancel(title= website, message= f"Are you sure you want to save \n website:{website} \n Email: {email}"
                                                        f"\n passwird: {passwordd}")
        if is_ok:
            with open('data.txt', "a") as data:
                data.write(f"{website} | {email} | {passwordd}\n")
                web_entry.delete(0, END)
                pswd_entry.delete(0,END)
        else:
            web_entry.delete(0, END)
            pswd_entry.delete(0, END)


        # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0, column=1)

# lables
web_lable = Label(text="Website")
web_lable.grid(row=1, column=0)

username_lable = Label(text="Email/Username")
username_lable.grid(row=2, column=0)

pswd_lable = Label(text="Password")
pswd_lable.grid(row=3, column=0)

#entries
web_entry = Entry()
web_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
web_entry.focus()


username_entry = Entry()
username_entry.grid(row=2, column=1, columnspan=2,sticky=EW)
username_entry.insert(END, "vaaish0408@gmail.com")


pswd_entry = Entry()
pswd_entry.grid(row=3, column=1, sticky=EW)


#buttons
generate_password = Button(text="Generate Password", command= generatepassword)
generate_password.grid(row=3, column=2)

add_button =Button(text= "Add", width= 36, command=save)
add_button.grid(row=4, column= 1, columnspan=2)




window.mainloop()


