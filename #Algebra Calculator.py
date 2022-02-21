#Algebra Calculator
import tkinter as tk
import cmath

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 60, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 100, window=entry2)

entry3 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry3)


def solvequadratic ():
    a = int(entry1.get())
    b = int(entry2.get())
    c = int(entry3.get())

    label1 = tk.Label(root, text= ((-b-cmath.sqrt((b**2)-(4*a*c))/(2*a))))
    canvas1.create_window(200, 230, window=label1)
    label1 = tk.Label(root, text = ((-b+cmath.sqrt((b**2)-(4*a*c))/(2*a))))
    canvas1.create_window(200, 260, window=label1)
    
button1 = tk.Button(text='Solve Quadratic', command=solvequadratic)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
