    with open(file="data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)