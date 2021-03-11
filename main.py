from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    with open(file="data.txt", mode="a") as file:
        file.write(f"{website} | {email} | {password}\n")
        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

website_text = Label(text="Website: ")
website_text.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_text = Label(text="Email/Username: ")
email_text.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "elmeholt@gmail.com")

password_text = Label(text="Password: ")
password_text.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

password_generate_button = Button(text="Generate password")
password_generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

# width: 35 för website / email
# width 21 för password fält
# width 36 för add-knappen
