import tkinter as tk
from datetime import datetime
def calculate_age():
    try:
        birth_year = int(year_entry.get())
        current_year = datetime.now().year
        age = current_year - birth_year
        result_label.config(text=f"Your age is: {age}")
    except ValueError:
        result_label.config(text="Please enter a valid year")
root = tk.Tk()
root.title("Age Calculator")
tk.Label(root, text="Enter your birth year:").pack()
year_entry = tk.Entry(root)
year_entry.pack()
tk.Button(root, text="Calculate Age", command=calculate_age).pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()