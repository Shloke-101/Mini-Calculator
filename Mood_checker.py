from tkinter import *
root = Tk()
root.title("Mood_Checker")  # Set the title of the window
root.geometry("400x300")  # Set the size of the window
bg = "light pink"  # Define the background color
root.config(bg=bg)  # Set the background color of the main window

label1 = Label(root, text="Are you happy ?") # Create a label in the main window
font = ('Courier', 12, 'bold')  # Define the font style
label1.config(font=font, bg="light pink", fg="black")  # Configure the label with font, background color, and foreground color

# Function to create a new window when the "Yes" button is clicked
def Happy():
    new_window = Toplevel(root)  # Create a new window
    bg = "light green"  # Define the background color for the new window
    new_window.config(bg=bg)  # Set the background color of the new window
    new_window.title("YAYYYY")  #Set the title of the new window
    new_window.geometry("400x300")  # Set the size of the new window
    mylabel = Label(new_window, text="CONGRATS ON BEING HAPPY", bg = "yellow")  # Create a label in the new window
    mylabel.pack()  # Pack the label into the new window

def Sad():
    new_window = Toplevel(root)  # Create a new window
    new_window.title("Awwww")  # Set the title of the new window
    bg = "light blue"  # Define the background color for the new window
    new_window.config(bg=bg)  # Set the background color of the new window
    new_window.geometry("400x300")  # Set the size of the new window
    mylabel = Label(new_window, text="DON'T BE SAD, YOU WILL BE HAPPY SOON", bg = "grey")  # Create a label in the new window
    mylabel.pack()  # Pack the label into the new window


Button1 = Button(root, text="Yes", command=Happy, bg="Green", fg="white", width = 10, height = 2)  # Creating a button with text, command, background color, and foreground color
Button1.pack(side = LEFT, padx = 20, pady = 50)  # Adding the first button to the window and packing it
Button2 = Button(root, text="No", command= Sad , bg="blue", fg = "white", width = 10, height = 2)  # Creating another button with text, command, background color, and foreground color
Button2.pack(side = RIGHT, padx = 20, pady = 50)  # Adding the second button to the window and packing it
label1.pack()  # Adding the label to the window and packing it
root.mainloop()  # This will run the window until it is closed by the user