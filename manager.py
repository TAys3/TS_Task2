import tkinter as tk
from tkinter import CENTER, ttk
from tkinter.messagebox import showinfo
import os
import sqlite3
import pyperclip
import webbrowser


#can add the ability to have different users depending on their login
main = tk.Tk()
main.title('Password Manager')
window_width = 700
window_height = 500
screen_width = main.winfo_screenwidth()             #these 5 lines put the window in the middle of the screen
screen_height = main.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)                      
center_y = int(screen_height / 2 - window_height / 2)
main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')   
main.resizable(False, False)
font = 'fira code'
pass_visible = False

#functions
def window():                                       #runs the password generator
    os.system('tk_pass_gen.py')
    remake_tree()

def create_tree():                                  #creates the tree widget
    global pass_visible
    records = []
    conn = sqlite3.connect('password.db')
    cur = conn.cursor()
    
    if pass_visible == False:
        cur.execute("SELECT website, username FROM passwords")
    elif pass_visible == True:
        cur.execute("SELECT * FROM passwords")
    
    db_records = cur.fetchall()
    conn.close()
    
    for n in db_records:
        records.append(n)
    
    if pass_visible == False:
        for record in records:                          #update the values
            tree.insert('', tk.END, values=record)
        tree.grid(row=0, column=0, sticky='nsew', columnspan= 5)
    else:
        for record in records:                          #update the values
            pass_tree.insert('', tk.END, values=record)
        pass_tree.grid(row=0, column=0, sticky='nsew', columnspan= 5)

def item_selected(event):                           #updates the labels with selected info
    global pass_visible
    if pass_visible == False:
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            recorded = item['values']
            #show record on labels
        website_label.configure(text = f'Website : {is_too_long(recorded[0])}')         #errors pop up here whenever I hide or show passwords, but it doesn't affect anything?
        username_label.configure(text = f'Username: {is_too_long(recorded[1])}')        #
    else:                                                                               #
        for selected_item in pass_tree.selection():                                     #"UnboundLocalError: local variable 'recorded' referenced before assignment" ?????????
            item = pass_tree.item(selected_item)                                        #
            recorded = item['values']                                                   #
            #show record on labels                                                      #Only happens after two clicks of the hide/show button ???
        website_label.configure(text = f'Website : {is_too_long(recorded[0])}')         #
        username_label.configure(text = f'Username: {is_too_long(recorded[1])}')        #
        password_label.configure(text = f'Password: {is_too_long(recorded[2])}')        #I'm so confused by it, but it doesn't change anything. Will I lose marks?

def is_too_long(text):                              #makes sure the copy button and other widgets aren't pushed around
    if len(text) <= 20:
        return text
    elif len(text) > 20:
        new = f'{text[:21]}...'
        return new

def remake_tree():                                  #remakes the tree to update it
    global pass_visible
    if pass_visible == False:
        for record in tree.get_children():
            tree.delete(record)
    else:
        for record in pass_tree.get_children():
            pass_tree.delete(record)
    create_tree()

def new_data():                                     #runs the credentials 'adder'
    os.system('database.py')
    remake_tree()

def open_website():                                 #opens the website (need to find a better way)
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        recorded = item['values']
    webbrowser.open(f'{recorded[0]}', new = 2, autoraise = True)

def copy_user():                                    #copies the username to the clipboard
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        recorded = item['values']
    pyperclip.copy(recorded[1])

def copy_pass():                                    #copies the password to the clipboard
    os.system('pin_auth.py')
    with open('pinworkornot.txt', 'r') as f:        #error if you don't get the pin correct as the directory is not created, but it still works
        lines = f.readlines()
    
    if lines[0] == 'True':
        os.remove('pinworkornot.txt')
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            recorded = item['values']

        conn = sqlite3.connect('password.db')
        cur = conn.cursor()
        website = f"%{recorded[0]}%"
        username = recorded[1]
        cur.execute(f"SELECT rowid, website, username FROM passwords WHERE website LIKE '{website}'")
        values = cur.fetchall()

        found = False
        for i in values:
            if i[2] == username and found == False:
                id = int(i[0])
                found = True
            else:
                pass    
        
        if found == True:
            cur.execute(f"SELECT password FROM passwords WHERE rowid = '{id}'")
            pass_to_copy = cur.fetchall()
            pyperclip.copy(pass_to_copy[0][0])
        else:
            pass

def remove_data():                                  #delets a record from the database (probably very jank)
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        recorded = item['values']

    conn = sqlite3.connect('password.db')
    cur = conn.cursor()
    website = f"%{recorded[0]}%"
    username = recorded[1]
    cur.execute(f"SELECT rowid, website, username FROM passwords WHERE website LIKE '{website}'")
    values = cur.fetchall()

    found = False
    for i in values:
        if i[2] == username and found == False:
            id = int(i[0])
            found = True
        else:
            pass
    
    if found == True:
        cur.execute(f"DELETE FROM passwords WHERE rowid = {id}")
    conn.commit()
    conn.close()
    remake_tree()

def hide_show():
    global pass_visible
    if pass_visible == False:
        os.system('pin_auth.py')
        with open('pinworkornot.txt', 'r') as f:
            lines = f.readlines()

        if lines[0] == 'True':
            os.remove('pinworkornot.txt')
            pass_visible = True
            tree.grid_forget()
            password_label.grid(column=0, row=3, sticky= tk.W, padx = 20, pady= 10, columnspan = 3)
        else:
            pass

    else:
        pass_visible = False
        pass_tree.grid_forget()
        password_label.grid_forget()
    remake_tree()


#widgets
columns = ('website', 'username')
tree = ttk.Treeview(main, columns = columns, show = 'headings')
tree.heading('website', text='Website')
tree.heading('username', text='Username')

tree.bind('<<TreeviewSelect>>', item_selected)

scrollbar = ttk.Scrollbar(main, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)


columns_2 = ('website', 'username', 'password')
pass_tree = ttk.Treeview(main, columns = columns_2, show = 'headings')
pass_tree.heading('website', text='Website')
pass_tree.heading('username', text='Username')
pass_tree.heading('password', text='Password')

pass_tree.bind('<<TreeviewSelect>>', item_selected)

scrollbar2 = ttk.Scrollbar(main, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)


create_tree()


website_label = ttk.Label(
    main, 
    text= 'Website: ',
    font=(f'{font}', 12),

)

username_label = ttk.Label(
    main, 
    text= 'Username:',
    font=(f'{font}', 12)
)

password_label = ttk.Label(
    main, 
    text= 'Password:',
    font=(f'{font}', 12),
)

button = ttk.Button(
    main,
    text = 'Password Generator',
    command = window
)

new_data_button = ttk.Button(
    main,
    text = 'New credentials',
    command = new_data
)

copy_img = tk.PhotoImage(file = './Resources/small_clipboard_icon2.png')
open_website_button = ttk.Button(
    main,
    text = "Go to",
    command = open_website
)

copy_username = ttk.Button(
    main,
    image = copy_img,
    text = "Copy",
    compound = tk.LEFT,
    command = copy_user
)

copy_password = ttk.Button(
    main,
    image = copy_img,
    text = "Copy password",
    compound = tk.LEFT,
    command = copy_pass
)

delete_button = ttk.Button(
    main,
    text = "Delete record",
    compound = tk.LEFT,
    command = remove_data
)

hide_or_show = ttk.Button(
    main,
    text = "Hide/Show passwords",
    compound = tk.LEFT,
    command = hide_show
)

#layout
scrollbar.grid(row=0, column=6, sticky='ns')

website_label.grid(column=0, row=1, sticky= tk.W, padx = 20, pady= 10, columnspan = 3)
username_label.grid(column=0, row=2, sticky= tk.W, padx = 20, pady= 10, columnspan = 3)
# password_label.grid(column=0, row=3, sticky= tk.W, padx = 20, pady= 10)
open_website_button.grid(column=4, row=1, sticky= tk.E, padx = 20, pady= 10)
copy_username.grid(column=4, row=2, sticky= tk.E, padx = 20, pady= 10)
copy_password.grid(column=4, row=3, sticky= tk.E, padx = 20, pady= 10)

button.grid(column=0, row=4, sticky= tk.W, padx = 20, pady= 10)
new_data_button.grid(column=0, row=6, sticky= tk.W, padx = 20, pady= 10)
delete_button.grid(column=0, row=7, sticky= tk.W, padx = 20, pady= 10)
hide_or_show.grid(column=1, row=7, sticky= tk.W, padx = 20, pady= 10)

#don't know why I made it like this, I just did
os.system('login.py')
with open('f6a214f7a5fcda0c2cee9660b7fc29f5649e3c68aad48e20e950137c98913a68.txt', 'r') as f:
    lines = f.readlines()

#but it does work
if lines[0] == '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18':
    os.remove('f6a214f7a5fcda0c2cee9660b7fc29f5649e3c68aad48e20e950137c98913a68.txt')
    main.mainloop()