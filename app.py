#Mostrar PDF
def pdfMostrar():

    v1=pdf.ShowPdf()
    v2=v1.pdf_view(ventana,pdf_location=r"variable.pdf",width=80,height=100)
    v2.pack()

#Mostrar Preguntas

def testMostrar():

    lbq1 = Label(ventana,text="Pregunta 1")
    lbq1.place(x=200,y=150,height=30,width=100)

    imgBtDog=PhotoImage(file="perrito.gif")
    btOpDog=Button(ventana,image=imgBtDog,height=20,width=100).place(x=200,y=200)
    
    imgBtBird=PhotoImage(file="pajarito.gif")
    btOpBird=Button(ventana,image=imgBtBird,height=20,width=100).place(x=200,y=240)

    imgBtFish=PhotoImage(file="pez.gif")
    btOpFish=Button(ventana,image=imgBtFish,height=20,width=100).place(x=200,y=280)

    imgBtDuck=PhotoImage(file="patito.gif")
    btOpDuck=Button(ventana,image=imgBtDuck,height=20,width=100).place(x=200,y=320)

    imgBtTurtle=PhotoImage(file="tortuga.gif")
    btOpTurtle=Button(ventana,image=imgBtTurtle,height=20,width=100).place(x=200,y=360)

    lbq2 = Label(ventana,text="Pregunta 2")
    lbq2.place(x=200,y=400,height=30,width=100)

    imgBtDog2=PhotoImage(file="perrito.gif")
    btOpDog2=Button(ventana,image=imgBtDog2,height=20,width=100).place(x=200,y=440)

    imgBtBird2=PhotoImage(file="pajarito.gif")
    btOpBird2=Button(ventana,image=imgBtBird2,height=20,width=100).place(x=200,y=480)

    imgBtFish2=PhotoImage(file="pez.gif")
    btOpFish2=Button(ventana,image=imgBtFish2,height=20,width=100).place(x=200,y=520)

    imgBtDuck2=PhotoImage(file="patito.gif")
    btOpDuck2=Button(ventana,image=imgBtDuck2,height=20,width=100).place(x=200,y=560)

    imgBtTurtle2=PhotoImage(file="tortuga.gif")
    btOpTurtle2=Button(ventana,image=imgBtTurtle2,height=20,width=100).place(x=200,y=600)

    btOpDog.pack()
    btOpBird.pack()
    btOpFish.pack()
    btOpDuck.pack()
    btOpTurtle.pack()
    btOpDog2.pack()
    btOpBird2.pack()
    btOpFish2.pack()
    btOpDuck2.pack()
    btOpTurtle2.pack()

