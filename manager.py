from time import sleep
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno
import os
import sqlite3
import pyperclip
import webbrowser
import string
import random


#can add the ability to have different users depending on their login
main = tk.Tk()
main.title('Password Manager')
window_width = 855
window_height = 430
screen_width = main.winfo_screenwidth()             #these 5 lines put the window in the middle of the screen
screen_height = main.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)                      
center_y = int(screen_height / 2 - window_height / 2)
main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')   
main.resizable(False, False)
main.iconbitmap('./Resources/lock_img.ico')
font = 'fira code'
pass_visible = False
bin_frame = 'closed'
eye_frame = 'closed'

#functions
def pass_gen():                                     #runs the password generator
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
        tree.grid(row=0, column=1, sticky='nsew', columnspan= 6, rowspan= 4, ipadx = 100)
        scrollbar.grid(row=0, column=7, sticky='ns', rowspan= 4)

    else:
        for record in records:                          #update the values
            pass_tree.insert('', tk.END, values=record)
        pass_tree.grid(row=0, column=1, sticky='nsew', columnspan= 6, rowspan= 4)
        scrollbar2.grid(row=0, column=7, sticky='ns', rowspan= 4)

def item_selected(event):                           #updates the labels with selected info
    global pass_visible
    if pass_visible == False:
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            recorded = item['values']
            #show record on labels
        website_label.configure(text = f'Website : {is_too_long(recorded[0])}')         #errors pop up here for a few things, but it doesn't affect anything?
        username_label.configure(text = f'Username: {is_too_long(recorded[1])}')        #
    else:                                                                               #
        for selected_item in pass_tree.selection():                                     #"UnboundLocalError: local variable 'recorded' referenced before assignment" ?????????
            item = pass_tree.item(selected_item)                                        #
            recorded = item['values']                                                   #
            #show record on labels                                                      #Only happens after two clicks of the hide/show button ???
        website_label.configure(text = f'Website : {is_too_long(recorded[0])}')         #
        username_label.configure(text = f'Username: {is_too_long(recorded[1])}')        #
        password_label.configure(text = f'Password: {is_too_long(recorded[2])}')        #I think it's due to records moving around and stuff, and the selection going wonky, but idk. Hopefully won't lose marks

def is_too_long(text):                              #makes sure the copy button and other widgets aren't pushed around
    if len(str(text)) <= 20:
        return str(text)
    elif len(str(text)) > 20:
        new = f'{str(text)[:21]}...'
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
    global pass_visible
    if pass_visible == False:
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            recorded = item['values']
    elif pass_visible == True:
        for selected_item in pass_tree.selection():
            item = pass_tree.item(selected_item)
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

def remove_data():                                  #deletes a record from the database (probably very jank)
    global pass_visible
    answer = askyesno(title = 'Are you sure?', message = 'Are you sure you want to delete?')
    if answer == True:
        if pass_visible == False:
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                recorded = item['values']
        elif pass_visible == True:
            for selected_item in pass_tree.selection():
                item = pass_tree.item(selected_item)
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

def hide_show():                                    #hides and shows the passwords column, which has the passwords in plain text (probably could have just remade the tree with *'s instead of the password in plain text)
    global pass_visible
    global eye_frame
    if pass_visible == False:
        os.system('pin_auth.py')
        with open('pinworkornot.txt', 'r') as f:
            lines = f.readlines()

        if lines[0] == 'True':
            os.remove('pinworkornot.txt')
            pass_visible = True
            tree.grid_forget()
            scrollbar.grid_forget()
            password_label.grid(column=1, row=6, sticky= tk.W, padx = 20, pady= 10, columnspan = 3)
            show_pass.grid_forget()
            hide_pass.grid(column=1, row=7, sticky= tk.W, padx = 20, pady= 10)
            eye_frame = 'closed'
        else:
            pass

    else:
        pass_visible = False
        pass_tree.grid_forget()
        password_label.grid_forget()
        scrollbar2.grid_forget()
        hide_pass.grid_forget()
        show_pass.grid(column=1, row=7, sticky= tk.W, padx = 20, pady= 10)
        eye_frame = 'closed'
    remake_tree()

def change_bin(event):                              #changes the bin button image. Very, VERY jank cause of garbage collection I think
    global bin_frame
    if bin_frame == 'closed':
        delete_button1.grid_forget()
        delete_button2.grid(column=0, row=2, sticky= tk.W, padx = 20, pady= 10, ipadx= 40)
        bin_frame = 'open'
    elif bin_frame == 'open':
        delete_button2.grid_forget()
        delete_button1.grid(column=0, row=2, sticky= tk.W, padx = 20, pady= 10, ipadx= 40)
        bin_frame = 'closed'

def change_eye(event):                              #changes the show/hide password button image. Very, VERY jank cause of garbage collection I think
    global eye_frame
    global pass_visible
    if pass_visible == False:
        if eye_frame == 'closed':
            show_pass1.grid_forget()
            show_pass.grid(column=0, row=3, sticky= tk.W, padx = 20, pady= 10, ipadx= 26)
            eye_frame = 'open'
        elif eye_frame == 'open':
            show_pass.grid_forget()
            show_pass1.grid(column=0, row=3, sticky= tk.W, padx = 20, pady= 10, ipadx= 26)
            eye_frame = 'closed'
    elif pass_visible == True:
        if eye_frame == 'open':
            hide_pass1.grid_forget()
            hide_pass.grid(column=0, row=3, sticky= tk.W, padx = 20, pady= 10, ipadx= 28)
            eye_frame = 'closed'
        elif eye_frame == 'closed':
            hide_pass.grid_forget()
            hide_pass1.grid(column=0, row=3, sticky= tk.W, padx = 20, pady= 10, ipadx= 28)
            eye_frame = 'open'

def pass_thing(event):                              #idk if this is cool or not. Wanted to do something similar to my password button. Changes the text before password generator
    characters = f"{string.ascii_letters}{string.punctuation}{string.digits}"
    for i in range(4):
        img_thing = ''
        for n in range(6):
            img_thing += random.choice(characters)
        pass_gen_button['text'] = f'{img_thing} Password Generator'
        pass_gen_button.update()
        sleep(0.05)


#widgets
columns = ('website', 'username')
tree = ttk.Treeview(main, columns = columns, show = 'headings', selectmode = 'browse')
tree.heading('website', text='Website')
tree.heading('username', text='Username')

tree.bind('<<TreeviewSelect>>', item_selected)

scrollbar = ttk.Scrollbar(main, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)


columns_2 = ('website', 'username', 'password')
pass_tree = ttk.Treeview(main, columns = columns_2, show = 'headings', selectmode = 'browse')
pass_tree.heading('website', text='Website')
pass_tree.heading('username', text='Username')
pass_tree.heading('password', text='Password')

pass_tree.bind('<<TreeviewSelect>>', item_selected)

scrollbar2 = ttk.Scrollbar(main, orient=tk.VERTICAL, command=pass_tree.yview)
pass_tree.configure(yscroll=scrollbar2.set)


create_tree()   #this makes code shorter


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

pass_gen_button = ttk.Button(
    main,
    text = '{^*!#@? Password Generator',
    command = pass_gen
)

plus_img = tk.PhotoImage(file = './Resources/plus2.png')
new_data_button = ttk.Button(
    main,
    image = plus_img,
    compound = tk.LEFT,
    text = 'New credentials',
    command = new_data
)

web_img = tk.PhotoImage(file = './Resources/net.png')
open_website_button = ttk.Button(
    main,
    image = web_img,
    compound = tk.LEFT,
    text = "Go to",
    command = open_website
)

copy_img = tk.PhotoImage(file = './Resources/small_clipboard_icon2.png')
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

delete_img_closed = tk.PhotoImage(file = './Resources/closed_bin2.png')
delete_button1 = ttk.Button(
    main,
    image = delete_img_closed, 
    text = "Delete record",
    compound = tk.LEFT,
    command = remove_data
)

delete_img_open = tk.PhotoImage(file = './Resources/open_bin2.png')
delete_button2 = ttk.Button(
    main,
    image = delete_img_open, 
    text = "Delete record",
    compound = tk.LEFT,
    command = remove_data
)

eye_closed_img = tk.PhotoImage(file = './Resources/show2.png')
show_pass = ttk.Button(
    main,
    image = eye_closed_img,
    text = "Show passwords",
    compound = tk.LEFT,
    command = hide_show
)

eye_open_img = tk.PhotoImage(file = './Resources/hide2.png')
hide_pass = ttk.Button(
    main,
    image = eye_open_img,
    text = "Hide passwords",
    compound = tk.LEFT,
    command = hide_show
)

show_pass1 = ttk.Button(
    main,
    image = eye_open_img,
    text = "Show passwords",
    compound = tk.LEFT,
    command = hide_show
)

hide_pass1 = ttk.Button(
    main,
    image = eye_closed_img,
    text = "Hide passwords",
    compound = tk.LEFT,
    command = hide_show
)


#layout
scrollbar.grid(row=0, column=7, sticky='ns', rowspan=4)

website_label.grid(column=1, row=4, sticky= tk.W, padx = 20, pady= 10, columnspan = 3)
username_label.grid(column=1, row=5, sticky= tk.W, padx = 20, pady= 10, columnspan = 3)
open_website_button.grid(column=6, row=4, sticky= tk.E, padx = 20, pady= 10)
copy_username.grid(column=6, row=5, sticky= tk.E, padx = 20, pady= 10)
copy_password.grid(column=6, row=6, sticky= tk.E, padx = 20, pady= 10)

pass_gen_button.grid(column=0, row=0, sticky= tk.NW, padx = 20, pady= 10, ipadx= 10, ipady= 10)
new_data_button.grid(column=0, row=1, sticky= tk.W, padx = 20, pady= 10)
delete_button1.grid(column=0, row=2, sticky= tk.W, padx = 20, pady= 10, ipadx= 40)
show_pass1.grid(column=0, row=3, sticky= tk.W, padx = 20, pady= 10, ipadx= 26)


#event binding
delete_button1.bind('<Enter>', change_bin)
delete_button2.bind('<Leave>', change_bin)

show_pass.bind('<Leave>', change_eye)
show_pass1.bind('<Enter>', change_eye)

hide_pass.bind('<Leave>', change_eye)
hide_pass1.bind('<Enter>', change_eye)

pass_gen_button.bind('<Enter>', pass_thing)


#don't know why I made it like this, I just did
os.system('login.py')
with open('f6a214f7a5fcda0c2cee9660b7fc29f5649e3c68aad48e20e950137c98913a68.txt', 'r') as f:
    lines = f.readlines()

#but it does work
if lines[0] == '3cbc87c7681f34db4617feaa2c8801931bc5e42d8d0f560e756dd4cd92885f18':
    os.remove('f6a214f7a5fcda0c2cee9660b7fc29f5649e3c68aad48e20e950137c98913a68.txt')
    main.mainloop()