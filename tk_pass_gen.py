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







slider_label = ttk.Label(
    root, 
text=f'''Password length: 
{pass_len} characters''',
font=(f'{font}', 12))

slider_label.pack()

root.mainloop()
