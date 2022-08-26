from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.geometry("1000x800")
root.title("GUI Creator")
root.config(background="#F5F1E3")

elements = ["Label", "Button", "Dropdown"]
elementsDropdown = ttk.Combobox(root, state = "readonly", values = elements, width = 10)
elementsDropdown.place(relx=0.5, rely=0.03, anchor=CENTER)


class CreateElements():
    def __init__(self):
        print("This is create Elements Class")
    
    def createLabel(self):
        label = Label(root, text = "New label created with Class", fg = "red")
        label.pack()
    
    def createButton(self):
        button = Button(root, text = "Button", command = self.message)
        button.pack()
    
    def createDropdown(self):
        list = ["1", "2", "3", "4", "5"]
        Dropdown = ttk.Combobox(root, state="readonly", values = list)
        Dropdown.pack()
    def choose(self):
        global elementsDropdown
        ComboboxVal = elementsDropdown.get()
        if ComboboxVal == "Label":
            self.createLabel()
        if ComboboxVal == "Button":
            self.createButton()
        if ComboboxVal == "Dropdown":
            self.createDropdown()
    def message(self):
        showinfo(title="Message", message="You clicked the Button using the class")

CreateElements = CreateElements()
Button1 = Button(root, text="Create Element", command = CreateElements.choose)
Button1.place(relx=0.5, rely=0.07, anchor=CENTER)

root.mainloop()