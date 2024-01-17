import tkinter as tk

def on_click(button_text) -> None:
    current_text = entry.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x305")

# Entry widget to display the input and output
entry = tk.Entry(root, width=16, font=("Fira Code", 17), justify="right")
entry.grid(row=0, column=0, columnspan=5)

# Buttons for digits and operations
buttons: list[str] = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "(", "0", ")", "/",
    "C", "=",
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=4, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
root.mainloop()
