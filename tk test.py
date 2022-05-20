import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window Demo')

message = tk.Label(root, text="Hello, World!")
message.pack()

root.mainloop()