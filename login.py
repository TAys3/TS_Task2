import hashlib
import tkinter as tk
from tkinter import CENTER, ttk
import sqlite3
from tkinter.messagebox import showerror

logged_in = False
#can add the ability to have different users depending on their login
login = tk.Tk()
login.title('Log in')
window_width = 300
window_height = 225
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
    password_hash = hashlib.sha256((password.get()).encode('utf-8')).hexdigest()
    
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    current_users = cur.fetchall()
    conn.close()
    user_list = []
    for i in current_users:
        user_list.append(i[0])
    
    exists = False
    count = 0
    while count < len(user_list) and exists == False:
        if username.get() == user_list[count]:
            exists = True
            place = count
        else:
            pass
        count += 1
    
    global logged_in
    if exists == False:
        showerror(title = "Error!", message = "Username or password incorrect!")
    else:
        if current_users[place][1] == password_hash:
            logged_in = True
            logged = hashlib.sha256((str(logged_in)).encode('utf-8')).hexdigest()
            with open('f6a214f7a5fcda0c2cee9660b7fc29f5649e3c68aad48e20e950137c98913a68.txt', 'w') as f:
                f.write(f'{logged}')
            login.destroy()
        else:
            showerror(title = "Error!", message = "Username or password incorrect!")


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
    textvariable = username
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
    show = '*'
)

login_button = ttk.Button(
    login,
    text = 'Log in',
    command = log_in
)


header_label.grid(column = 0, row = 0, sticky = tk.EW, padx = 20, pady = 15, columnspan = 2)
username_label.grid(column = 0, row = 1, sticky = tk.W, padx = 20, pady = 15)
username_entry.grid(column = 1, row = 1, sticky = tk.W, padx = 20, pady = 15)
password_label.grid(column = 0, row = 2, sticky = tk.W, padx = 20, pady = 15)
password_entry.grid(column = 1, row = 2, sticky = tk.W, padx = 20, pady = 15)
login_button.grid(column = 1, row = 3, sticky = tk.NE, padx = 20, pady = 5)

login.mainloop()
