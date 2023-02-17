#import tkinter  # used for GUI
from tkinter import *  # import every class within tkinter

def button_clicked():
    print("You clicked me")
    new_text = input.get()
    my_label.config(text=new_text)
   #my_label.config(text="You clicked me")

#window = tkinter.Tk()  #creates the window, used when importing tkinter only
window = Tk()  # used when importing all classes from tkinter
window.title("My GUIness")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  #adds padding 

# Label
#my_label = tkinter.Label(text="Labelocity", font=("Arial", 24, "italic"))  # used when importing tkinter only
my_label = Label(text="Labelocity", font=("Arial", 24, "italic"))  #used when importing all classes of tkinter
my_label.config(text="New Text")
#my_label.pack() # placement is defined automatically
#my_label.place(x=50, y=0)  #allows you to place items in specific coordinates
my_label.grid(column=0, row=0)  # uses grid format to place items

# updating labels that have been defined earlier
# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# Buttons

button = Button(text="Clickety click me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Clickerocity me", command=button_clicked)
#button.pack()
new_button.grid(column=2, row=0)

# Entry component
input = Entry(width=20)
input.grid(column=3, row=2)
#input.pack()

window.mainloop()  # keeps the window on the screen
