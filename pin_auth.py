import tkinter as tk
from tkinter import ttk, CENTER
import sqlite3
import hashlib
from tkinter.messagebox import showerror
font = 'fira code'


auth_change = tk.Tk()
auth_change.title('Authenticate')
window_width = 275
window_height = 125
screen_width = auth_change.winfo_screenwidth()             #these 5 lines put the window in the middle of the screen
screen_height = auth_change.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)                      
center_y = int(screen_height / 2 - window_height / 2)
auth_change.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')   
auth_change.resizable(False, False)

def check_pin():
    pin_hash = hashlib.sha256((pin_entry.get()).encode('utf-8')).hexdigest()

    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_pin")
    pins = cur.fetchall()
    
    pin_good = False
    for i in pins:
        if i[1] == pin_hash:
            pin_good = True
        else:
            pass

    if pin_good == True:
        with open('pinworkornot.txt', 'w') as f:
            f.write('True')
        auth_change.destroy()
    else:
        showerror(title = "Error!", message = "Pin incorrect!")
    conn.commit()
    conn.close()



pin_lbl = ttk.Label(
auth_change, 
text= 'Enter PIN: ',
font=(f'{font}', 12),
)
pin_lbl.grid(column=1, row=0, sticky= tk.EW, padx = 20, pady= 10)

Pin = tk.StringVar()
pin_entry = website_entry = ttk.Entry(
auth_change,
justify = CENTER,
textvariable = Pin,
)
pin_entry.grid(column = 0, row=1, sticky= tk.EW, padx = 20, pady= 10, columnspan= 2)

ok_button = ttk.Button(
auth_change,
text = "OK",
compound = tk.LEFT,
command = check_pin
)
ok_button.grid(column=2, row=1, sticky= tk.W, padx = 20, pady= 10)



auth_change.mainloop()