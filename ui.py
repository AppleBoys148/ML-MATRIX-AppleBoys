import tkinter as tk
from PIL import ImageTk, Image
from tkinter import END, Toplevel, Listbox, MULTIPLE
from mainScript import *
import numpy as np
import sys
import pandas as pd

model = knn_model

def compare():
        PlotHist(train, title = "train")
        PlotHist(valid, title = "valid")
        PlotHist(test, title = "test")
        PlotHist(train, title = "train_resampled")
        PlotHist(valid, title = "valid")
        PlotHist(test, title = "test")

def exit():
    sys.exit()

def about():
    ab = Toplevel(root)
    ab.title("About Us")
    ab.geometry('1800x800')
    ab.configure(bg = 'blue')

    ab.grid_columnconfigure(1, weight = 1)
    ab.grid_columnconfigure(0, weight = 1)
    ab.grid_columnconfigure(2, weight = 1)
    ab.grid_rowconfigure(0, weight = 1)
    ab.grid_rowconfigure(1, weight = 1)
    ab.grid_rowconfigure(2, weight = 1)

    desc = tk.Label(ab, text = "Creators:\nHaseeb Ahmed S (ECE 1st Year, BMSCE) -data collection, ML application\nMadhav Krishnan Natarajan (CSE 1st Year, BMSCE) -UI/UX, ML\nDate Created: 19th Oct, 2024", bg = 'blue', fg = "black", font = "Arial, 10")
    desc.grid(row = 1, column = 1, sticky = 'nsew', padx = 10, pady = 10)

def diagnosing():
    dw = Toplevel(root)
    dw.title("DIAGNOSING")
    dw.geometry('1800x800')
    dw.configure(bg = 'darkblue')

    dw.grid_columnconfigure(1, weight = 1)
    dw.grid_columnconfigure(0, weight = 1)
    dw.grid_columnconfigure(2, weight = 1)
    dw.grid_rowconfigure(0, weight = 1)
    dw.grid_rowconfigure(1, weight = 1)
    dw.grid_rowconfigure(2, weight = 1)
    dw.grid_rowconfigure(3, weight = 1)
    dw.grid_rowconfigure(4, weight = 1)
    dw.grid_rowconfigure(5, weight = 1)

    l = tk.Label(dw, text = "Select symptoms", bg = "lightblue", fg = 'darkblue', font=("Helvetica", 20))
    l.grid(row = 0, column = 1, padx = 10, pady = 10)

    symptoms = []
    for a in symptNames.keys():
        symptoms.append(a)

    listbox = Listbox(dw, selectmode=MULTIPLE, width = 100, bg = "white", fg = 'black', font = ("Helvetica", 13))
    listbox.grid(row = 1, column = 1, padx = 50, pady = 10)

    for item in symptoms:
        listbox.insert(tk.END, item)

    result = tk.Label(dw, text = "", bg = "lightblue", fg = "black")
    result.grid(row = 4, column = 1, padx = 10, pady = 10)

    def DIAGNOSE():
        index = listbox.curselection()
        symtnamelist = [listbox.get(i) for i in index] 
        if len(symtnamelist) == 0:
            result.config(text = "Please select a symptom")
        elif len(symtnamelist) < 17:
            symtnamelist = symtnamelist + [np.nan]*(17-len(symtnamelist))
            result.config(text = Diagnose(symtnamelist, model))
        elif len(symtnamelist) > 17:
            result.config(text = "select less than 17")
        else:
            result.config(text = Diagnose(symtnamelist, model), font = ("Helvetica", 20)) 
    
    click = tk.Button(dw, text = 'Diagnose', bg = "lightblue", fg = 'black', relief = "groove", bd = 3, font = ("Helvetica", 20), width = 15, command = DIAGNOSE)
    click.grid(row = 3, column = 1, padx = 10, pady = 10)

    

root = tk.Tk()
root.title("ML MATRIX")

root.geometry("1800x800")

root.configure(bg = "blue")

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_columnconfigure(2, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)
root.grid_rowconfigure(3, weight = 1)

doctor = Image.open("stethoscope-10.png")
pic = ImageTk.PhotoImage(doctor)

img = tk.Label(root, image = pic)
img.grid(row = 1, rowspan = 2, column = 3, padx = 10, pady = 10)

whiz_button = tk.Button(root, text = "I am a Comp whiz", width = 20, font = ("Helvetica", 8), bg = 'beige', fg = 'black', relief = 'ridge', bd = 3, command = compare)
whiz_button.grid(row = 0, column = 3, padx = 2, pady = 2)

diagnose_button = tk.Button(root, text = "DIAGNOSE", width = 20, font=("Helvetica", 20), bg = "lightblue",fg = "black", relief = "raised", bd = 5, command = diagnosing)
abtus_button = tk.Button(root, text = "About Us", width = 5, font = ("Helvetica", 12), bg = "lightblue",fg = "black", relief = "raised", bd = 5, command = about)
exit_button = tk.Button(root, text = "Exit", width = 5, font = ("Helvetica", 12), bg = "lightblue",fg = "black", relief = "raised", bd = 5, command = exit)
diagnose_button.grid(row=1, column = 1, columnspan=2, sticky = 'nsew', padx = 20, pady = 10)
abtus_button.grid(row = 2, column = 1, sticky = 'nsew', padx = 10, pady = 5)
exit_button.grid(row = 2, column = 2, sticky = 'nsew', padx = 10, pady = 5)

root.mainloop()

