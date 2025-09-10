import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Demo")

ttk.Label(root, text="Choose:").grid(row=0, column=0, padx=8, pady=8)
choice = tk.StringVar()
combo = ttk.Combobox(root, textvariable=choice, values=["A", "B", "C"], state="readonly")
combo.grid(row=0, column=1, padx=8, pady=8)

def go():
    print("You chose:", choice.get())

ttk.Button(root, text="Go", command=go).grid(row=1, column=0, columnspan=2, pady=8)
root.mainloop()
