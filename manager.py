import tkinter as tk
from tkinter import CENTER, ttk
from tkinter.messagebox import showinfo
import os
# from tk_pass_gen import root #very interesting


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



def window():
    os.system('tk_pass_gen.py')

button = ttk.Button(
    main,
    text = 'Open',
    command = window
)

button.grid(column=0, row=0, sticky= tk.W, padx = 20, pady= 10)

columns = ('website', 'username', 'password')
tree = ttk.Treeview(main, columns = columns, show = 'headings')
tree.heading('website', text='Website')
tree.heading('username', text='Username')
tree.heading('password', text='Password')




main.mainloop()