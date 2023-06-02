#Modulos
from tkinter import *
import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import webbrowser
import random
import pickle
import os.path
import datetime
from tkinter import ttk
from tkinter import messagebox as MessageBox

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

#Diccionario donde se guardarán las fallas

diccionario_fallas = {}

def fallas():
    fallas = tk.Tk()
    fallas.title("Lista de fallas")
    fallas.geometry("600x500")

    global diccionario_fallas

    #Botón para crear, buscar, actualizar y eliminar una falla

    crear_falla = Button(fallas, text="Crear falla", width=15, height=2, bg="#00C040", command=lambda : funcion_crear_falla())
    crear_falla.place(x=240, y=50)

    consultar_falla = Button(fallas, text="Consultar falla", width=15, height=2, bg="#607ec9", command=lambda : funcion_consultar_falla())
    consultar_falla.place(x=240, y=100)

    actualizar_falla = Button(fallas, text="Actualizar falla", width=15, height=2, bg="#FFEA0C", command=lambda : funcion_actualizar_fallas())
    actualizar_falla.place(x=240, y=150)

    eliminar_falla = Button(fallas, text="Eliminar falla", width=15, height=2, bg="#FF0000", command=lambda : funcion_eliminar_fallas())
    eliminar_falla.place(x=240, y=200)

#Función inicial para crear fallas

def funcion_crear_falla():
    global crear_fallas
    crear_fallas = tk.Tk()
    crear_fallas.title("Crear una falla")
    crear_fallas.geometry("800x500")

    global diccionario_fallas
    global llave
    global descripcion
    global combo_t

    #Label para el título
    label_crear = tk.Label(crear_fallas, text="CREAR FALLA")
    label_crear.place(x=10, y=10)
    label_crear.config(font=("Arial", 20))

    #Label y entry de el número de falla
    label_falla = tk.Label(crear_fallas, text="Número de falla")
    label_falla.place(x=130, y=80)
    llave = tk.Entry(crear_fallas)
    llave.place(x=230, y=80)

    #Label y Text para la descripción de la falla
    label_descripcion = tk.Label(crear_fallas, text="Descripción de la falla")
    label_descripcion.place(x=100, y=130)
    descripcion = tk.Text(crear_fallas, height=10, width=50)
    #descripcion = tk.Entry(crear_fallas)
    descripcion.place(x=230, y=130)

    #Label
    label_tipo = tk.Label(crear_fallas, text="Tipo de falla")
    label_tipo.place(x=140, y=320)

    tipo = ["Leve", "Grave"]

    combo_t = ttk.Combobox(crear_fallas, values=tipo)
    combo_t.place(x=230, y=320)

    boton_aceptar = tk.Button(crear_fallas, text="Aceptar", width=10, height=2, command=lambda : agregar_fallas())
    boton_aceptar.place(x=240, y=370)

    boton_cancelar = tk.Button(crear_fallas, text="Cancelar", width=10, height=2, command=lambda : crear_fallas.destroy())
    boton_cancelar.place(x=340, y=370)


    crear_fallas.mainloop()

#Función que agregará los fallas al diccionario de fallas

def agregar_fallas():
    llave1 = llave.get()
    descripcion1 = descripcion.get("1.0", "end-1c")
    combo_t1 = combo_t.get()

    if llave1 in diccionario_fallas:
        messagebox.showinfo("Error", "La llave ya ha sido asignada")
    else:
        diccionario_fallas[llave1] = (descripcion1, combo_t1)
        print(diccionario_fallas)
        crear_fallas.destroy()

    #print(llave1, descripcion1, combo_t1)

#Función para consultar fallas

def funcion_consultar_falla():
    global consultar_fallas
    consultar_fallas = tk.Tk()
    consultar_fallas.title("Crear una falla")
    consultar_fallas.geometry("800x500")

    global diccionario_fallas
    global label_tipo2
    global llave
    global descripcion
    global combo_t

    #Label para el título
    label_consultar = tk.Label(consultar_fallas, text="CONSULTAR FALLA")
    label_consultar.place(x=10, y=10)
    label_consultar.config(font=("Arial", 20))

    #Label y entry para ingresar la llave
    label_falla = tk.Label(consultar_fallas, text="Número de falla")
    label_falla.place(x=130, y=80)
    llave = tk.Entry(consultar_fallas)
    llave.place(x=230, y=80)

    #Label y Text para mostrar la descripción
    label_descripcion = tk.Label(consultar_fallas, text="Descripción de la falla")
    label_descripcion.place(x=100, y=130)
    descripcion = tk.Text(consultar_fallas, height=10, width=50)
    #descripcion = tk.Entry(consultar_fallas, state="disabled")
    descripcion.place(x=230, y=130)

    #Dos Label para el tipo
    label_tipo = tk.Label(consultar_fallas, text="Tipo de falla")
    label_tipo.place(x=140, y=320)
    label_tipo2 = tk.Label(consultar_fallas, state="disabled")
    label_tipo2.place(x=230, y=320)

    #Botón para consultar
    boton_aceptar = tk.Button(consultar_fallas, text="Consultar", width=10, height=2, command=lambda : escribir_fallas())
    boton_aceptar.place(x=240, y=370)

    #Botón para salir
    boton_cancelar = tk.Button(consultar_fallas, text="Salir", width=10, height=2, command=lambda : consultar_fallas.destroy())
    boton_cancelar.place(x=340, y=370)

    consultar_fallas.mainloop()

#Función que escribe para mostrar la consulta
def escribir_fallas():

    llave_b = llave.get()
    if llave_b in diccionario_fallas:
        diccionario = diccionario_fallas[llave_b]
        descripcion2 = diccionario[0]
        tipo2 = diccionario[1]

        descripcion.insert("1.0", descripcion2)
        label_tipo2.config(text=tipo2)
    else:
        messagebox.showinfo("Error", "La llave no existe")
        consultar_fallas.destroy()

def funcion_actualizar_fallas():
    global actualizar_fallas
    actualizar_fallas = tk.Tk()
    actualizar_fallas.title("Actualizar una falla")
    actualizar_fallas.geometry("800x500")

    global diccionario_fallas
    global llave
    global descripcion
    global combo_t

    # Label para el título
    label_crear = tk.Label(actualizar_fallas, text="ACTUALIZAR FALLA")
    label_crear.place(x=10, y=10)
    label_crear.config(font=("Arial", 20))

    # Label y entry de el número de falla
    label_falla = tk.Label(actualizar_fallas, text="Número de falla")
    label_falla.place(x=150, y=80)
    llave = tk.Entry(actualizar_fallas)
    llave.place(x=250, y=80)

    # Label y Text para la descripción de la falla
    label_descripcion = tk.Label(actualizar_fallas, text="Nueva descripción de la falla")
    label_descripcion.place(x=90, y=130)
    descripcion = tk.Text(actualizar_fallas, height=10, width=50)
    # descripcion = tk.Entry(actualizar_fallas)
    descripcion.place(x=250, y=130)

    # Label
    label_tipo = tk.Label(actualizar_fallas, text="Nuevo tipo de falla")
    label_tipo.place(x=140, y=320)

    tipo = ["Leve", "Grave"]

    combo_t = ttk.Combobox(actualizar_fallas, values=tipo)
    combo_t.place(x=250, y=320)

    boton_aceptar = tk.Button(actualizar_fallas, text="Aceptar", width=10, height=2, command=lambda: cambiar_fallas())
    boton_aceptar.place(x=240, y=370)

    boton_cancelar = tk.Button(actualizar_fallas, text="Cancelar", width=10, height=2, command=lambda: actualizar_fallas.destroy())
    boton_cancelar.place(x=340, y=370)

    actualizar_fallas.mainloop()

    # Función que actualizará las fallas del diccionario de fallas

def cambiar_fallas():
    llave1 = llave.get()
    descripcion1 = descripcion.get("1.0", "end-1c")
    combo_t1 = combo_t.get()

    if llave1 in diccionario_fallas:
        diccionario_fallas[llave1] = (descripcion1, combo_t1)
        print(diccionario_fallas)
        actualizar_fallas.destroy()
    else:
        messagebox.showinfo("Error", "La llave no ha sido asignada")
        actualizar_fallas.destroy()



def funcion_eliminar_fallas():
    global eliminar_fallas
    eliminar_fallas = tk.Tk()
    eliminar_fallas.title("Crear una falla")
    eliminar_fallas.geometry("800x500")

    global diccionario_fallas
    global label_tipo2
    global llave
    global descripcion
    global combo_t

    #Label para el título
    label_eliminar = tk.Label(eliminar_fallas, text="ELIMINAR FALLA")
    label_eliminar.place(x=10, y=10)
    label_eliminar.config(font=("Arial", 20))

    #Label y entry para ingresar la llave
    label_falla = tk.Label(eliminar_fallas, text="Número de falla")
    label_falla.place(x=130, y=80)
    llave = tk.Entry(eliminar_fallas)
    llave.place(x=230, y=80)

    #Label y Text para mostrar la descripción
    label_descripcion = tk.Label(eliminar_fallas, text="Descripción de la falla")
    label_descripcion.place(x=100, y=130)
    descripcion = tk.Text(eliminar_fallas, height=10, width=50)
    #descripcion = tk.Entry(consultar_fallas, state="disabled")
    descripcion.place(x=230, y=130)

    #Dos Label para el tipo
    label_tipo = tk.Label(eliminar_fallas, text="Tipo de falla")
    label_tipo.place(x=140, y=320)
    label_tipo2 = tk.Label(eliminar_fallas, state="disabled")
    label_tipo2.place(x=230, y=320)

    #Botón para consultar
    boton_aceptar = tk.Button(eliminar_fallas, text="Eliminar", width=10, height=2, command=lambda : escribir_fallas2())
    boton_aceptar.place(x=240, y=370)

    #Botón para salir
    boton_cancelar = tk.Button(eliminar_fallas, text="Salir", width=10, height=2, command=lambda : eliminar_fallas.destroy())
    boton_cancelar.place(x=340, y=370)

    eliminar_fallas.mainloop()

def escribir_fallas2():

    llave_b = llave.get()
    if llave_b in diccionario_fallas:
        global ventana_confirmacion

        diccionario = diccionario_fallas[llave_b]
        descripcion2 = diccionario[0]
        tipo2 = diccionario[1]

        descripcion.insert("1.0", descripcion2)
        label_tipo2.config(text=tipo2)

        ventana_confirmacion = Toplevel()
        ventana_confirmacion.title("Confirmación")
        ventana_confirmacion.geometry("200x100")

        label_confirmacion = tk.Label(ventana_confirmacion, text="¿Seguro que desea eliminar la falla?")
        label_confirmacion.pack()

        boton_si = tk.Button(ventana_confirmacion, text="Si", width=4, command=lambda : eliminar(llave_b))
        boton_si.place(x=55, y=50)

        boton_no = tk.Button(ventana_confirmacion, text="No", width=4, command=lambda : salir_de_todo())
        boton_no.place(x=100, y=50)
    else:
        messagebox.showinfo("Error", "La llave no existe")
        eliminar_fallas.destroy()

def eliminar(llave):
    del diccionario_fallas[llave]
    ventana_confirmacion.destroy()
    eliminar_fallas.destroy()

def salir_de_todo():
    ventana_confirmacion.destroy()
    eliminar_fallas.destroy()


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




