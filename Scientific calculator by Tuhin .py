import tkinter as tk
import math

root = tk.Tk()
root.title("Tuhin Scientific Calculator")
root.geometry("400x600")

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expr = entry_var.get()
            expr = expr.replace('^', '**')
            expr = expr.replace('√', 'math.sqrt')
            expr = expr.replace('sin', 'math.sin(math.radians')
            expr = expr.replace('cos', 'math.cos(math.radians')
            expr = expr.replace('tan', 'math.tan(math.radians')
            expr = expr.replace('log', 'math.log10')
            open_count = (
                expr.count("math.sin(math.radians") +
                expr.count("math.cos(math.radians") +
                expr.count("math.tan(math.radians")
            )
            if open_count > 0:
                expr += ")" * open_count
            result = eval(expr)
            entry_var.set(str(result))
        except:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        if text in ["sin", "cos", "tan", "√", "log"]:
            entry_var.set(entry_var.get() + text + "(")
        else:
            entry_var.set(entry_var.get() + text)

entry_var = tk.StringVar()
entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Arial", 24),
    bd=8,
    relief=tk.RIDGE,
    justify="right"
)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ['sin', 'cos', 'tan', 'log', 'C'],
    ['7', '8', '9', '^', '√'],
    ['4', '5', '6', '*', '/'],
    ['1', '2', '3', '+', '-'],
    ['0', '.', '=', '(', ')']
]

for row in buttons:
    f = tk.Frame(root)
    f.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(
            f,
            text=btn,
            font=("Arial", 18),
            relief=tk.RIDGE,
            bd=5
        )
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()