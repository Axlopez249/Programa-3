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
global arbol, diccionario

numero_cita = 0
tipo_cita = IntVar()
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
diccionario_fallas = {'1234': ('Prueba', 'Leve'), "4321": ("Prueba 2", "Grave")}
arbol = [['2023-06-16', (21, 0), 'abc1234', 'Reinspección', 'bmw', '2010', 'axel lopez', 'axelstevenlopezvega04@gmail.com', '927384', 'loaiza iglesia 200', 'Automovil particular y vehiculo de carga liviana (menor o iguala 3500kg)', 'PENDIENTE'], None, None]
precios_vehiculos = [10920, 14380, 14380, 11785, 14380, 7195, 14380, 6625]
lista_tipos_vehiculos = ["Automovil particular y vehiculo de carga liviana (menor o iguala 3500kg)",
                             "Automovil particular y vehiculo de carga liviana (mayor a 3500kg, menor a 8000kg)",
                             "Vehiculo de carga pesada y cabezales (mayor o iguala a 8000kg)",
                             "Taxis",
                             "Autobuses, buses y microbuses",
                             "Motocicletas",
                             "Equipo especial de obras",
                             "Equipo especial agricola (maquinaria agricula)"]
opcion_fechas = StringVar()


#Variables del tablero
placas_revision = []
colas_lista = [] 
for x in range(lineas):
    colas_lista.append([])

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
#Funcion que crea todo el menu para guardar una cita
#E: vacia. LLamada por el boton de programar cita
#S: Una cita creada
def crear_citas():

    citas = tk.Tk()
    citas.title("Programacion de citas")
    citas.geometry("900x750")

    #Crear acceso a las variables fuera de la funcion
    global numero_cita, tipo_cita, lista_tipos_vehiculos, opcion_fechas, vehiculos, texto_placa, texto_marca, texto_modelo, texto_propietario, texto_correo, texto_telefono, texto_direccion
    numero_cita += 1

    #Lista donde se guardarán todos los datos de la cita
    lista_cita = []

    

    #Titulo del numero de cita
    label_num_cita = tk.Label(citas, text = "Número de cita: " + str(numero_cita))
    label_num_cita.place(x = 10, y = 10)
    label_num_cita.config(font=("Arial", 15))

    #Solicitud de datos

    #Tipo de cita
    label_tipo_cita = tk.Label(citas, text = " Tipo de cita: ")
    label_tipo_cita.place(x = 100, y = 80)
    label_tipo_cita.config(font=("Arial", 10))
    t1 = tk.Radiobutton(citas, text="Primera vez", variable=tipo_cita, value=1, command=lambda : cambiar_tipo_cita(1))
    t2 = tk.Radiobutton(citas, text="Reinspección", variable=tipo_cita, value=2, command=lambda : cambiar_tipo_cita(2))
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
    for elemento in lista_tipos_vehiculos:
        vehiculos.insert(tk.END, elemento)
    vehiculos.place(x = 80, y = 180)

    #Botón necesario para guardar el dato

    boton_guardar_vehiculos = tk.Button(citas, text="Guardar selección", command=lambda : obtener_seleccion())
    boton_guardar_vehiculos.place(x=575, y=250)

    # Función que se ejecuta al hacer clic en el botón aceptar
#    def obtener_seleccion():
 #       seleccion = vehiculos.curselection()
  #      if seleccion:
   #         indice = seleccion[0]
    #        elemento = vehiculos.get(indice)
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
    #Toma el import del gmail y revisa la estrctura
    #E: un elemento string de email
    #S: true si el email es correcto
    def is_valid_email():
        from validate_email import validate_email
        email = texto_correo.get()
        is_valid = validate_email(email, verify=True)

        if is_valid == True:
            return messagebox.showinfo("Listo", "Correo electrónico guardado")
        else:
            texto_correo.config(text = " ")
            return messagebox.showinfo("Error", "Correo electrónico inválido")

    boton_verificar = tk.Button(citas, text="Verificar correo", command=lambda : is_valid_email())
    boton_verificar.place(x=350, y=450)

    
 
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
        global hora_final, hora_inicio, cant_meses, minutos_revision, estado, fechas, horas, fechas_dias, lista_horas_por_dia
        estado = 2
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
        acep_fecha = tk.Button(citas, text="Guardar fecha", width=10, command = lambda : obtener_fecha_automatica())
        acep_fecha.place(x = 130, y = 640)

        acep_hora = tk.Button(citas, text= "Guardar hora", width=10, command=lambda : obtener_hora_automatica())
        acep_hora.place(x = 430, y = 640)

        return
    #Esta funcion se llama cuando el usuario decide solicitar la cita de forma manual
    #E: Vacia
    #S: Validaciones de la fecha
    def opcion_manual():
        global estado, entry_fecha, entry_hora
        estado = 1
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

    #Botón que después vemos como lo acomodamos, pero va a guardar todos los datos en una lista

    boton_principal = tk.Button(citas, text="GUARDADO DE DATOS", command=lambda : realizar_funciones())
    boton_principal.place(x=650, y=375)
    #--------------------------------------------------------------------------

    """boton_aceptar = tk.Button(citas, text="" , width=10)
    boton_aceptar.place()"""


    citas.mainloop()

#Funciones necesarias en la opción de programar citas

#Función que compara el número que recibe cada cita y añade en el árbol binario según sea necesario
#Entradas: Árbol y cita
#Salidas: Árbol modificado
def insertar_en_arbol_binario(arbol, valor):
    if arbol is None:
        # Si el árbol está vacío, se crea un nuevo nodo con el valor dado
        arbol = [valor, None, None]
    else:
        if valor[0] < arbol[0][0]:
            # Si el valor es menor que el valor del nodo actual, se inserta en el subárbol izquierdo
            arbol[1] = insertar_en_arbol_binario(arbol[1], valor)
        else:
            # Si el valor es mayor o igual al valor del nodo actual, se inserta en el subárbol derecho
            arbol[2] = insertar_en_arbol_binario(arbol[2], valor)

    return arbol


#Función que obtiene lo que estén marcado en la listbox de fechas
#E: Vacia. Llamada por un boton de guardar
#S: El elemento seleccionado del listbox
def obtener_fecha_automatica():
    global elemento2
    seleccion = fechas.curselection()
    if seleccion:
        indice = seleccion[0]
        elemento2 = fechas.get(indice)
    return elemento2

#Función que obtiene lo que estén marcado en la listbox de horas
#E: Vacia. Llamada por un boton de guardar
#S: El elemento seleccionado del listbox
def obtener_hora_automatica():
    global elemento3
    seleccion = horas.curselection()
    if seleccion:
        indice = seleccion[0]
        elemento3 = horas.get(indice)
#        print(arbol)
    return elemento3

#Función que obtiene lo que esté marcado en la listbox de vehículos
#Entrada:
#Salida: Lo que esté marcado en la listbox
def obtener_seleccion():
    global elemento
    seleccion = vehiculos.curselection()
    if seleccion:
        indice = seleccion[0]
        elemento = vehiculos.get(indice)
    print(elemento)
    return elemento

#Funcion que hace las validaciones de cada elemento de la programacion de las citas
#E: la lista de informacion de la cita (nodo)
#S: True si todas las validaciones estan correctas o false de lo contrario
def validar(cita):
    #global validaciones
    validaciones = True
    if len(cita[2]) > 8 or len(cita[2]) < 1:
        validaciones = False
    if len(cita[4]) < 3 or len(cita[4]) > 15:
        validaciones = False
    if len(cita[5]) < 1 or len(cita[5]) > 15:
        validaciones = False
    if len(cita[6]) < 6 or len(cita[6]) > 40:
        validaciones = False
    if len(cita[8]) > 20:
        validaciones = False
    if len(cita[9]) < 10 or len(cita[9]) > 40:
        validaciones = False
    return validaciones

#Función asignada al botón principal, este botón guardará todos los datos en un futuro
#Guarda toda la informacion de la lista en el nodo del arbol por medio de otra funcion
#E: Vacia. Llamada por el boton de guardado
#S: La lista guardada en el nodo del arbol
def realizar_funciones():
    global arbol, elemento2, elemento3
#    print(elemento)
 #   print(texto_placa.get())
    placa = texto_placa.get()
  #  print(texto_marca.get())
    marca = texto_marca.get()
   # print(texto_modelo.get())
    modelo = texto_modelo.get()
    #print(texto_propietario.get())
    propietario = texto_propietario.get()
#    print(texto_correo.get())
    correo = texto_correo.get()
 #   print(texto_telefono.get())
    telefono = texto_telefono.get()
  #  print(texto_direccion.get())
    direccion = texto_direccion.get()

    estado_revision = "PENDIENTE"
    if estado == 1:
   #     print(entry_fecha.get())
        fecha_manual = entry_fecha.get()
    #    print(entry_hora.get())
        hora_manual = entry_hora.get()

        hora_s = int(hora_manual[:2])
        #print(hora_s)
        minutos_s = int(hora_manual[3:])
#        print(minutos_s)
        
        lista_cita = [ fecha_manual, (hora_s,minutos_s), placa, tipo_cita, marca, modelo, propietario, correo, telefono, direccion, elemento, estado_revision]


    elif estado == 2:


        hora_s = elemento3[0]
       # print(hora_s)
        minutos_s = elemento3[1]
        #print(minutos_s)

        lista_cita = [ elemento2, (hora_s,minutos_s), placa, tipo_cita, marca, modelo, propietario, correo, telefono, direccion, elemento, estado_revision]

    validaciones = validar(lista_cita)

    if validaciones == True:
        arbol_c = arbol
        arbol = insertar_en_arbol_binario(arbol_c, lista_cita)
        print(arbol)
        lista = revisar_contenido(arbol, lista_cita[2], None, None)
        print(lista)
        messagebox.showinfo("Validaciones", "La cita ha sido guardada exitosamente")
    else:
        messagebox.showerror("Validaciones", "Alguno de los datos ingresados es inválido")

    #El siguiente diccionario será utilizado para guardar información de uso recurrente
    #diccionario[placa] = []

#Función que cambia la variable tipo_cita entre 1 y 2
#Entradas: Numero 1 para primera vez o numero 2 para reinspección
#Salidas: Variable tipo_cita con un valor asociado
def cambiar_tipo_cita(tipo_de_cita):
    global tipo_cita
    if tipo_de_cita == 1:
        tipo_cita = "Primera vez"
    if tipo_de_cita == 2:
        tipo_cita = "Reinspección"

#La siguiente función sola será utilizada durante el desarrollo del proyecto, en este caso la utilizaré para ver que tiene una variable

def prueba():
    print(arbol)


#Función que recibirá el árbol, una placa, y 2 variables None, para poder buscar la placa en el árbol y retornar la lista con los datos
#Entradas: Árbol, string de placa, 2 variables None
#Salidas: Lista con la información de cita de una placa específica
#Manera de utilizarla: revisar_contenido(arbol, "230948709238409", None, None)
def revisar_contenido(lista, placa, lista_variable, lista_cita):
    for elemento in lista:
        if isinstance(elemento, list):
            lista_variable = elemento
            resultado = revisar_contenido(elemento, placa, lista_variable, lista_cita)
            if resultado is not None:
                return resultado
        else:
            if elemento == placa:
                return lista_variable
    
    return None


#Función que permitirá agregar una falla al nodo de una cita especifica
#Entradas: Árbol, placa a la que desea agregarle una falla, número de falla
#Salidas: Árbol modificado con el número de falla agregado
def modificar_elemento(lista, placa, falla):
    if isinstance(lista, list):
        for i in range(len(lista)):
            if isinstance(lista[i], list):
                modificar_elemento(lista[i], placa, falla)
            elif lista[i] == placa:
                if isinstance(lista[-1], list):
                    lista[-1].append(falla)
                else:
                    lista.append([falla])

#Funcion que actualiza la lista de informacion de una cita ubicada en el arbol
#E: El arbol, el elemento de busqueda, El indice donde se encuentra ese elemento en la lista de informacion y la lista de infromacion nueva con los datos actualizados
#S: La informacion de la cita actualizada dentro del arbol
def actualizar_lista(arbol, elemento_comparar, indice_comparar, nuevo_elemento):
    if arbol is None:
        return None
    
    for i in range(len(arbol)):
        if isinstance(arbol[i], list):
            if arbol[i][indice_comparar] == elemento_comparar:
                arbol[i] = nuevo_elemento
            else:
                arbol[i] = actualizar_lista(arbol[i], elemento_comparar, indice_comparar, nuevo_elemento)
    
    return arbol

def cancelar_citas():
    citas = tk.Tk()
    citas.title("Programacion de citas")
    citas.geometry("600x500")

    citas.mainloop()

#Funcion que ingresa una placa a la estacion (La ingresa a la cola de revisio)
#E: Vacia. Llamada por medio del boton del menu
#S: Se ingresa a la cola de revision
def ingreso_estacion():
    global arbol
    estacion = tk.Tk()
    estacion.title("Ingreso a la estación")
    estacion.geometry("600x500")

    #labels
    label_titulo = tk.Label(estacion, text= "INGRESO A LA ESTACION")
    label_titulo.place(x=50, y=50)

    label_cita = tk.Label(estacion, text= "Numero de cita")
    label_cita.place(x=100, y= 100)
    texto_cita = tk.Entry(estacion)
    texto_cita.place(x= 150, y= 100)

    label_placa = tk.Label(estacion, text = "Placa: ")
    label_placa.place(x = 100, y = 120)
    texto_placa = tk.Entry(estacion)
    texto_placa.place(x = 150, y = 120)

    #Funcion que trae toda la informacion de la cita de una placa y despliega toda la informacion en la pantalla
    #E:  Vacia
    #S: Impresion de la informacion de la lista
    def traer_informacion():

        from datetime import datetime
        from datetime import date

        global precios_vehiculos, lista_tipos_vehiculos, porcentaje, placas_revision, arbol, colas_lista

        placa = texto_placa.get()
        #Se trae la informacion
        lista_informacion = revisar_contenido(arbol, placa, None, None)
        fecha_cita = lista_informacion[0]
        hora_cita = lista_informacion[1]
        marca = lista_informacion[4]
        modelo = lista_informacion[5]
        propie = lista_informacion[6]
        tipo_vehi = lista_informacion[10]
        indice = lista_tipos_vehiculos.index(tipo_vehi)
        precio = precios_vehiculos[indice]
        

        #Se calcula el precio que toca
        valor_agregado = precio * (porcentaje/100)
        precio = precio + valor_agregado


        #Aquí se despliega todo en la pantalla
        label_marca = tk.Label(estacion, text= "Marca del vehículo     " + marca)
        label_marca.place(x= 100, y= 175)

        label_modelo = tk.Label(estacion, text= "Modelo del vehículo     " + modelo)
        label_modelo.place(x= 100, y= 200)

        label_propie = tk.Label(estacion, text= "Propietario del vehículo     " + propie)
        label_propie.place(x= 100, y= 220)

        label_costo = tk.Label(estacion, text= "Costo del ingreso     " + str(precio))
        label_costo.place(x= 100, y= 240)

        #Saco la fecha del sistema para compararlo con la fecha de la cita
        #Tambien la hora para ver que hay por lo menos 1 hora antes que la de la cita
        # Obtener la hora actual
        hora_actual = datetime.now().time()

        # Obtener solo las horas y minutos
        horas = int(hora_actual.strftime('%H'))
        minutos = int(hora_actual.strftime('%M'))

        #Parte donde se comparan las horas
        minutos_cita = (int(hora_cita[0])*60) + int(hora_cita[1])-60
        minutos_actuales = ((horas*60) + minutos)

        


        #Se valida que esté 60 minutos antes
        if minutos_actuales < minutos_cita:
            fecha_actual = date.today()

            if fecha_actual == fecha_cita:
                messagebox.showinfo("Cita", "La cita está lista para el ingreso a la estación")
        else:
            return messagebox.showerror("Cita", "La cita no se encuentra 60 minutos antes")
        
        #Se valida que esté en pendiente
        estado_revision = lista_informacion[-1]
        if estado_revision != "PENDIENTE":
            return messagebox.showerror("Cita", "La cita no se encuentra en estado PENDIENTE")
        
        #Funcion para agregar la placa a la cola
        for placas in placas_revision:
            if placas[0] == placa:
                return messagebox.showerror("ERROR", "La placa ya está en cola de revisión")
            
        for fila in colas_lista:
            for col in fila:
                if col[0] == placa:
                    return messagebox.showerror("ERROR", "La placa ya está en cola de espera en una línea")
            
        placas_revision.append([placa,0])

        
        archivo_path = "Datos_tablero.dat"
        if os.path.isfile(archivo_path):
            # Abre el archivo en modo lectura binaria
            with open(archivo_path, 'rb') as archivo:
                # Carga los datos del archivo pickle
                datos_guardados = pickle.load(archivo)
            datos_guardados[2] = placas_revision

            archivo_path = "Datos_tablero.dat"
            with open(archivo_path, 'wb') as archivo:
                pickle.dump(datos_guardados, archivo)

        return 

        

        #Se agrega toda la información
    b_aceptar = tk.Button(estacion, text= "Traer información", command= traer_informacion)
    b_aceptar.place(x= 100, y= 145)

    

    estacion.mainloop()

def tablero():

    global placas_revision, lineas, colas_lista, cant_fallas
    table = tk.Tk()
    table.geometry("800x500")
    #Se crean las colas de cada linea

    #Se crean los labels
    salto = 100
    for x in range(lineas):
        label = tk.Label(table, text=str(x+1))
        label.place(x = 100, y = salto)
        salto += 30

    #Imprimir puestos
    puestos = ["Puesto 1", "Puesto 2","Puesto 3","Puesto 4","Puesto 5",]
    espaciado = 120
    for x in range(5):
        label = tk.Label(table, text=puestos[x])
        label.place(x = espaciado, y = 75)
        espaciado += 120

    lista_labels = []
    salto = 100
    for fila in range(lineas):
        sublista = []
        espaciado = 120
        for columna in range(5):
            label = tk.Label(table, text = "")
            label.place(x = espaciado, y = salto)
            sublista.append(label)
            espaciado += 120
        salto += 30
        lista_labels.append(sublista)


    #Funcion que genera los pdf
    def resultado_revision(lista):
        import webbrowser as wb
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication 
        from fpdf import FPDF

        #Orientacion de la hoja y el tipo
        #En unit va la forma de medida de la hoja
        pdf = FPDF(orientation = "P", unit = "mm", format="A4")

        #Se agrega la pagina
        pdf.add_page()

        #Se agregan los elementos a la pagina
        pdf.line(20, 20, 190, 20)

        #Tipo de letra
        pdf.set_font("Arial", "", 11)

        pdf.text(x = 20, y = 50, txt = ("Resultado de la revisión del vehículo      "))
        pdf.text(x = 20, y = 60, txt = ("Fecha de la cita  " + lista[0]))
        pdf.text(x = 20, y = 70, txt = ("Hora de la cita  " + str(lista[1])))
        pdf.text(x = 20, y = 80, txt = ("Placa  " + lista[2]))
        pdf.text(x = 20, y = 90, txt = ("Tipo de cita  " + lista[3]))
        pdf.text(x = 20, y = 100, txt = ("Marca  " + lista[4]))
        pdf.text(x = 20, y = 110, txt = ("Modelo  " + lista[5]))
        pdf.text(x = 20, y = 120, txt = ("Propietario  " + lista[6]))
        pdf.text(x = 20, y = 130, txt = ("Correo  " + lista[7]))
        pdf.text(x = 20, y = 140, txt = ("Teléfono  " + lista[8]))
        pdf.text(x = 20, y = 150, txt = ("Dirección  " + lista[9]))
        pdf.text(x = 20, y = 160, txt = ("Tipo de vehículo  " + lista[10]))
        pdf.text(x = 20, y = 170, txt = ("Estado de la cita  " + lista[11]))
        pdf.text(x = 20, y = 180, txt = ("Fallas  " ))
        pdf.text(x = 20, y = 190, txt = ("Número                                        Descripcion                                               Tipo" ))
        #Fallas
        y = 200
        if isinstance(lista[-1], list) == True:
            lista_fallas = lista[-1]
            for falla in lista_fallas:
                tupla = diccionario_fallas[falla]

                pdf.text(x = 20, y = y, txt = (falla + "                                               " + tupla[0] + "                                                    " + tupla[1]))
                y += 10
        
            
        pdf.output("Resultado_revision.pdf")



        #Se envía al correo electrónico
        # create message object instance
        msg = MIMEMultipart()
        message = "Buenas. La informacion de su cita"
        msg.attach(MIMEText(message, 'plain'))
        # setup the parameters of the message 
        password = "nzewymngmujkfzkv"
        msg['From'] = "reteve90@gmail.com"
        msg['To'] = lista[7]
        msg['Subject'] = "Informacion cita RETEVE"
            # add in the message body 
        with open('Resultado_revision.pdf', 'rb') as f:
            pdf_data = f.read()
        pdf_part = MIMEApplication(pdf_data, 'pdf', Name='Resultado_revision.pdf')
        pdf_part['Content-Disposition'] = 'attachment; filename = "Resultado_revision.pdf"'
        msg.attach(pdf_part)
            #create server 
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
            # Login Credentials for sending the mail 
        server.login(msg['From'], password)
            # send the message via the server. 
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        return
    


    def certificado_transito(lista):
        import webbrowser as wb
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication 
        from fpdf import FPDF

        #Orientacion de la hoja y el tipo
        #En unit va la forma de medida de la hoja
        pdf = FPDF(orientation = "P", unit = "mm", format="A4")

        #Se agrega la pagina
        pdf.add_page()

        #Se agregan los elementos a la pagina
        pdf.line(20, 20, 190, 20)

        #Tipo de letra
        pdf.set_font("Arial", "", 11)

    #Calculo de la vigencia del certificado
        fecha_cita = lista[0]
        fecha_vigencia = fecha_cita + datetime.timedelta(days=365)

        pdf.text(x = 20, y = 50, txt = ("Certificado de tránsito     "))
        pdf.text(x = 20, y = 60, txt = ("Placa:  " + lista[2]))
        pdf.text(x = 20, y = 70, txt = ("Marca:  " + lista[4]))
        pdf.text(x = 20, y = 80, txt = ("Propietario:  " + lista[6]))
        pdf.text(x = 20, y = 90, txt = ("Tipo de vehículo:  " + lista[10]))
        pdf.text(x = 20, y = 100, txt = ("Vigencia del certificado de tránsito:  " + fecha_vigencia))

        
        

        
            
        pdf.output("certificado_transito.pdf")



        #Se envía al correo electrónico
        # create message object instance
        msg = MIMEMultipart()
        message = "Buenas. La informacion de su cita"
        msg.attach(MIMEText(message, 'plain'))
        # setup the parameters of the message 
        password = "nzewymngmujkfzkv"
        msg['From'] = "reteve90@gmail.com"
        msg['To'] = lista[7]
        msg['Subject'] = "Informacion cita RETEVE"
            # add in the message body 
        with open("certificado_transito.pdf", 'rb') as f:
            pdf_data = f.read()
        pdf_part = MIMEApplication(pdf_data, 'pdf', Name='certificado_transito.pdf')
        pdf_part['Content-Disposition'] = 'attachment; filename = "certificado_transito.pdf"'
        msg.attach(pdf_part)
            #create server 
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
            # Login Credentials for sending the mail 
        server.login(msg['From'], password)
            # send the message via the server. 
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        return
    #Funciones de los comandos
    def comando_U(placa):
        #Se busca entre todos los labels para encontrar la placa y preguntar por el siguiente
        for ind_f, fila in enumerate(lista_labels):
            for ind_c, col in enumerate(fila):
                if col.cget("text") == placa:
                    if ind_c == 4:
                        return messagebox.ERROR("Error", "La placa se encuentra en la posicion 5. No se puede usar este comando")
                    if lista_labels[ind_f][ind_c+1].cget("text") == "":
                        lista_labels[ind_f][ind_c+1].config(text = placa)

                        if lista_textos[ind_f][ind_c][-1] == ".":
                            lista_textos[ind_f][ind_c+1] = lista_textos[ind_f][ind_c]
                            lista_textos[ind_f][ind_c] = ""
                            lista_labels[ind_f][ind_c+1].config(bg = "red")
                            lista_labels[ind_f][ind_c].config(text = "")
                            lista_labels[ind_f][ind_c].config(bg = "#C0C0C0")
                        else:
                            lista_textos[ind_f][ind_c+1] = placa
                            lista_textos[ind_f][ind_c] = ""
                            lista_labels[ind_f][ind_c].config(text = "")

                        #Se busca la placa en la cola de revision para modificarla
                        for placas in placas_revision:
                            if placas[0] == placa:
                                placas[1] += 1

                        #Se busca la lista colas de la fila, para que ingrese a el primer puesto
                        #Se pregunta esto si la placa que se movió estaba en la posicion 
                        # 
                        
                        if ind_c == 0 and len(colas_lista[ind_f]) > 0:
                            placa_ingresada = colas_lista[ind_f][0]
                            del colas_lista[ind_f][0]
                            placa_ingresada[1] += 1
                            placas_revision.append(placa_ingresada)
                            lista_labels[ind_f][ind_c].config(text = placa_ingresada[0])

                        #Se guardan los datos
                        
                        datos_guardados = [lista_textos, colas_lista, placas_revision]
                        archivo_path = "Datos_tablero.dat"
                        with open(archivo_path, 'wb') as archivo:
                            pickle.dump(datos_guardados, archivo)
                        return
                    else:
                        return messagebox.showerror("Error", "El siguiente puesto está ocupado")
                    
        
                    
    def comando_T(placa):
        for ind_f, fila in enumerate(lista_labels):
            for ind_c, col in enumerate(fila):
                if col.cget("text") == placa:
                    contador = 3
                    while contador >= 0:
                        if lista_labels[ind_f][contador].cget("text") != "":
                            if lista_labels[ind_f][contador+1].cget("text") == "":
                                placa =  lista_labels[ind_f][contador].cget("text")

                                #Se actualiza la lista de textos
                                if lista_textos[ind_f][contador][-1] == ".":
                                    lista_textos[ind_f][contador+1] = lista_textos[ind_f][contador]
                                    lista_textos[ind_f][contador] = ""
                                    lista_labels[ind_f][contador]
                                    lista_labels[ind_f][contador+1].config(bg = "red")
                                    lista_labels[ind_f][contador].config(bg = "#C0C0C0")
                                else:
                                    lista_textos[ind_f][contador+1] = placa
                                    lista_textos[ind_f][contador] = ""
                                    

                                #Se actualiza la cola de revision
                                #se busca la placa
                                for placas in placas_revision:
                                    if placas[0] == placa:
                                        placas[1] += 1

                                lista_labels[ind_f][contador+1].config(text = placa)
                                lista_labels[ind_f][contador].config(text = "")
                        contador -= 1

                    #Se busca la lista colas de la fila, para que ingrese a el primer puesto
                    #Se pregunta esto si la placa que se movió estaba en la posicion 1
                    
                    if ind_c == 0 and len(colas_lista[ind_f]) > 0:
                        placa_ingresada = colas_lista[ind_f][0]
                        del colas_lista[ind_f][0]
                        placa_ingresada[1] += 1
                        placas_revision.append(placa_ingresada)
                        lista_labels[ind_f][ind_c].config(text = placa_ingresada[0])
                    #Se guardan los datos
                        
                    datos_guardados = [lista_textos, colas_lista, placas_revision]
                    archivo_path = "Datos_tablero.dat"
                    with open(archivo_path, 'wb') as archivo:
                        pickle.dump(datos_guardados, archivo)
                    return
                
    def comprobacion_comando(comando):
        coman = comando[0]
        placa = comando[1:]
        if coman == "E":
            placa = comando[1:-4]
            falla = comando[-4:]
            #Se tiene que comprobar que el numero de la falla exista
            if not falla in diccionario_fallas:
                return messagebox.showerror("Error", "La falla establecida no existe")
            
            #Se continua con el proceso
            tupla_informacion = diccionario_fallas[falla]
            tipo_falla = tupla_informacion[1]
            if tipo_falla == "Grave":
                #Se recorre la lista de labels
                for ind_f,fila in enumerate(lista_labels):
                    for ind_c,col in enumerate(fila):
                        if col.cget("text") == placa:
                            
                            col.config(bg="red")
                            #Se usa la funcion para agregar la falla al nodo de la cita
                            modificar_elemento(arbol, placa, falla)
                            lista_textos[ind_f][ind_c] += "."

                            lista = revisar_contenido(arbol, placa, None, None)
                            print(lista)
            else:
                modificar_elemento(arbol, placa, falla)

            datos_guardados = [lista_textos, colas_lista, placas_revision]
            archivo_path = "Datos_tablero.dat"
            with open(archivo_path, 'wb') as archivo:
                pickle.dump(datos_guardados, archivo)

            return
        
        for placas in placas_revision:
            if placas[0] == placa:
                if coman == "U":
                    #Se realizan las validaciones
                    #Se verifica que la placa no esté en el puesto 5
                    for fila in lista_labels:
                        for ind, col in enumerate(fila):
                            if col.cget("text") == placa:
                                if ind == 4:
                                    return messagebox.showerror("Error", "La placa se encuentra en la posicion 5. No se puede usar este comando")

                    comando_U(placa)
                if coman == "T":
                    #Se realizan las validaciones
                    #Se verifica que la placa no esté en el puesto 5
                    for fila in lista_labels:
                        for ind, col in enumerate(fila):
                            if col.cget("text") == placa:
                                if ind == 4:
                                    return messagebox.showerror("Error", "La placa se encuentra en la posicion 5. No se puede usar este comando")
                    comando_T(placa)
                if coman == "F":
                    #Se realizan las validaciones
                    #Se verifica que la placa no esté en el puesto 5
                    for fila in lista_labels:
                        for ind, col in enumerate(fila):
                            if col.cget("text") == placa:
                                if ind == 4:
                                    #se tiene que quitar del puesto 5 y
                                    for ind_f, fila in enumerate(lista_labels):
                                        for ind_c, col in enumerate(fila):
                                            if col.cget("text") == placa:
                                                if lista_textos[ind_f][ind_c][-1] == ".":
                                            
                                                    lista_textos[ind_f][ind_c] = ""
                                                    lista_labels[ind_f][ind_c].config(text = "")
                                                    lista_labels[ind_f][ind_c].config(bg = "#C0C0C0")

                                                    #Se verifica lo de las fallas para actualizar 
                                                    #Primero se trae la lista de la informacion
                                                    lista_informacion = revisar_contenido(arbol, placa, None, None)
                                                    if isinstance(lista_informacion[-1], list) == False:
                                                        #Hay que cambiar el estado a aprobada
                                                        lista_informacion[-1] = "APROBADA"
                                                        actualizar_lista(arbol, placa, 2, lista_informacion)

                                                        #se llaman las funciones para los pdf
                                                        lista_informacion = revisar_contenido(arbol, placa, None, None)
                                                        resultado_revision(lista_informacion)
                                                        certificado_transito(lista_informacion)
                                                        for ind, placas in enumerate(placas_revision):
                                                            if placas[0] == placa:
                                                                del placas_revision[ind]

                                                        return messagebox.showinfo("Info", "El vehículo ha sido aprobado. Tendrá los documentos por correo")
                                                    

                                                    lista_fallas = lista_informacion[-1]

                                                    cantidad_g = 0
                                                    cantidad_l = 0
                                                    for falla in lista_fallas:
                                                        tupla_info = diccionario_fallas[falla]
                                                        tipo_fall = tupla_info[1]
                                                        if tipo_fall == "Leve":
                                                            cantidad_l += 1
                                                        elif tipo_fall == "Grave":
                                                            cantidad_g += 1
                                                    
                                                    #Segun la cantidad de fallas leves y graves se cambia el estado de la cita o del vehiculo
                                                    if cantidad_g == 0:
                                                        #Hay que cambiar el estado a aprobada
                                                        lista_informacion[11] = "APROBADA"
                                                        actualizar_lista(arbol, placa, 2, lista_informacion)

                                                        #se llaman las funciones para los pdf
                                                        resultado_revision(placa)
                                                        certificado_transito(placa)
                                                        for ind, placas in enumerate(placas_revision):
                                                            if placas[0] == placa:
                                                                del placas_revision[ind]

                                                        return messagebox.showinfo("Info", "El vehículo ha sido aprobado. Tendrá los documentos por correo")
                                                    elif cantidad_g >= 1 and cantidad_g < cant_fallas:
                                                        #Hay que cambiar el estado a aprobada
                                                        lista_informacion[11] = "REINSPECCION"
                                                        actualizar_lista(arbol, placa, 2, lista_informacion)

                                                        #se llaman las funciones para los pdf
                                                        resultado_revision(placa)
                                                        for ind, placas in enumerate(placas_revision):
                                                            if placas[0] == placa:
                                                                del placas_revision[ind]

                                                        return messagebox.showinfo("Info", "El vehículo ha sido enviado a reinspeccion. Tendrá los documentos por correo")
                                                    elif cantidad_g >=  cant_fallas:
                                                        #Hay que cambiar el estado a aprobada
                                                        lista_informacion[11] = "SACAR DE CIRCULACION"
                                                        actualizar_lista(arbol, placa, 2, lista_informacion)

                                                        #se llaman las funciones para los pdf
                                                        resultado_revision(placa)
                                                        for ind, placas in enumerate(placas_revision):
                                                            if placas[0] == placa:
                                                                del placas_revision[ind]

                                                        return messagebox.showinfo("Info", "El vehículo se ha sacado de circulación. Tendrá los documentos por correo")
                                                else:
                                                    lista_textos[ind_f][ind_c] = ""
                                                    lista_labels[ind_f][ind_c].config(text = "")

                                                    #Se verifica lo de las fallas para actualizar 
                                                    #Primero se trae la lista de la informacion
                                                    lista_informacion = revisar_contenido(arbol, placa, None, None)
                                                    if isinstance(lista_informacion[-1], list) == False:
                                                        #Hay que cambiar el estado a aprobada
                                                        lista_informacion[-1] = "APROBADA"
                                                        actualizar_lista(arbol, placa, 2, lista_informacion)

                                                        #se llaman las funciones para los pdf
                                                        lista_informacion = revisar_contenido(arbol, placa, None, None)
                                                        resultado_revision(lista_informacion)
                                                        certificado_transito(lista_informacion)
                                                        for ind, placas in enumerate(placas_revision):
                                                            if placas[0] == placa:
                                                                del placas_revision[ind]

                                                        return messagebox.showinfo("Info", "El vehículo ha sido aprobado. Tendrá los documentos por correo")
                                                    

                                                    lista_fallas = lista_informacion[-1]

                                                    cantidad_g = 0
                                                    cantidad_l = 0
                                                    for falla in lista_fallas:
                                                        tupla_info = diccionario_fallas[falla]
                                                        tipo_fall = tupla_info[1]
                                                        if tipo_fall == "Leve":
                                                            cantidad_l += 1
                                                        elif tipo_fall == "Grave":
                                                            cantidad_g += 1
                                                    
                                                    #Segun la cantidad de fallas leves y graves se cambia el estado de la cita o del vehiculo
                                                    if cantidad_g == 0:
                                                        #Hay que cambiar el estado a aprobada
                                                        lista_informacion[11] = "APROBADA"
                                                        actualizar_lista(arbol, placa, 2, lista_informacion)

                                                        #se llaman las funciones para los pdf
                                                        resultado_revision(placa)
                                                        certificado_transito(placa)
                                                        for ind, placas in enumerate(placas_revision):
                                                            if placas[0] == placa:
                                                                del placas_revision[ind]

                                                        return messagebox.showinfo("Info", "El vehículo ha sido aprobado. Tendrá los documentos por correo")
                                                    elif cantidad_g >= 1 and cantidad_g < cant_fallas:
                                                        #Hay que cambiar el estado a aprobada
                                                        lista_informacion[11] = "REINSPECCION"
                                                        actualizar_lista(arbol, placa, 2, lista_informacion)

                                                        #se llaman las funciones para los pdf
                                                        resultado_revision(placa)
                                                        for ind, placas in enumerate(placas_revision):
                                                            if placas[0] == placa:
                                                                del placas_revision[ind]

                                                        return messagebox.showinfo("Info", "El vehículo ha sido enviado a reinspeccion. Tendrá los documentos por correo")
                                                    elif cantidad_g >=  cant_fallas:
                                                        #Hay que cambiar el estado a aprobada
                                                        lista_informacion[11] = "SACAR DE CIRCULACION"
                                                        actualizar_lista(arbol, placa, 2, lista_informacion)

                                                        #se llaman las funciones para los pdf
                                                        resultado_revision(placa)
                                                        for ind, placas in enumerate(placas_revision):
                                                            if placas[0] == placa:
                                                                del placas_revision[ind]

                                                        return messagebox.showinfo("Info", "El vehículo se ha sacado de circulación. Tendrá los documentos por correo")

                                else:
                                    return messagebox.showerror("Error", "La placa no se encuentra en la posicion 5. No se puede usar este comando")

                    comando_T(placa)
                    
                    #comando_F(placa)
                


    archivo_path = "Datos_tablero.dat"
    if os.path.isfile(archivo_path):

        # Abre el archivo en modo lectura binaria
        with open(archivo_path, 'rb') as archivo:
            # Carga los datos del archivo pickle
            datos_guardados = pickle.load(archivo)

        #Se pintan los labels con los guardados
        lista_textos_modificados = datos_guardados[0]
        colas_lista = datos_guardados[1]
        placas_revision = datos_guardados[2]

        for fila in range(len(lista_labels)):
            for col in range(len(lista_labels[0])):
                texto = lista_textos_modificados[fila][col]
                if len(texto)>2 and texto[-1] == ".":
                    lista_labels[fila][col].config(bg = "red")
                    lista_labels[fila][col].config(text = texto[:-1])
                else:
                    lista_labels[fila][col].config(text = texto)

        #Aqui se recorre la lista de revisiones 
        #Se usa el proceso con aquellos que tienen 0
        for linea in lista_labels:
            if linea[0].cget("text") == "":
                for placa in placas_revision:
                    if placa[1] == 0:
                        linea[0].config(text=placa[0])
                        placa[1] += 1
                        break
                

        #Se recorre la lista de vehiculos en revision para ver 
        #si hay alguno que sea igual a 0
        #Despues se evalua cual lista tiene menos espacios libres
        for carro in placas_revision:
            if carro[1] == 0:
                #Se verifica cuál línea está más vacía
                #Se saca una lista y en ella van las cantidades de espacios vacíos en cada linea
                #Para ello se recorre cada fila de la lista de labels y se suma si hay un espacio vacío
                #Cuando se termina de recorrer cada fila, entonces se agrega su suma
                lista_sumas = []
                for fila in range(len(lista_labels)):
                    suma_fila = 0
                    for colu in range(len(lista_labels[0])):
                        if lista_labels[fila][colu].cget("text") == "":
                            suma_fila += 1
                    lista_sumas.append(suma_fila)

                #Aqui se agrega a la cola de la linea correspondiende
                #Se agrega el vehículo, para posteriormente poder hacer los procesos correspondientes de los comandos
                linea_desocupada = lista_sumas.index(min(lista_sumas))
                colas_lista[linea_desocupada].append([carro[0], 0])

        #Se crea la lista con los textos de los labels
        lista_textos = []
        for fila in lista_labels:
            sublista = []
            for col in fila:
                texto = col.cget("text")
                sublista.append(texto)
            lista_textos.append(sublista)
        

        label_coman = tk.Label(table, text="COMANDO ")
        label_coman.place(x=100, y = 300)
        entry_coman = tk.Entry(table)
        entry_coman.place(x=168, y=300)

        
        b_aceptar = tk.Button(table, text= "Aceptar", command= lambda: comprobacion_comando(entry_coman.get()))
        b_aceptar.place(x=100, y=320)

        

    else:
        #Aqui se recorre la lista de revisiones 
        #Se usa el proceso con aquellos que tienen 0
        for linea in lista_labels:
            if linea[0].cget("text") == "":
                for placa in placas_revision:
                    if placa[1] == 0:
                        linea[0].config(text=placa[0])
                        placa[1] += 1
                        break
                


        #Se recorre la lista de vehiculos en revision para ver 
        #si hay alguno que sea igual a 0
        #Despues se evalua cual lista tiene menos espacios libres
        for carro in placas_revision:
            if carro[1] == 0:
                #Se verifica cuál línea está más vacía
                #Se saca una lista y en ella van las cantidades de espacios vacíos en cada linea
                #Para ello se recorre cada fila de la lista de labels y se suma si hay un espacio vacío
                #Cuando se termina de recorrer cada fila, entonces se agrega su suma
                lista_sumas = []
                for fila in range(len(lista_labels)):
                    suma_fila = 0
                    for colu in range(len(lista_labels[0])):
                        if lista_labels[fila][colu].cget("text") == "":
                            suma_fila += 1
                    lista_sumas.append(suma_fila)

                #Aqui se agrega a la cola de la linea correspondiende
                #Se agrega el vehículo, para posteriormente poder hacer los procesos correspondientes de los comandos
                linea_desocupada = lista_sumas.index(min(lista_sumas))
                colas_lista[linea_desocupada].append([carro[0], 0])


        #Se crea la lista con los textos de los labels
        lista_textos = []
        for fila in lista_labels:
            sublista = []
            for col in fila:
                texto = col.cget("text")
                sublista.append(texto)
            lista_textos.append(sublista)



        label_coman = tk.Label(table, text="COMANDO ")
        label_coman.place(x=100, y = 300)
        entry_coman = tk.Entry(table)
        entry_coman.place(x=168, y=300)


        b_aceptar = tk.Button(table, text= "Aceptar", command= lambda: comprobacion_comando(entry_coman.get()))
        b_aceptar.place(x=100, y=320)



        #Se guardan los datos
        datos_guardados = [lista_textos, colas_lista, placas_revision]
        archivo_path = "Datos_tablero.dat"
        with open(archivo_path, 'wb') as archivo:
            pickle.dump(datos_guardados, archivo)


    table.mainloop()

#Diccionario donde se guardarán las fallas



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




