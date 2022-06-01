import sqlite3
import tkinter as tk
from tkinter import CENTER, ttk

dbtest = tk.Tk()
dbtest.title('db test')
window_width = 400
window_height = 500
screen_width = dbtest.winfo_screenwidth()                                  #these 5 lines put the window in the middle of the screen
screen_height = dbtest.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)                      
center_y = int(screen_height / 2 - window_height / 2)
dbtest.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')   
dbtest.resizable(False, False)
font = 'fira code'

#functions
if 0 == 1:
    conn = sqlite3.connect('password.db')

    cur = conn.cursor()

    # cur.execute("""CREATE TABLE passwords (
    #     email text, 
    #     password text
    #     )""")

    # cur.execute("""INSERT INTO passwords VALUES """)

    conn.commit()
    conn.close()




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
)




#grid and setup
header_label.grid(column = 0, row = 0, sticky = tk.EW, padx = 20, pady = 15, columnspan = 2)
website_label.grid(column = 0, row = 1, sticky = tk.W, padx = 20, pady = 15)
username_label.grid(column = 0, row = 2, sticky = tk.W, padx = 20, pady = 15)
password_label.grid(column = 0, row = 3, sticky = tk.W, padx = 20, pady = 15)
website_entry.grid(column = 1, row = 1, sticky = tk.EW, padx = 20, pady = 15, ipadx = 50, ipady = 3)
username_entry.grid(column = 1, row = 2, sticky = tk.EW, padx = 20, pady = 15, ipadx = 50, ipady = 3)
password_entry.grid(column = 1, row = 3, sticky = tk.EW, padx = 20, pady = 15, ipadx = 50, ipady = 3)



dbtest.mainloop()