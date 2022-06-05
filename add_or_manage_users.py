import hashlib
import sqlite3
import tkinter as tk
from tkinter import CENTER, ttk
from tkinter.messagebox import showerror

# conn = sqlite3.connect('users.db')
# cur = conn.cursor()
# cur.execute("""CREATE TABLE user (
#     username text,
#     password text
#     )""")
# usre = 'Taylor'
# passw = 'Password'
# passwhased = hashlib.sha256((passw).encode('utf-8')).hexdigest()
# cur.execute("INSERT INTO user VALUES (?,?)", (usre, passwhased))
# conn.commit()
# conn.close()

add_user = tk.Tk()
add_user.title('Add users')
window_width = 300
window_height = 250
screen_width = add_user.winfo_screenwidth()                                  #these 5 lines put the window in the middle of the screen
screen_height = add_user.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)                      
center_y = int(screen_height / 2 - window_height / 2)
add_user.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')   
add_user.resizable(False, False)
font = 'fira code'





#functions
def new_user():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    current_users = cur.fetchall()
    conn.close()
    user_list = []
    for i in current_users:
        user_list.append(i[0])

    exists = False
    counter = 0
    while counter < len(user_list) and exists == False:
        if username.get() == user_list[counter]:
            exists = True
        else:
            pass
        counter += 1
    
    if exists == True:
        showerror(title = "Error!", message = "User already exists!")
    else:
        #why does it crash
        from surely_this_works import commit
        new_username = username.get()
        new_password = hashlib.sha256((password.get()).encode('utf-8')).hexdigest()
        commit(new_username, new_password)
        exit()



#widgets
header_label = ttk.Label(
    add_user, 
    text= 'Add user:',
    font=(f'{font}', 15)
)

username = tk.StringVar()
username_label = ttk.Label(
    add_user, 
    text= 'Username:',
    font=(f'{font}', 12)
)
username_entry = ttk.Entry(
    add_user,
    justify = CENTER,
    textvariable = username,
)

password = tk.StringVar()
password_label = ttk.Label(
    add_user, 
    text= 'Password:',
    font=(f'{font}', 12)
)
password_entry = ttk.Entry(
    add_user,
    justify = CENTER,
    textvariable = password,
)

save_button = ttk.Button(
    add_user,
    text = 'Save',
    command = new_user
)


header_label.grid(column = 0, row = 0, sticky = tk.EW, padx = 20, pady = 15, columnspan = 2)
username_label.grid(column = 0, row = 1, sticky = tk.W, padx = 20, pady = 15)
username_entry.grid(column = 1, row = 1, sticky = tk.W, padx = 20, pady = 15)
password_label.grid(column = 0, row = 2, sticky = tk.W, padx = 20, pady = 15)
password_entry.grid(column = 1, row = 2, sticky = tk.W, padx = 20, pady = 15)
save_button.grid(column = 1, row = 3, sticky = tk.E, padx = 20, pady = 15)

add_user.mainloop()