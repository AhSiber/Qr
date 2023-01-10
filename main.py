import tkinter as tk
import qrcode
from random import randrange

root=tk.Tk()

# setting the windows size
root.geometry("300x300")

# declaring string variable
# for storing name and password

name_var=tk.StringVar()

# defining a function that will
# get the name and password and
# print them on the screen
def submit():
   genert = str(randrange(1,100))
   img = qrcode.make(name_var.get()).save(f"{genert}.png")
   root.destroy()

name_label = tk.Label(root, text = 'Paste the copied text here:', font=('calibre',10, 'bold')).pack(padx=0,pady=3)
# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal')).pack(padx=10,pady=20)

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit).pack(padx=10,pady=15)
root.mainloop()
