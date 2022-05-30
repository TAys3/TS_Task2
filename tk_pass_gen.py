# A ton of errors will appear in the terminal if no boxes are ticked and you move the slider,
# but this is expected, and the app will still run, unaffected.

import tkinter as tk
from tkinter import CENTER, ttk
import string
import random
import os

root = tk.Tk()
root.title('Password Generator')

window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()                                  #these 5 lines put the window in the middle of the screen
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)                      
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')   
root.resizable(False, False)                                             #window will not be able to be resized

font = 'fira code'
LOWER_CASE = string.ascii_lowercase
UPPER_CASE = string.ascii_uppercase
DIGITS = string.digits
OTHER = string.punctuation

#functions
def update_label(event):                                #updates the label text and calls the function to make the password
    if round(pass_len.get()) == 1: 
        plural = ''
    else:
        plural = 's'
    slider_label.configure(text= f'''Password length: 
{round(pass_len.get())} character{plural}''')
    make_pass()

def make_pass():                                    #makes the password based upon slider and checkbox values
    pass_char = ""
    if letters_var.get() == '1': 
        pass_char += LOWER_CASE
    else:
        pass
    if cap_letters_var.get() == '1':
        pass_char += UPPER_CASE
    else:
        pass
    if numbers_var.get() == '1':
        pass_char += DIGITS
    else:
        pass
    if special_char_var.get() == '1':
        pass_char += OTHER
    else:
        pass
    
    Gen_Pass = ''
    for i in range(round(pass_len.get())):          #slider value is a float and has many decimals, round() rounds it down
        Gen_Pass += random.choice(pass_char)
    password_entry.delete(0, len(Password.get()))   #updates the entry box's text
    password_entry.insert(0, Gen_Pass)

def copy_pass():                                     #copies the password to the clipboard
    text = Password.get()
    command = 'echo | set /p nul=' + text.strip() + '| clip'    #I have no idea how this works, it just does
    os.system(command)


#widgets and associated variables
slider_label = ttk.Label(
    root, 
    text=f'''Password length: 
0 characters''',
    font=(f'{font}', 12)
)

pass_len = tk.DoubleVar()
pass_len_slider = ttk.Scale(
    root,
    from_= 0,
    to = 40,
    orient = 'horizontal',  # vertical
    command = update_label,
    variable = pass_len
)

letters_var = tk.StringVar()
letters = ttk.Checkbutton(
    root,
    text = 'a-z',
    command = make_pass,
    variable = letters_var,
)

cap_letters_var = tk.StringVar()
cap_letters = ttk.Checkbutton(
    root,
    text ='A-Z',
    command = make_pass,
    variable = cap_letters_var,
)

numbers_var = tk.StringVar()
numbers = ttk.Checkbutton(
    root,
    text = '0-9',
    command = make_pass,
    variable = numbers_var,
)

special_char_var = tk.StringVar()
special_char = ttk.Checkbutton(
    root,
    text = '0-9',
    command = make_pass,
    variable = special_char_var,
)

Password = tk.StringVar()
password_entry = ttk.Entry(
    root,
    justify = CENTER,
    textvariable = Password,
)

copy_img = tk.PhotoImage(file = './Resources/211649_clipboard_icon2.png')
copy_to_clip = ttk.Button(
    root,
    image = copy_img,
    text = "Copy to clipboard",
    compound = tk.LEFT,
    command = copy_pass
)

new_pass = tk.Button(
    root,
    text = 'Re-generate password',
    command = make_pass
)



#adding to window/layout
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

slider_label.grid(column=0, row=0, sticky= tk.W, padx = 20, pady= 10)
pass_len_slider.grid(column=0, row=2, sticky= tk.EW, padx = 20, pady= 10, columnspan= 2)
letters.grid(column=0, row=3, sticky= tk.W, padx = 20, pady= 10)
cap_letters.grid(column=1, row=3, sticky= tk.W, padx = 20, pady= 10)
numbers.grid(column=0, row=4, sticky= tk.W, padx = 20, pady= 10)
special_char.grid(column=1, row=4, sticky= tk.W, padx = 20, pady= 10)
password_entry.grid(column=0, row=5, sticky= tk.EW, padx = 20, pady= 10, columnspan= 2)
copy_to_clip.grid(column=0, row=6, sticky= tk.EW, padx = 20, pady= 10, columnspan= 2)
new_pass.grid(column=0, row=7, sticky= tk.EW, padx = 20, pady= 10, columnspan= 2)


root.mainloop()
