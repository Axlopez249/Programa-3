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
label_reteve.config(font=("Arial", 20))

#Variables funcion crear citas
numero_cita = 0
tipo_cita = IntVar()




#Funciones
def crear_citas():
    citas = tk.Tk()
    citas.title("Programacion de citas")
    citas.geometry("600x750")

    #Crear acceso a las variables fuera de la funcion
    global numero_cita, tipo_cita
    numero_cita += 1

    #Titulo del numero de cita
    label_num_cita = tk.Label(citas, text = "Número de cita: " + str(numero_cita))
    label_num_cita.place(x = 10, y = 10)
    label_num_cita.config(font=("Arial", 15))

    #Solicitud de datos

    #Tipo de cita
    label_tipo_cita = tk.Label(citas, text = " Tipo de cita: ")
    label_tipo_cita.place(x = 100, y = 80)
    label_tipo_cita.config(font=("Arial", 10))
    t1 = tk.Radiobutton(citas, text="Primera vez", variable=tipo_cita, value=1)
    t2 = tk.Radiobutton(citas, text="Reinspección", variable=tipo_cita, value=2)
    t1.place(x = 120, y = 100)
    t2.place(x = 120, y = 120)
    #--------------------------------------------------------------------------------------------
    #Placa
    label_placa = tk.Label(citas, text = "Número de placa: ")
    label_placa.place(x = 100, y = 140)
    texto_placa = tk.Entry(citas)
    texto_placa.place(x = 200, y = 140)
    #--------------------------------------------------------------------------------------------
    #Tipo de vehículo
    label_vehiculo = tk.Label(citas, text = "Tipos de vehiculos:")
    label_vehiculo.place(x = 100, y = 160)
    vehiculos = tk.Listbox(citas, selectmode=tk.UNITS, width=75)
    lista_tipos_vehiculos = ["Automovil particular y vehiculo de carga liviana (menor o iguala 3500kg)",
                             "Automovil particular y vehiculo de carga liviana (mayor a 3500kg, menor a 8000kg)",
                             "Vehiculo de carga pesada y cabezales (mayor o iguala a 8000kg)",
                             "Taxis",
                             "Autobuses, buses y microbuses",
                             "Motocicletas",
                             "Equipo especial de obras",
                             "Equipo especial agricola (maquinaria agricula)"]
    for elemento in lista_tipos_vehiculos:
        vehiculos.insert(tk.END, elemento)
    vehiculos.place(x = 80, y = 180)
    # Función que se ejecuta al hacer clic en el botón aceptar
    def obtener_seleccion():
        seleccion = vehiculos.curselection()
        if seleccion:
            indice = seleccion[0]
            elemento = vehiculos.get(indice)
    #--------------------------------------------------------------------------------------------
    #Marca del vehiculo
    label_marca = tk.Label(citas, text = "Marca del vehiculo: ")
    label_marca.place(x = 100, y = 360)
    texto_marca = tk.Entry(citas)
    texto_marca.place(x = 210, y = 360)
    #--------------------------------------------------------------------------------------------
    #Modelo
    label_modelo = tk.Label(citas, text = "Modelo: ")
    label_modelo.place(x = 100, y = 383)
    texto_modelo = tk.Entry(citas)
    texto_modelo.place(x = 160, y = 383)
    #--------------------------------------------------------------------------------------------
    #Propietario
    label_propietario = tk.Label(citas, text = "Propietario: ")
    label_propietario.place(x = 100, y = 405)
    texto_propietario = tk.Entry(citas)
    texto_propietario.place(x = 165, y = 405)
    #--------------------------------------------------------------------------------------------
    #Telefono
    label_telefono = tk.Label(citas, text = "Telefono: ")
    label_telefono.place(x = 100, y = 430)
    texto_telefono = tk.Entry(citas)
    texto_telefono.place(x = 160, y = 430)
    #--------------------------------------------------------------------------------------------
    #Correo electrónico
    label_correo = tk.Label(citas, text = "Correo electrónico: ")
    label_correo.place(x = 100, y = 450)
    texto_correo = tk.Entry(citas)
    texto_correo.place(x = 210, y = 450)
    #Validacion del correo
    correo = texto_correo.get()
    #Toma el import del gmail y revisa la estrctura
    #E: un elemento string de email
    #S: true si el email es correcto
    def is_valid_email(email):
        from validate_email import validate_email

        is_valid = validate_email(email, verify=True)

        if is_valid:
            return 
        else:
            texto_correo.config(text = " ")
            return messagebox.showinfo("Error", "Correo electrónico inválido")
 
    #-------------------------------------------------------------------------
    #Direccion
    label_direccion = tk.Label(citas, text = "Direccion: ")
    label_direccion.place(x = 100, y = 480)
    texto_direccion = tk.Entry(citas)
    texto_direccion.place(x = 160, y = 480)
    
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




