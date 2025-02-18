import tkinter as tk


# Function to update the expression in the text entry field
def click_button(value):
    entry_field.insert(tk.END, value)  # Insert value into the entry field


# Function to clear the entry field
def clear():
    entry_field.delete(0, tk.END)  # Delete everything from entry field


# Function to evaluate the expression and display the result
def calculate():
    try:
        expression = entry_field.get()
        result = eval(expression)  # Evaluate the mathematical expression
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")


# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.configure(bg="lightgray")

# Entry field for displaying input and result
entry_field = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.GROOVE, justify="right")
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', 'C', '=', '+')
]

# Creating buttons dynamically
for row_index, row in enumerate(buttons):
    for col_index, symbol in enumerate(row):
        if symbol == "=":
            btn = tk.Button(root, text=symbol, font=("Arial", 16), bg="lightgreen", fg="black",
                            height=2, width=5, command=calculate)
        elif symbol == "C":
            btn = tk.Button(root, text=symbol, font=("Arial", 16), bg="red", fg="white",
                            height=2, width=5, command=clear)
        else:
            btn = tk.Button(root, text=symbol, font=("Arial", 16), bg="white", fg="black",
                            height=2, width=5, command=lambda s=symbol: click_button(s))

        btn.grid(row=row_index + 1, column=col_index, padx=5, pady=5)

# Run the application
root.mainloop()
