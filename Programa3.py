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
#Ok, voy
#
numero_cita = 0
tipo_cita = IntVar()
citas = {}
lineas = 6
minutos_revision = 30
dias_reinspeccion = 30
cant_meses = 1
cant_fallas = 4
porcentaje = 13.0
hora_inicio = 6
hora_final = 21
fecha = ""
hora = ()
precios_vehiculos = [10920, 14380, 14380, 11785, 14380, 7195, 14380, 6625]
opcion_fechas = StringVar()

#Se guarda la informacion en el archivo
archivo_path = "Datos_configuracion.dat"
if os.path.isfile(archivo_path):
    with open(archivo_path, 'rb') as archivo:
        # Carga los datos del archivo pickle
        datos_guardados = pickle.load(archivo)

    lineas = datos_guardados[0]
    hora_inicio = datos_guardados[1]
    hora_final = datos_guardados[2]
    cant_fallas = datos_guardados[3]
    cant_meses = datos_guardados[4]
    dias_reinspeccion = datos_guardados[5]
    minutos_revision = datos_guardados[6]
    porcentaje = datos_guardados[7]
    precios_vehiculos = datos_guardados[8]



#Funciones
def crear_citas():

    citas = tk.Tk()
    citas.title("Programacion de citas")
    citas.geometry("900x750")

    #Crear acceso a las variables fuera de la funcion
    global numero_cita, tipo_cita, opcion_fechas
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
    
    #--------------------------------------------------------------------------
    #Opcion para tomar las fechas
    #Esta funcion es para crear los list_box cuando el usuario marca la casilla de seleccion automatica
    #E: Vacia
    #S: La creacion y seleccion de las fechas
    def opcion_automatica(): 
        global hora_final, hora_inicio, cant_meses, minutos_revision
        h_i = hora_inicio
        h_f = hora_final
        #Se muestran las fechas y horas

        #Proceso para las fechas
        cantidad_dias = cant_meses * 30
        # Obtener la fecha actual
        fecha_actual = datetime.date.today()

        # Obtener la fecha final (dentro de un mes)
        fecha_final = fecha_actual + datetime.timedelta(days = cantidad_dias)

        # Iterar desde la fecha actual hasta la fecha final
        fecha_actual_iteracion = fecha_actual
        fechas_dias = []
        while fecha_actual_iteracion <= fecha_final:
            fechas_dias.append(fecha_actual_iteracion)
            fecha_actual_iteracion += datetime.timedelta(days=1)


        #Se muestra el proceso para las horas por dia
        lista_horas_por_dia = []
        minutos = 0
        while h_i < h_f:
            
            if minutos == 60:
                h_i += 1
                minutos = 0
            if minutos > 60:
                h_i += 1
                minutos = (minutos-60)
            lista_horas_por_dia.append((h_i, minutos))
            minutos += minutos_revision

        #Procesos para la creacion de los listbox
    
        #Se muestra la Listbox de las fechas
        # Crear el Frame 
        label_horas = Label(citas, text = "Fechas en días")
        label_horas.place(x = 130, y = 540)

        frame_dias = tk.Frame(citas)
        frame_dias.place(x = 90, y = 560)

        fechas = tk.Listbox(frame_dias, selectmode=tk.UNITS, width=40, height=4)
        fechas.pack(side = 'left',fill = 'y' )

        scrollbar_fechas = Scrollbar(frame_dias, orient="vertical",command=fechas.yview)
        scrollbar_fechas.pack(side="right", fill="y")

        fechas.config(yscrollcommand=scrollbar_fechas.set)

        for elemento in fechas_dias:
            fechas.insert(tk.END, elemento)


        # Crear el Frame de las horas
        label_horas = Label(citas, text = "Horas y minutos")
        label_horas.place(x = 430, y = 540)

        frame = tk.Frame(citas)
        frame.place(x = 390, y = 560)

        horas = tk.Listbox(frame, selectmode=tk.UNITS, width=40, height=4)
        horas.pack(side = 'left',fill = 'y' )

        scrollbar_horas = Scrollbar(frame, orient="vertical",command=horas.yview)
        scrollbar_horas.pack(side="right", fill="y")

        horas.config(yscrollcommand=scrollbar_horas.set)

        for elemento in lista_horas_por_dia:
            horas.insert(tk.END, elemento)



        #Funciones para guardar la informacion de la cita
        #Botones para guardar la fecha y la hora
        acep_fecha = tk.Button(citas, text="Guardar fecha", width=10)
        acep_fecha.place(x = 130, y = 640)

        acep_hora = tk.Button(citas, text= "Guardar hora", width=10)
        acep_hora.place(x = 430, y = 640)

        return
    #Esta funcion se llama cuando el usuario decide solicitar la cita de forma manual
    #E: Vacia
    #S: Validaciones de la fecha
    def opcion_manual():
        label_fecha = Label(citas, text = "Indique la fecha a solicitar (aaaa-mm-dd) ")
        label_fecha.place(x = 100, y = 540)
        entry_fecha = Entry(citas, width=10)
        entry_fecha.place(x = 320, y = 540)

        label_hora = Label(citas, text = "Indique la hora a solicitar (hh,mm) ")
        label_hora.place(x = 100, y = 560)
        entry_hora = Entry(citas, width=10)
        entry_hora.place(x = 320, y = 560)

        #Funcion para consultar si una cita esta disponible cuando le usuario decide solicitarla de forma manual
        #E: vacia
        #S: Un mensaje de afirmacion si esta disponible o no de lo contrario
        def consultar_citas():
            global hora_final, hora_inicio, minutos_revision, cant_meses
            #Aqui se toman las variables globales para no modificarlas y modificar su contenido
            h_i = hora_inicio
            h_f = hora_final
            fecha = entry_fecha.get()
            tiempo = entry_hora.get()
            lista_tiempo = tiempo.split(",")
            horas = int(lista_tiempo[0])
            minu = int(lista_tiempo[1])

            #Se sacan las fechas disponibles segun los minutos por revision
            lista_horas_por_dia = []
            minutos = 0
            while h_i < h_f:
                
                if minutos == 60:
                    h_i += 1
                    minutos = 0
                if minutos > 60:
                    h_i += 1
                    minutos = (minutos-60)
                lista_horas_por_dia.append((h_i, minutos))
                minutos += minutos_revision


            cantidad_dias = cant_meses * 30
            # Obtener la fecha actual
            fecha_actual = datetime.date.today()

            # Obtener la fecha final (dentro de un mes)
            fecha_final = fecha_actual + datetime.timedelta(days = cantidad_dias)

            # Iterar desde la fecha actual hasta la fecha final
            fecha_actual_iteracion = fecha_actual
            fechas_dias = []
            while fecha_actual_iteracion <= fecha_final:
                fechas_dias.append(fecha_actual_iteracion)
                fecha_actual_iteracion += datetime.timedelta(days=1)

            #Se recorre la lista creada para verificar que esa hora exista y esté disponible
            for elemento in lista_horas_por_dia:
                if elemento[0] == horas and elemento[1] == minu:
                    for ele in fechas_dias:
                        
                        if str(ele) == fecha:
                            messagebox.showinfo("Cita", "Fecha disponible")
                            return 
            
            
            messagebox.showerror("Cita", "Fecha no disponible")
            return

        boton_consultar = tk.Button(citas, text="Consultar", width=10, command = consultar_citas)
        boton_consultar.place(x=100, y=580)



    #Radio botones de la opciones para solicitar la cita
    manual = tk.Radiobutton(citas, text="Manual", variable=opcion_fechas, value="opcion1", command=opcion_manual)
    manual.place(x = 100, y = 500)
    automatico = tk.Radiobutton(citas, text="Automático", variable=opcion_fechas, value="opcion2", command=opcion_automatica)
    automatico.place(x = 100, y = 520)
    #--------------------------------------------------------------------------
    

    """boton_aceptar = tk.Button(citas, text="" , width=10)
    boton_aceptar.place()"""


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
    configuracion.geometry("900x700")

    label_titulo = tk.Label(configuracion, text= "CONFIGURACION")
    label_titulo.place(x= 50, )

    label_lineas = tk.Label(configuracion, text="Líneas de trabajo (1-25)")
    label_lineas.place(x = 50, y = 60)
    entry_lineas = tk.Entry(configuracion)
    entry_lineas.place(x = 180, y = 60)

    label_hora_inicio = tk.Label(configuracion, text="Hora inicial (0-23)")
    label_hora_inicio.place(x = 50, y = 90)
    entry_hora_inicio = tk.Entry(configuracion)
    entry_hora_inicio.place(x = 150, y = 90)

    label_hora_final = tk.Label(configuracion, text="Hora final (0-23)")
    label_hora_final.place(x = 50, y = 120)
    entry_hora_final = tk.Entry(configuracion)
    entry_hora_final.place(x = 150, y = 120)

    label_minutos_revision = tk.Label(configuracion, text="Minutos por revisión (20-60)")
    label_minutos_revision.place(x=50, y = 150)
    entry_minutos_revision = tk.Entry(configuracion)
    entry_minutos_revision.place(x=205, y = 150)

    label_dias_naturales_reinspeccion = tk.Label(configuracion, text="Cantidad máxima de días naturales para reinspección (1-60)")
    label_dias_naturales_reinspeccion.place(x = 50, y = 180)
    entry_dias_naturales_reinspeccion = tk.Entry(configuracion)
    entry_dias_naturales_reinspeccion.place(x = 370, y = 180)

    label_cantidad_fallas = tk.Label(configuracion, text="Cantidad de fallas para sacar al vehículo (> 0)")
    label_cantidad_fallas.place(x = 50, y= 210)
    entry_cantidad_fallas = tk.Entry(configuracion)
    entry_cantidad_fallas.place(x= 295, y= 210)

    label_cantidad_meses = tk.Label(configuracion, text= "Cantidad de meses para desplegar las citas disponibles (1-12)")
    label_cantidad_meses.place(x= 50, y= 240)
    entry_cantidad_meses = tk.Entry(configuracion)
    entry_cantidad_meses.place(x= 380, y= 240)

    label_porcentaje = tk.Label(configuracion, text= "Impuesto al valor agregado")
    label_porcentaje.place(x= 50, y= 270)
    entry_porcentaje = tk.Entry(configuracion)
    entry_porcentaje.place(x= 380, y= 270)

    #Tabla con cada tipo de automovil
    label = tk.Label(configuracion, text="", bd=1, relief="solid")
    label.place(x=50, y= 300)
    c = ["Automovil particular y vehiculo de carga liviana (menor o iguala 3500kg)",
        "Automovil particular y vehiculo de carga liviana (mayor a 3500kg, menor a 8000kg)",
        "Vehiculo de carga pesada y cabezales (mayor o iguala a 8000kg)",
        "Taxis",
        "Autobuses, buses y microbuses",
        "Motocicletas",
        "Equipo especial de obras",
        "Equipo especial agricola (maquinaria agricula)"
        ]
    for x in c:
        texto = label.cget("text")
        label.config(text=texto+x+"\n"+ "\n")

    #Entrys de cada uno de los automoviles
    lista_entrys_vehiculos = []
    salto = 300
    for x in range(8):
        entry = tk.Entry(configuracion)
        entry.place(x= 500, y= salto)
        lista_entrys_vehiculos.append(entry)
        salto += 31


    def validacion():
        global lineas, hora_inicio, hora_final, cant_fallas, cant_meses, dias_reinspeccion, minutos_revision, porcentaje, precios_vehiculos

        #Validaciones
        if entry_lineas.get() == "":
            lineas = 0
        else:
            valor = int(entry_lineas.get())
            if valor > 0 and valor < 26:
                lineas = valor
            else:
                return messagebox.showerror("Error", "No están en el rango indicado")
        
        #----------------------------------------------------------------------------------------------------------------------
        if entry_hora_inicio.get() == "":
            hora_inicio = 0
        else:    
            valor1 = int(entry_hora_inicio.get())
            if valor1 >= 0 and valor1 < 24:
                hora_inicio = valor1
            else:
                return messagebox.showerror("Error", "No están en el rango indicado")
        
        #----------------------------------------------------------------------------------------------------------------------
        if entry_hora_final.get() == "":
            hora_final = 0
        else:    
            valor2 = int(entry_hora_final.get())
            if valor2 > 0 and valor2 < 24 and valor2 >= valor1:
                hora_final = valor2
            else:
                return messagebox.showerror("Error", "No están en el rango indicado")
        
        #----------------------------------------------------------------------------------------------------------------------
        if entry_cantidad_fallas.get() == "":
            cant_fallas = 0
        else:    
            valor3 = int(entry_cantidad_fallas.get())
            if valor3 > 0 :
                cant_fallas = valor3
            else:
                return messagebox.showerror("Error", "No están en el rango indicado")
        
        #----------------------------------------------------------------------------------------------------------------------
        if entry_cantidad_meses.get() == "":
            cant_meses = 0
        else:    
            valor4 = int(entry_cantidad_meses.get()) 
            if valor4 > 0 and valor4 < 13:
                cant_meses = valor4
            else:
                return messagebox.showerror("Error", "No están en el rango indicado")

        #----------------------------------------------------------------------------------------------------------------------
        if entry_dias_naturales_reinspeccion.get() == "":
            dias_reinspeccion = 0
        else:    
            valor5 = int(entry_dias_naturales_reinspeccion.get())
            if valor5 > 0 and valor5 < 61:
                dias_reinspeccion = valor5
            else:
                return messagebox.showerror("Error", "No están en el rango indicado")
        
        #----------------------------------------------------------------------------------------------------------------------
        if entry_minutos_revision.get() == "":
            minutos_revision = 0
        else:    
            valor6 = int(entry_minutos_revision.get())
            if valor6 > 19 and valor6 < 61:
                minutos_revision = valor6
            else:
                return messagebox.showerror("Error", "No están en el rango indicado")
        
        #----------------------------------------------------------------------------------------------------------------------
        if entry_porcentaje.get() == "":
            porcentaje = 0
        else:    
            valor7 = float(entry_porcentaje.get())
            if valor7 >= 0 and valor7 < 21:
                porcentaje = valor7
            else:
                return messagebox.showerror("Error", "No están en el rango indicado")

        #----------------------------------------------------------------------------------------------------------------------
        #Si realizó cambios en los precios de los vehículos entonces se guardan en la lista
        for ind, valor in enumerate(precios_vehiculos):
            if lista_entrys_vehiculos[ind].get() != "":
                precios_vehiculos[ind] = int(lista_entrys_vehiculos[ind].get())


        #Se guarda la informacion en el archivo
        archivo_path = "Datos_configuracion.dat"
        if os.path.isfile(archivo_path):
            # Cargar la lista almacenada en el archivo
            with open(archivo_path, 'rb') as file:
                lista_original = pickle.load(file)

            # Modificar la lista según sea necesario
            datos_guardados = [lineas, hora_inicio, hora_final, cant_fallas, cant_meses, dias_reinspeccion, minutos_revision, porcentaje, precios_vehiculos]

            # Guardar la lista modificada en el archivo
            with open(archivo_path, 'wb') as file:
                pickle.dump(datos_guardados, file)
        else:
            #Se guardan los datos
            datos_guardados = [lineas, hora_inicio, hora_final, cant_fallas, cant_meses, dias_reinspeccion, minutos_revision, porcentaje, precios_vehiculos]
            with open(archivo_path, 'wb') as archivo:
                pickle.dump(datos_guardados, archivo)

        #Cuando se mete a la condicion de que si está creado el archivo es cuando se abre el programa por primera vez para poner los valores como predeterminados

    b_guardar = tk.Button(configuracion, text= "Guardar informacion", command= validacion)
    b_guardar.place(x= 50, y= 580)

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




