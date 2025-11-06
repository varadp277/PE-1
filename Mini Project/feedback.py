import tkinter as tk
from tkinter import messagebox
import main

root, robot, status = main.run_app()

def send_feedback():
    msg = entry.get().strip().lower()
    
    if msg == "clean":
        status.config(text="Thank you! Area is already clean.")
    
    elif msg == "not clean":
        status.config(text="Our team is cleaning the area now (normal speed)...")
        robot.start_cleaning()
    
    else:
        messagebox.showwarning("Invalid Input", "Please type: clean or not clean")

fb = tk.Toplevel(root)
fb.title("Consumer Response")

tk.Label(fb, text="Is the road clean? Type: clean / not clean").pack(pady=(10, 4))
entry = tk.Entry(fb, width=28)
entry.pack(pady=4)
entry.focus()

tk.Button(fb, text="Submit", command=send_feedback).pack(pady=(6, 10))

root.mainloop()
