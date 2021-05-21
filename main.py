import tkinter as tk

root = tk.Tk()
v = tk.IntVar()
tk.Label(root, text="Symbol").grid(row=0)

tk.Label(root, text="Period").grid(row=1)

tk.Radiobutton(root, text="3mo", padx = 20, 
               variable=v, 
               value=1).pack(anchor=tk.W)

tk.Radiobutton(root, 
               text="1mo",
               padx = 20, 
               variable=v, 
               value=2).pack(anchor=tk.W)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

root.mainloop()