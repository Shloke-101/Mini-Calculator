import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("🎂 Happy Birthday Aahana 🎂")
root.geometry("400x400")
root.config(bg="#ffe4e1")

header = tk.Label(root, text="🎉 Happy Birthday Aahana! 🎉", font=("Helvetica", 18, "bold"), bg="#ffe4e1", fg="#d63384")
header.pack(pady=20)

def cake_clicked():
    messagebox.showinfo("Cake! 🎂", "Enjoy this sweet virtual cake, Aahana! 🍰 mmm YUM YUM")

def popper_clicked():
    messagebox.showinfo("Party Popper! 🎉", "Party time for the best person ever! 🎊")

def gift_clicked():
    messagebox.showinfo("Gift for Aahana 🎁", "Dear Aahana, you are caring, kind, loving, and the best and the most beautiful person ever. Happy Birthday! ❤️")

cake_button = tk.Button(root, text="🎂 Cake 🎂", font=("Helvetica", 16), bg="#ffb6c1", command=cake_clicked)
cake_button.pack(pady=10)

popper_button = tk.Button(root, text="🎊 Popper 🎊", font=("Helvetica", 16), bg="#ffb6c1", command=popper_clicked)
popper_button.pack(pady=10)

gift_button = tk.Button(root, text="🎁 Gift 🎁", font=("Helvetica", 16), bg="#ffb6c1", command=gift_clicked)
gift_button.pack(pady=10)

instruction = tk.Label(root, text="Click the buttons to celebrate together!", font=("Helvetica", 14), bg="#ffe4e1", fg="#d63384")
instruction.pack(pady=20)

root.mainloop()

