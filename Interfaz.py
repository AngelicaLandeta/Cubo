from tkinter import *
import serial
import time
import threading

value_input_digital=0
value_output_digital=0

arduino= serial.Serial("COM11", 9600)
time.sleep(0)


#########################################################################
#FUNCIONES
class Interfaz: 
    def __init__():
        value_input_analog= StringVar()
        value_input_digital= StringVar()
        val=StringVar()
        pwm= StringVar()
        cad= StringVar()
        Encender_Led=IntVar()
#Función para lectura de sensores
def getSensorValues():
    
    while True:
        hilo1 = threading.Thread(target= getSensorValues,daemon=True)
        cad =arduino.readline().decode('ascii').strip()
        if cad:         
            pos=cad.index(":")
            label=cad[:pos] #Desde inicio hasta POS
            value=cad[pos+1:] #Desde POS+1 hasta final
        if label == 'Pulso':
            value_input_digital=value                   
        if label == 'pot':
            value_input_analog=value
            print (value_input_digital)
                    

        hilo1.start()


#Función para cerrar ventana
def Close_Window():
    arduino.close() #cierra la comunicación del arduino con el puerto serie
    cuadro.destroy() #cierra la ventana
#Función para encender led
def Encender_Led():
    cad='led:1' 
    arduino.write(cad.encode('ascii'))
# print(cad)

#Función para apagar led   
def Apagar_Led():
    cad='led:0' 
    arduino.write(cad.encode('ascii'))
#  print(cad)

#Función para escribir los valores del PWM  
def print_value():
   pwm= val
   cad='pwm:'+ str(pwm)
   arduino.write(cad.encode('ascii'))
   
#print(cad)
#########################################################################
#Panel o ventana de instrumentos
cuadro=Tk()
cuadro.geometry("500x500")
cuadro.title("Adquisición de datos")
##########################################################################
#Frame o cuadro superior
TitleFrame= Frame() 
TitleFrame.config(bg="black", width = "500", height= "60")
TitleFrame.place(x=0, y=0)

#Título en el cuadro 
labelTitulo= Label(TitleFrame, text="Interfaz de Usuario", bg= "blue",
                   fg = "white", font=("Arial", 14))
labelTitulo.place(x=170, y=15)
###########################################################################
#Frame o cuadro inferior
ButtonsFrame= Frame()
ButtonsFrame.config(bg="blue", width = "500", height= "450")
ButtonsFrame.place(x=0, y=60)

#WIDGETS
#Botón de encender led
button_on= Button(ButtonsFrame, text="Encender", bg="green", 
                  fg ="white", font=("Arial", 10), command=Encender_Led)
button_on.place(x=107, y=77)
#Botón de apagar led
button_off= Button(ButtonsFrame, text="Apagar", bg="red",
                   fg ="white", font=("Arial", 10), command=Apagar_Led)
button_off.place(x=57, y=77)
label_Salida_digital= Label(ButtonsFrame, text="Salida Digital:", bg= "black",
                   fg = "white", font=("Arial", 11))
label_Salida_digital.place(x=70, y=50)

#Botón de cerrar
button_close= Button(ButtonsFrame, text="Cerrar", 
                     bg="gray", fg ="black", font=("Arial", 10), command=Close_Window)
button_close.place(x=230, y=400)

#Barra deslizante
Barra=Scale(ButtonsFrame, from_=0, to=255, tickinterval=25, resolution=25.5, length=350, width=20, cursor='arrow',
            label='Intensidad', orient= HORIZONTAL, troughcolor= "orange", 
            bg="black", activebackground= 'red', fg ="white", font=("Arial", 10), command= print_value)
Barra.place(x=70, y=200)
label_Salida_PWM= Label(ButtonsFrame, text="Salida Digital PWM:", bg= "black",
                   fg = "white", font=("Arial", 11))
label_Salida_PWM.place(x=170, y=170)

#Desplegador entrada analógica
Display_analog= Label(ButtonsFrame, textvariable=value_input_analog, width=5, 
                     bg="white", fg ="black", font=("Arial", 10))
Display_analog.place(x=400, y=50)
label_Display_analog= Label(ButtonsFrame, text="Entrada Analógica:", bg= "black",
                   fg = "white", font=("Arial", 11))
label_Display_analog.place(x=270, y=49)

#Desplegador entrada digital
Display_digital= Label(ButtonsFrame, textvariable=value_input_digital, width=5, 
                     bg="white", fg ="black", font=("Arial", 10)) 
Display_digital.place(x=400, y=80)
label_Display_digital= Label(ButtonsFrame, text="Entrada Digital:", bg= "black",
                   fg = "white", font=("Arial", 11))
label_Display_digital.place(x=270, y=79)
print(value_input_digital)
############################################################################
#Panel o ventana de instrumentos como principal
cuadro.mainloop()
