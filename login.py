import hashlib
import tkinter as tk
from tkinter import ttk

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



login.mainloop()