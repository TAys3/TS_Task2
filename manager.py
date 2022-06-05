import tkinter as tk
from tkinter import CENTER, ttk
from tkinter.messagebox import showinfo
import os
import sqlite3


#can add the ability to have different users depending on their login
main = tk.Tk()
main.title('Password Generator')
window_width = 700
window_height = 500
screen_width = main.winfo_screenwidth()                                  #these 5 lines put the window in the middle of the screen
screen_height = main.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)                      
center_y = int(screen_height / 2 - window_height / 2)
main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')   
main.resizable(False, False)
font = 'fira code'

#functions
def window():
    os.system('tk_pass_gen.py')

def create_tree():
    records = []
    conn = sqlite3.connect('password.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords")
    db_records = cur.fetchall()
    conn.close()
    for n in db_records:                     #need to change it to use password db
        records.append(n)
    
    for record in records:                    #update the values (need to change a bit)
        tree.insert('', tk.END, values=record)

def item_selected(event):                   #change to update a label/s with the info
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        recorded = item['values']
        # show a message
        website_label.configure(text = f'Website: {recorded[0]}')
        username_label.configure(text = f'Username: {recorded[1]}')
        password_label.configure(text = f'Password: {recorded[2]}')



#widgets
columns = ('website', 'username', 'password')
tree = ttk.Treeview(main, columns = columns, show = 'headings')
tree.heading('website', text='Website')
tree.heading('username', text='Username')
tree.heading('password', text='Password')

tree.bind('<<TreeviewSelect>>', item_selected)

scrollbar = ttk.Scrollbar(main, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)

create_tree()

website_label = ttk.Label(
    main, 
    text= 'Website:',
    font=(f'{font}', 12)
)

username_label = ttk.Label(
    main, 
    text= 'Username:',
    font=(f'{font}', 12)
)

password_label = ttk.Label(
    main, 
    text= 'Password:',
    font=(f'{font}', 12)
)

button = ttk.Button(
    main,
    text = 'Password Generator',
    command = window
)



#layout
tree.grid(row=0, column=0, sticky='nsew')
scrollbar.grid(row=0, column=1, sticky='ns')

website_label.grid(column=0, row=1, sticky= tk.W, padx = 20, pady= 10)
username_label.grid(column=0, row=2, sticky= tk.W, padx = 20, pady= 10)
password_label.grid(column=0, row=3, sticky= tk.W, padx = 20, pady= 10)
button.grid(column=0, row=4, sticky= tk.W, padx = 20, pady= 10)


main.mainloop()