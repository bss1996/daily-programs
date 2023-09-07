import tkinter as tk

f_num = None
math_op = None
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def clear():
    display.delete(0, tk.END)

def add():
    first_number = display.get()
    global f_num
    global math_op
    math_op = "addition"
    f_num = float(first_number)
    display.delete(0, tk.END)

def subtract():
    first_number = display.get()
    global f_num
    global math_op
    math_op = "subtraction"
    f_num = float(first_number)
    display.delete(0, tk.END)

def multiply():
    first_number = display.get()
    global f_num
    global math_op
    math_op = "multiplication"
    f_num = float(first_number)
    display.delete(0, tk.END)

def divide():
    first_number = display.get()
    global f_num
    global math_op
    math_op = "division"
    f_num = float(first_number)
    display.delete(0, tk.END)

def calculate():
    second_number = display.get()
    display.delete(0, tk.END)

    if math_op == "addition":
        result = f_num + float(second_number)
    elif math_op == "subtraction":
        result = f_num - float(second_number)
    elif math_op == "multiplication":
        result = f_num * float(second_number)
    elif math_op == "division":
        if float(second_number) != 0:
            result = f_num / float(second_number)
        else:
            result = "Error: Division by zero"

    display.insert(0, result if 'result' in locals() else "")
    f_num = result if 'result' in locals() else None
    
# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create and configure the display
display = tk.Entry(window, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4)

# Create buttons for digits
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20,
              command=lambda b=button: button_click(b) if b != "=" else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create clear button
tk.Button(window, text="C", padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)

window.mainloop()
