import tkinter as tk
from tkinter import ttk

def clean_input(input_str):
    # Remove non-numeric and non-plus characters, and keep the '=' for validation
    cleaned = ''.join(filter(lambda x: x.isdigit() or x in ['+', '='], input_str))
    return cleaned

def validate_sum(expression):
    if '=' not in expression:
        return False
    try:
        left, right = expression.split('=')
        return eval(left) == eval(right)
    except:
        return False

def process_input():
    raw_input = input_entry.get()
    cleaned_expression = clean_input(raw_input)
    # Insert into the tree view
    tree.insert('', 'end', values=(raw_input, cleaned_expression))

# Create the main window
root = tk.Tk()
root.title("Turing Machine Sum Validator")

# Input field
input_label = tk.Label(root, text="Enter expression:")
input_label.pack(pady=5)

input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)

# Process button
process_button = tk.Button(root, text="Process", command=process_input)
process_button.pack(pady=5)

# Result table
columns = ('Input Expression', 'Cleaned Expression')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('Input Expression', text='Input Expression')
tree.heading('Cleaned Expression', text='Cleaned Expression')
tree.pack(pady=20)

# Run the application
root.mainloop()
