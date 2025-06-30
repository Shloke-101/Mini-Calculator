from  tkinter import  *

root = Tk()
root.title("Button Example")  # Set the title of the window
root.geometry("400x300")  # Set the size of the window
def myFunction():
    mylabel = Label(root, text="Button clicked!")
    mylabel.pack()

myButton = Button(root, text="Click this", command = myFunction, bg = "pink", fg = "white")  # Creating a button with text, command, background color, and foreground color
myButton.pack()  # Adding a button to the window and packing it 

root.mainloop()  # This will run the window until it is closed by the user

  # Adding a label to the window and packing it