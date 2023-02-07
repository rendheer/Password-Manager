from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Added in file password_generator.py as a method and imported it here in this file
def password_gen():
    new_password = generate_password()
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data_old.json", "r") as data_file:
            data = json.load(data_file)
            # print(data[website_entry.get()]["email"])
    except FileNotFoundError:
        messagebox.showwarning(title="File Not Found", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.askokcancel(title=website, message=f"Website: {website}\n Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = str(website_entry.get())
    email = str(email_entry.get())
    password = str(password_entry.get())
    line = f"{website} | {email} | {password} \n"
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # fresh_data = {
    #     "new_website": {
    #         "email": "new_email",
    #         "password": "new_password",
    #     }
    # }
    #
    # # if len(website) == 0 or len(password) == 0 or len(email) == 0:
    # with open("data_file.json", "r") as file:
    #     # json.dump(new_data, file, indent=4)
    # #     print(new_data)
    #     data = json.load(file)
    #     data.update(fresh_data)
    #
    # with open("data_file.json", "w") as file:
    #     json.dump(data, file, indent=4)

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Incomplete Fields", message="The fields cannot be empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website}  \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            print("OK")
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    print(data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            # with open("data.txt", "a") as data_file:
            #     data_file.write(line)
            # website_entry.delete(0, END)
            # password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 16, "bold"))
website_label.grid(column=0, row=1)
website_label.config(padx=10, pady=10)

website_entry = Entry(width=18)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_label = Label(text="Email/Username:", font=("Arial", 16, "bold"))
email_label.grid(column=0, row=2)
email_label.config(padx=10, pady=10)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "rendheerjoshy@gmail.com")

password_label = Label(text="Email/Username:", font=("Arial", 16, "bold"))
password_label.grid(column=0, row=3)
password_label.config(padx=10, pady=10)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

gen_password_button = Button(text="Generate Password", command=password_gen)
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()