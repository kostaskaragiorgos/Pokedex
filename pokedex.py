""" Csv File Spliter"""
from tkinter import Menu, Button, messagebox as msg, Tk, Label
from tkinter import filedialog, Text, IntVar, Checkbutton
from tkinter.constants import END

import pandas as pd


def helpmenu():
    """help menu function"""
    pass

    
def aboutmenu():
    """about menu function"""
    msg.showinfo("About", "POKEDEX\nVersion 1.0")


class Pokedex():
    def __init__(self, master):
        self.master = master
        self.master.title("POKEDEX")
        self.master.geometry("250x250")
        self.master.resizable(False, False)

        self.pokemonnamelab = Label(self.master, text="Enter the name of the pokemon")
        self.pokemonnamelab.pack()

        self.pokemontext = Text(self.master, height=1, width=10)
        self.pokemontext.pack()

        self.findbutton = Button(self.master, text="FIND", command=self.findpokemon())
        self.findbutton.pack()

        self.clearbutton = Button(self.master, text="CLEAR", command=self.clearname())
        self.clearbutton.pack()

        self.menu = Menu(self.master)
        
        
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())

    
    def clearname(self):
        pass
    def findpokemon(self):
        pass

    def exitmenu(self):
        """exit menu function"""
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()



def main():
    """main functionn"""
    root = Tk()
    Pokedex(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()