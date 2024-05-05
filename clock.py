import tkinter as tk
from time import strftime


def time():
    # Get the current time format
    string = strftime('%H:%M:%S %p')

    label.config(text=string)

    label.after(1000, time)


def change_color():

    current_color = label.cget('foreground')
    # Toggle between cyan and white colors
    new_color = 'cyan' if current_color == 'white' else 'white'

    label.config(foreground=new_color)

    label.after(1000, change_color)


root = tk.Tk()
root.title('Digital Clock')


label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

#updating the clock time and color
time()
change_color()


root.mainloop()


