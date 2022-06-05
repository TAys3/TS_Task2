import hashlib
import tkinter as tk
from tkinter import CENTER, ttk

#can add the ability to have different users depending on their login

login = tk.Tk()
login.title('Log in')
window_width = 300
window_height = 200
screen_width = login.winfo_screenwidth()                                  #these 5 lines put the window in the middle of the screen
screen_height = login.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)                      
center_y = int(screen_height / 2 - window_height / 2)
login.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')   
login.resizable(False, False)
login.iconbitmap('./Resources/lock_img.ico')
font = 'fira code'

#functions
def log_in():
    pass



header_label = ttk.Label(
    login, 
    text= 'Log in:',
    font=(f'{font}', 15)
)

username = tk.StringVar()
username_label = ttk.Label(
    login, 
    text= 'Username:',
    font=(f'{font}', 12)
)
username_entry = ttk.Entry(
    login,
    justify = CENTER,
    textvariable = username,
)

password = tk.StringVar()
password_label = ttk.Label(
    login, 
    text= 'Password:',
    font=(f'{font}', 12)
)
password_entry = ttk.Entry(
    login,
    justify = CENTER,
    textvariable = password,
)

save_button = ttk.Button(
    login,
    text = 'Save',
    command = log_in
)



header_label.grid(column = 0, row = 0, sticky = tk.EW, padx = 20, pady = 15, columnspan = 2)
username_label.grid(column = 0, row = 1, sticky = tk.W, padx = 20, pady = 15)
username_entry.grid(column = 1, row = 1, sticky = tk.W, padx = 20, pady = 15)
password_label.grid(column = 0, row = 2, sticky = tk.W, padx = 20, pady = 15)
password_entry.grid(column = 1, row = 2, sticky = tk.W, padx = 20, pady = 15)


login.mainloop()