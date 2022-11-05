from tkinter import *
from tkinter import ttk
from tkPDFViewer import tkPDFViewer as pdf
import tkinter as tk

def pdfMostrar():

    v1=pdf.ShowPdf()
    v2=v1.pdf_view(win,pdf_location=r"variable.pdf",width=80,height=60)
    v2.pack()

win = Tk()

boton=Button(text="Informacion",command=pdfMostrar())
boton.pack()
boton.place(x=50,y=50)

boton=Button(text="Preguntas",command=pdfMostrar())
boton.pack()
boton.place(x=50,y=80)

win.geometry("600x600")

win.title("MyScroller")
win.mainloop()