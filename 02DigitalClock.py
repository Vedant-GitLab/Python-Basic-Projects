import tkinter as tk #tkinter ek module hai GUI banane ke liye
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime("%H:%M:%S %p \n %d:%m:%y")
    label.config(text=string)
    label.after(1000, time) #update after every 1 second

label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

time()

root.mainloop()
