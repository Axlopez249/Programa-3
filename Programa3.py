#Modulos
from tkinter import *
import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import webbrowser
import random
import pickle
import os.path

menu_inicial = tk.Tk()
menu_inicial.title("Menu principal")
menu_inicial.geometry("600x500")

#Titulo RETEVE
label_reteve = tk.Label(menu_inicial, text = "RETEVE")
label_reteve.place(x = 10, y = 10)

#Variables funcion crear citas
numero_cita = 0





#Funciones
def crear_citas():
    citas = tk.Tk()
    citas.title("Programacion de citas")
    citas.geometry("600x500")

    #Crear acceso a las variables fuera de la funcion
    global numero_cita
    numero_cita += 1

    #Titulo del numero de cita
    label_num_cita = tk.Label(citas, text = "Número de cita: " + str(numero_cita))
    label_num_cita.place(x = 10, y = 10)

    citas.mainloop()

def cancelar_citas():
    citas = tk.Tk()
    citas.title("Programacion de citas")
    citas.geometry("600x500")

    citas.mainloop()

def ingreso_estacion():
    estacion = tk.Tk()
    estacion.title("Programacion de citas")
    estacion.geometry("600x500")

    estacion.mainloop()

def tablero():
    tablero = tk.Tk()
    tablero.title("Programacion de citas")
    tablero.geometry("600x500")

    tablero.mainloop()

def fallas():
    fallas = tk.Tk()
    fallas.title("Lista de fallas")
    fallas.geometry("600x500")

    fallas.mainloop()

def configuracion():
    configuracion = tk.Tk()
    configuracion.title("Programacion de citas")
    configuracion.geometry("600x500")

    configuracion.mainloop()




#Botones para acceder a diferentes opciones que solicita el programa
#Cargar cita
b_cargar_cita = tk.Button(menu_inicial, text = "Programar citas", width = 15, height =2, bg = "green", command=crear_citas)
b_cargar_cita.place(x=250, y=50)

#Cancelar cita
b_cancelar_cita = tk.Button(menu_inicial, text = "Cancelar citas", width = 15, height =2, bg = "red", command=cancelar_citas)
b_cancelar_cita.place(x=250, y=100)

# Ingreso de vehículos a la estación
b_ingreso_estacion = tk.Button(menu_inicial, text = "Ingreso de vehículos a la estación", width = 25, height =2, bg = "light yellow",command=ingreso_estacion)
b_ingreso_estacion.place(x=210, y=150)

#Tablero de revisión.
b_tablero = tk.Button(menu_inicial, text = "Tablero de revisión", width = 15, height =2, bg = "light blue",command=tablero)
b_tablero.place(x=250, y=200)

# Lista de fallas
b_fallas = tk.Button(menu_inicial, text = "Lista de fallas", width = 15, height =2, bg = "orange",command=fallas)
b_fallas.place(x=250, y=250)

# Configuración del sistema
b_configuracion = tk.Button(menu_inicial, text = "Configuración del sistema", width = 20, height =2, bg = "PeachPuff4",command=configuracion)
b_configuracion.place(x=230, y=300)


menu_inicial.mainloop()




