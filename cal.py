from tkinter import *

# Create the main window
root = Tk()
root.title("Responsive Calculator")

# Create a entry field for displaying calculations
entry_field = Entry(root, width=35, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=4)

# Define functions for calculations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error"
    else:
        return x / y

def equal():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, END)
        entry_field.insert(0, str(result))
    except:
        entry_field.delete(0, END)
        entry_field.insert(0, "Error")

def clear():
    entry_field.delete(0, END)

# Create number buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: entry_field.insert(END, "1"))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: entry_field.insert(END, "2"))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: entry_field.insert(END, "3"))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: entry_field.insert(END, "4"))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: entry_field.insert(END, "5"))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: entry_field.insert(END, "6"))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: entry_field.insert(END, "7"))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: entry_field.insert(END, "8"))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: entry_field.insert(END, "9"))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: entry_field.insert(END, "0"))

# Create operator buttons
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: entry_field.insert(END, "+"))
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: entry_field.insert(END, "-"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: entry_field.insert(END, "*"))
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: entry_field.insert(END, "/"))
button_equal = Button(root, text="=", padx=91, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=clear)

# Place buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=4)

# Start the main loop
root.mainloop()


