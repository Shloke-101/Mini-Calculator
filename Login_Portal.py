from tkinter import *
root = Tk()
root.title("Login Portal")
root.geometry("700x400")
root.config(bg="#f0f0f0")
bg = "lightblue"
root.configure(bg=bg)
label1 = Label(root, text="Username", font=("Helvetica", 24), bg="#da7cff")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = Entry(root, font=("Arial", 24), bg="#f0f0f0")
entry1.grid(row=0, column=1, padx=10, pady=10)


label2 = Label(root, text="Password", font=("Helvetica", 24), bg="#fcff5b")
label2.grid(row=1, column=0, padx=10, pady=20)

entry2 = Entry(root, font=("Arial", 24), bg="#f0f0f0", show="*")
entry2.grid(row=1, column=1, padx=10, pady=20)

def Log_in():
    username = entry1.get()
    password = entry2.get()
    if username == "admin" and password == "Bilwa1234":
        success_label = Label(root, text="Login Successful!", font=("Arial", 24), fg="green", bg="#f0f0f0")
        success_label.grid(pady=20)
    else:
        error_label = Label(root, text="Invalid Credentials", font=("Arial", 24), fg="red", bg="#f0f0f0")
        error_label.grid(pady=20)

login_button = Button(root, text="Login", font=("Arial", 24), bg="#3c9bc0", fg="white", command= Log_in)
login_button.grid(row = 2, column = 1,)

root.mainloop()
