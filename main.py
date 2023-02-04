from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    # print(len(website))
    email = email_entry.get()
    # print(len(email))
    password = password_entry.get()
    # print(len(password))
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)

        # This should happen if file is not found
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="This data file does not exist.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist yet.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=18)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=32)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "vashu@gmail.com")
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)


# Buttons
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)
generate_password_button = Button(text="Generate Pass", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()