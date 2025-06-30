from tkinter import *
root = Tk()

root.title("Grid Example")  # Set the title of the window
root.geometry("400x300")  # Set the size of the window
label1 = Label(root, text="Label 1", bg="red", fg="white")
label2 = label = Label(root, text="Label 2", bg="blue", fg="white")

label1.grid(row = 0, column = 1)
label2.grid(row=1, column=0)

root.mainloop()  # This will run the window until it is closed by the user