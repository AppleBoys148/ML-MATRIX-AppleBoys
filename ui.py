import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Toplevel, Listbox, MULTIPLE
from mainScript import symptNames, Diagnose, lg_model, NULLINDEX
import numpy as np


final_res = []


def diagnosing():
    dw = Toplevel(root)
    dw.title("DIAGNOSING")
    dw.geometry('500x400')
    dw.configure(bg = 'darkblue')

    dw.grid_columnconfigure(1, weight = 1)
    dw.grid_columnconfigure(0, weight = 1)
    dw.grid_columnconfigure(2, weight = 1)
    dw.grid_rowconfigure(0, weight = 1)
    dw.grid_rowconfigure(1, weight = 1)
    dw.grid_rowconfigure(2, weight = 1)
    dw.grid_rowconfigure(3, weight = 1)

    l = tk.Label(dw, text = "Select symptoms", bg = "lightblue", fg = 'darkblue', font="Arial, 20")
    l.grid(row = 0, column = 1, padx = 10, pady = 10)

    symptoms = []
    for a in symptNames.keys():
        symptoms.append(a)

    listbox = Listbox(dw, selectmode=MULTIPLE, bg = "white", fg = 'black')
    listbox.grid(row = 1, column = 1, padx = 10, pady = 20)

    for item in symptoms:
        listbox.insert(tk.END, item)

    result = tk.Label(dw, text = "", bg = "lightblue", fg = "black")
    result.grid(row = 3, column = 1, padx = 10, pady = 10)

    def DIAGNOSE():
        index = listbox.curselection()
        symtnamelist = [listbox.get(i) for i in index] 
        if len(symtnamelist) < 17:
            symtnamelist = symtnamelist + [np.nan]*(17-len(symtnamelist))
            result.config(text = Diagnose(symtnamelist, lg_model))
        elif len(symtnamelist) > 17:
            result.config(text = "select less than 17")
        else:
            result.config(text = Diagnose(symtnamelist, lg_model)) 
    
    click = tk.Button(dw, text = 'Diagnose', bg = "lightblue", fg = 'black', relief = "groove", bd = 3, font = "Arial 20", width = 15, command = DIAGNOSE)
    click.grid(row = 2, column = 1, padx = 10, pady = 10)
   
root = tk.Tk()
root.title("ML MATRIX")

root.geometry("500x400")

root.configure(bg = "beige")

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)
root.grid_rowconfigure(3, weight = 1)

doctor = Image.open("stethoscope-10.png")
pic = ImageTk.PhotoImage(doctor)

img = tk.Label(root, image = pic)
img.grid(row = 1, rowspan = 2, column = 2, padx = 10, pady = 10)

diagnose_button = tk.Button(root, text = "DIAGNOSE", width = 20, font="Arial, 20", bg = "lightblue",fg = "black", relief = "raised", bd = 5, command = diagnosing)
quiz_button = tk.Button(root, text = "QUIZ", width = 20, font = "Arial 20", bg = "lightblue",fg = "black", relief = "raised", bd = 5)

diagnose_button.grid(row=1, column = 1, sticky = 'nsew', padx = 20, pady = 10)
quiz_button.grid(row = 2, column = 1, sticky = 'nsew', padx = 20, pady = 10)

root.mainloop()

