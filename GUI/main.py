from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from Trie import *

# Trie -------------------------------------------------------------------------
t = Trie()
# File -------------------------------------------------------------------------
global file
def choose_file():
    filepath = filedialog.askopenfilename(title='Open a text file')
    file = open(filepath) # Open file
    combo_value = []
    for i in file.readlines(): # Inserting into the Trie
        t.insert(i)
        combo_value.append(i)
    combo['values'] = combo_value
    file.close()
# ActionMethod -----------------------------------------------------------------
def ActionMethod(event):
    var = t.AutoSuggestions(combo.get())
    if var == -1:
        combo['values'] = []
        print("Trie is Empty...\n")
    elif var == 0:
        combo['values'] = []
        print("No words found with this title...\n")
    else:
        combo['values'] = var
# Gui --------------------------------------------------------------------------
def gui():
    root=Tk() # Object of Tk liblary
    
    v = tk.StringVar()

    peyw = Label(root, text = "Please enter your word :").place(x=40,y=40)  # Label 
    
    global combo
    combo = ttk.Combobox(root , width= 40 , textvariable=v)
    combo.pack(padx=40 , pady=80)
    combo.bind("<KeyRelease>" , ActionMethod) #Action listener

    Button(root,text="Choose File", command=choose_file, width=10).place(x=40,y=250) # Button Choose file

    root.geometry('330x300') # Size of root
    root.resizable(0,0)
    root.title("Data structure and Algorithm") # Title
    mainloop()
gui()