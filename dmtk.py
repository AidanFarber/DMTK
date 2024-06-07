from tkinter import *

items_5e = {
    "healing_potion",
}

class Character:
    def __init__(self, name, stats, inventory):
        self.name = name
        self.stats = stats
        self.inventory = inventory

def main():
    root = Tk()

    # Basic GUI Setup
    root.title("DMTK v1.0")
    root.geometry('900x600')

    lbl = Label(root, text = "Character Info Follows")
    lbl.grid()


    # Execute TKinter
    root.mainloop()

def addCharacter():
    None

if __name__ == "__main__":
    main()
