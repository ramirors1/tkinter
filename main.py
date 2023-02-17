#import tkinter  # used for GUI
from tkinter import *  # import every class within tkinter

#window = tkinter.Tk()  #creates the window, used when importing tkinter only
window = Tk()  # used when importing all classes from tkinter
window.title("My GUIness")
window.minsize(width=500, height=300)

# Label
#my_label = tkinter.Label(text="Labelocity", font=("Arial", 24, "italic"))  # used when importing tkinter only
my_label = Label(text="Labelocity", font=("Arial", 24, "italic"))  #used when importing all classes of tkinter
my_label.pack()

# updating labels that have been defined earlier
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Buttons
def button_clicked():
    print("You clicked me")
    new_text = input.get()
    my_label.config(text=new_text)
   #my_label.config(text="You clicked me")

button = Button(text="Clickety click me", command=button_clicked)
button.pack()

# Entry component
input = Entry(width=20)

input.pack()

window.mainloop()  # keeps the window on the screen
