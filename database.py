import sqlite3
import tkinter as tk
from tkinter import CENTER, ttk
import os
from tkinter.messagebox import askyesno

#can add the ability to have different users depending on their login

dbtest = tk.Tk()
dbtest.title('db test')
window_width = 400
window_height = 500
screen_width = dbtest.winfo_screenwidth()                     #these 5 lines put the window in the middle of the screen
screen_height = dbtest.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)                      
center_y = int(screen_height / 2 - window_height / 2)
dbtest.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')   
dbtest.resizable(False, False)
font = 'fira code'

#functions
def clear_data():
    answer = askyesno(title='confirmation',
        message='Are you sure that you want to clear the database?')
    if answer:
        os.remove("password.db") 
        conn = sqlite3.connect('password.db')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE passwords (
            website text,
            username text,
            password text
            )""")
        conn.commit()
        conn.close()

# maybe call a function to destroy the widget and then remake it, then exit
def save():         
    conn = sqlite3.connect('password.db')
    cur = conn.cursor()
    new_website = str(website.get())
    new_username = str(username.get())
    new_password = str(password.get())
    cur.execute("INSERT INTO passwords VALUES (?,?,?)", (new_website, new_username, new_password))
    conn.commit()
    conn.close()

    exit()

def cancel():
    exit()

def save_gen_pass():
    with open('new_pass.txt', 'r') as f:
        lines = f.readlines()
    os.remove('new_pass.txt')
    password_entry.insert(0, lines)


#widgets
header_label = ttk.Label(
    dbtest, 
    text= 'Save log in credentials:',
    font=(f'{font}', 15)
)

website = tk.StringVar()
website_label = ttk.Label(
    dbtest, 
    text= 'Website:',
    font=(f'{font}', 12)
)
website_entry = ttk.Entry(
    dbtest,
    justify = CENTER,
    textvariable = website,
)

username = tk.StringVar()
username_label = ttk.Label(
    dbtest, 
    text= 'Username:',
    font=(f'{font}', 12)
)
username_entry = ttk.Entry(
    dbtest,
    justify = CENTER,
    textvariable = username,
)

password = tk.StringVar()
password_label = ttk.Label(
    dbtest, 
    text= 'Password:',
    font=(f'{font}', 12)
)
password_entry = ttk.Entry(
    dbtest,
    justify = CENTER,
    textvariable = password,
    show = '*'
)

save_button = ttk.Button(
    dbtest,
    text = 'Save',
    command = save
)

cancel_button = ttk.Button(
    dbtest,
    text = 'Cancel',
    command = cancel
)

removeDB_button = ttk.Button(
    dbtest,
    text = 'Clear database',
    command = clear_data
)

use_gen_pass = ttk.Button(
    dbtest,
    text = 'Generated password',
    command = save_gen_pass
)


#grid and setup
header_label.grid(column = 0, row = 0, sticky = tk.EW, padx = 20, pady = 15, columnspan = 2)
website_label.grid(column = 0, row = 1, sticky = tk.W, padx = 20, pady = 15)
username_label.grid(column = 0, row = 2, sticky = tk.W, padx = 20, pady = 15)
password_label.grid(column = 0, row = 3, sticky = tk.W, padx = 20, pady = 15)
website_entry.grid(column = 1, row = 1, sticky = tk.EW, padx = 20, pady = 15, ipadx = 50, ipady = 3)
username_entry.grid(column = 1, row = 2, sticky = tk.EW, padx = 20, pady = 15, ipadx = 50, ipady = 3)
password_entry.grid(column = 1, row = 3, sticky = tk.EW, padx = 20, pady = 15, ipadx = 50, ipady = 3)
save_button.grid(column = 0, row = 4, sticky = tk.W, padx = 25, pady = 50, ipadx = 5, ipady = 3)
cancel_button.grid(column = 1, row = 4, sticky = tk.W, padx = 5, pady = 50, ipadx = 5, ipady = 3)
removeDB_button.grid(column = 0, row = 6, sticky = tk.W, padx = 5, pady = 5, ipadx = 5, ipady = 3)
use_gen_pass.grid(column = 0, row = 5, sticky = tk.W, padx = 5, pady = 5, ipadx = 5, ipady = 3)



dbtest.mainloop()