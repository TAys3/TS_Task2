import tkinter as tk
from tkinter import ttk
import string
import random

root = tk.Tk()
root.title('Password Generator')

window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

pass_len = 0
font = 'fira code'
LOWER_CASE = string.ascii_lowercase
UPPER_CASE = string.ascii_uppercase
DIGITS = string.digits
OTHER = string.punctuation

def make_pass():   #generates a password based upon user's input
    if pass_len_slider.get() == 1:    #This changes the label's text to the value of the slider
        plural = ''
    else:
        plural = 's'
    slider_label['text'] = f'''Password length: 
{round(pass_len_slider.get())} character{plural}'''

    pass_char = ""
    if letters_var.get() == 1:     #These are to check if a box is ticked, and then add the characters if so
        pass_char += LOWER_CASE
    else:
        pass
    if cap_letters_var.get() == 1:
        pass_char += UPPER_CASE
    else:
        pass
    if numbers_var.get() == 1:
        pass_char += DIGITS
    else:
        pass
    if special_char_var.get() == 1:
        pass_char += OTHER
    else:
        pass
    
    Gen_Pass = ''
    for i in range(int(round(pass_len_slider.get()))):  #This creates the password
        Gen_Pass += random.choice(pass_char)
    Password = Gen_Pass

    





slider_label = ttk.Label(
    root, 
    text=f'''Password length: 
{pass_len} characters''',
    font=(f'{font}', 12)
)

pass_len_slider = ttk.Scale(
    root,
    from_= 0,
    to = 40,
    orient = 'horizontal',  # vertical
    command = make_pass
)

letters_var = tk.StringVar()
letters = ttk.Checkbutton(root,
    text = 'a-z',
    command = make_pass,
    variable = letters_var,
)

cap_letters_var = tk.StringVar()
cap_letters = ttk.Checkbutton(root,
    text ='A-Z',
    command = make_pass,
    variable = cap_letters_var,
)

numbers_var = tk.StringVar()
numbers = ttk.Checkbutton(root,
    text = '0-9',
    command = make_pass,
    variable = numbers_var,
)

special_char_var = tk.StringVar()
special_char = ttk.Checkbutton(root,
    text = '0-9',
    command = make_pass,
    variable = special_char_var,
)

Password = tk.StringVar()
password_entry = ttk.Entry(
    root,
    textvariable = Password,
)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
slider_label.grid(column=0, row=0, sticky= tk.W, padx = 20, pady= 10)
pass_len_slider.grid(column=0, row=2, sticky= tk.EW, padx = 20, pady= 10, columnspan= 2)
letters.grid(column=0, row=4, sticky= tk.W, padx = 20, pady= 10, columnspan= 2)
cap_letters.grid(column=1, row=4, sticky= tk.W, padx = 20, pady= 10, columnspan= 2)


root.mainloop()
