# -----------------------------------------------------------------------------
#
# HorarioApp
#
# Desarrollado por: Benjamin Pavez
#
# Fecha Inicio: 28-12-2024
#
# Fecha Ultima Modificacion: 06-01-2025
#
# Versión: 0.1
#
# Licence: MIT License
#
# Este código fuente corresponde a la aplicacion HorarioApp, representa 
# un prototipo, para mas informacion revisar el README.
#
# El código fuente se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
# APTITUD PARA UN PROPÓSITO PARTICULAR.
#
# DESCRIPCIÓN:
# Programa principal de HorarioApp (main.py).
#
# -----------------------------------------------------------------------------
from customtkinter import *
from tkinter import messagebox
from CTkListbox import *
from CTkTable import *
import tkinter as tk
from copy import deepcopy

#DATAFRAME
Dataframe = [
    ["Bloque", "Hora", "Lunes" ,"Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"],
    ["1-2", "08:15 - 09:25", "-", "-", "-", "-", "-", "-", "-"],
    ["3-4", "09:40 - 10:50", "-", "-", "-", "-", "-", "-", "-"],
    ["5-6", "11:05 - 12:15", "-", "-", "-", "-", "-", "-", "-"],
    ["7-8", "12:30 - 13:40", "-", "-", "-", "-", "-", "-", "-"],
    ["9-10", "14:40 - 15:50", "-", "-", "-", "-", "-", "-", "-"],
    ["11-12", "16:05 - 17:15", "-", "-", "-", "-", "-", "-", "-"],
    ["13-14", "17:30 - 18:40", "-", "-", "-", "-", "-", "-", "-"],
    ["15-16", "18:50 - 20:00", "-", "-", "-", "-", "-", "-", "-"],
    ["17-18", "20:15 - 21:25", "-", "-", "-", "-", "-", "-", "-"],
    ["19-20", "21:40 - 22:50", "-", "-", "-", "-", "-", "-", "-"]
]

#-----------------------------------------------------------------------------Variables globales-----------------------------------------------------------------------------
topes_problem = [] #DEJAR VACIO
semestre = "2025-1" #USAR NOTACION 2025-1 como por ejemplo
nombre_carrera = "Ingeniería Civil en Informática"
numero_ramos = 7
#Escribe aqui tus ramos obligatorios, tiene que ser igual o menor al numero de ramos
obligatorios = ["Computacion Cientifica", "Gestion de Proyectos Informaticos", "Inteligencia Artificial", "Sistemas Distribuidos"]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Interfaz Gráfica
class HorarioSeleccionado(CTk):
    #Constructor
    def __init__(self, wea, topes_problem, horario, num):
        super().__init__()

        self.geometry("1000x800")
        self.title(f"HorarioApp - Horario #{num+1}")
        self.configure(bg="#2b2b2b")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=3)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=3)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=2)
        self.columnconfigure(0, weight=1)

        title_label = CTkLabel(self, text=f"Horario {semestre} - {nombre_carrera}",
                               text_color="white", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, pady=10, sticky="n")

        topes_label = CTkLabel(self, text=f"Cantidad de Topes: {len(topes_problem)}",
                               font=("Helvetica", 12))
        topes_label.grid(row=1, column=0, pady=10, sticky="n")

        frametabla = CTkFrame(master=self, corner_radius=10)
        frametabla.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        table = CTkTable(frametabla, row=11, column=9, values=wea, width=130, height=10, corner_radius=10)
        table.pack(expand=True, fill="both", padx=10, pady=10)

        asignaturas_label = CTkLabel(self, text="Asignaturas", font=("Helvetica", 12))
        asignaturas_label.grid(row=3, column=0, pady=10, sticky="n")

        asignaturas_frame = CTkFrame(self, corner_radius=10)
        asignaturas_frame.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        for i in horario:
            CTkLabel(asignaturas_frame, text=f"{i}",
                     font=("Helvetica", 12)).pack(anchor="w", padx=10)

        topes_label = CTkLabel(self, text="Topes", font=("Helvetica", 12))
        topes_label.grid(row=5, column=0, pady=10, sticky="n")

        topes_frame = CTkFrame(self, corner_radius=10)
        topes_frame.grid(row=6, column=0, padx=20, pady=10, sticky="nsew")

        for ramo1, ramo2 in topes_problem:
            CTkLabel(topes_frame, text=f"El ramo {ramo1} topa con {ramo2}",
                     font=("Helvetica", 12)).pack(anchor="w", padx=10)



#Interfaz Gráfica
class Horario(CTk):
    def __init__(self, horarios_optimos):
        super().__init__()
        self.geometry("970x800")
        self.title("HorarioApp")
        self.configure(bg="#2b2b2b")

        self.horarios_optimos = horarios_optimos

        CTkLabel(self, text="Horarios Óptimos", text_color="white", font=("Helvetica", 16)).grid(row=0, column=0, pady=10, sticky="n")

        self.listbox = CTkListbox(self, height=600, width=900)
        self.listbox.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        for idx, horario in enumerate(horarios_optimos, start=1):
            rams = ""
            for ramo in horario:
                rams += f"({ramo.sigla}-{ramo.paralelo}) "
            self.listbox.insert(tk.END, f"Horario #{idx} - Ramos: {rams}")

        CTkButton(self, text="Mostrar Detalles", command=self.mostrar_detalles).grid(row=2, column=0, pady=10)

        guardar_horarios_txt(horarios_optimos)

    #Muestra los detalles del horario seleccionado en una ventana emergente con una tabla.
    def mostrar_detalles(self):
        seleccionado = self.listbox.curselection() 
        if isinstance(seleccionado, int):
            idx = seleccionado
        elif seleccionado:
            idx = seleccionado[0]
        else:
            messagebox.showwarning("Advertencia", "No has seleccionado ningún horario.")
            return

        horario = self.horarios_optimos[idx] 

        data_copy = deepcopy(Dataframe)
        Topes(horario, data_copy, idx)



#Clase Ramo
class Ramo:
    def __init__(self, nombre, sigla, paralelo, horario):
        self.nombre = nombre
        self.sigla = sigla
        self.paralelo = paralelo
        self.horario = horario

    def __str__(self):
        return f"{self.nombre} ({self.sigla}) - Paralelo {self.paralelo} - {self.horario}"

    def __repr__(self):
        return f"{self.nombre} ({self.sigla}) - Paralelo {self.paralelo} - {self.horario}"



'''
La funcion genera todas las combinaciones de horarios con n ramos, considerando ramos obligatorios y guarda los que tienen la menor cantidad de topes.

    Parametros:
        data (list): Lista de ramos disponibles.
        horario_actual (list): Lista de ramos seleccionados actualmente.
        obligatorios (list): Lista con nombres de ramos obligatorios.
        mejor_horario (list): Lista de los mejores horarios encontrados hasta ahora.
        min_topes (float): Cantidad mínima de topes encontrada.


    Retorno:
        La funcion retorna una lista de horarios con la menor cantidad de topes.
'''
def ordenar_todos(data, horario_actual, obligatorios, mejor_horarios=None, min_topes=float('inf')):
    if mejor_horarios is None:
        mejor_horarios = []

    if len(horario_actual) == numero_ramos:
        if all(any(ramo.nombre == oblig for ramo in horario_actual) for oblig in obligatorios):
            topes = revisar(horario_actual)
            if topes < min_topes:
                mejor_horarios = [horario_actual[:]]
                min_topes = topes
            elif topes == min_topes:
                mejor_horarios.append(horario_actual[:])
        return mejor_horarios, min_topes

    for i in range(len(data)):
        ramo = data[i]
        if ramo not in horario_actual:
            nuevo_horario = horario_actual + [ramo]
            mejor_horarios, min_topes = ordenar_todos(data[i+1:], nuevo_horario, obligatorios, mejor_horarios, min_topes)

    return mejor_horarios, min_topes



'''
La funcion guarda los horarios óptimos en un archivo de texto.

    Parametros:
        horarios (list): Lista de horarios óptimos.
        archivo (str): Nombre del archivo de texto
        
    Retorno:
        La funcion no retorna nada.
'''
def guardar_horarios_txt(horarios, archivo="horarios_optimos.txt"):
    with open(archivo, "w") as f:
        for idx, horario in enumerate(horarios, start=1):
            f.write(f"Horario #{idx}:\n")
            for ramo in horario:
                f.write(f"  {ramo}\n")
            f.write("\n")
    print(f"Horarios óptimos guardados en {archivo}")



'''
La funcion traduce un día y bloque a índices de la matriz horaria.

    Parametros:
        dia (str): Dia de la semana.
        bloque (str): Bloque horario.
        
    Retorno:
        La funcion retorna los indices (x, y) correspondientes en la matriz.
'''
def translate(dia, bloque):
    bloque = bloque.strip("\n")

    dias = {"Lunes": 2, 
            "Martes": 3, 
            "Miercoles": 4, 
            "Jueves": 5, 
            "Viernes": 6,
            "Sabado": 7,
            "Domingo": 8}
    
    bloques = {"1-2": 1, 
               "3-4": 2, 
               "5-6": 3, 
               "7-8": 4,
               "9-10": 5, 
               "11-12": 6, 
               "13-14": 7,
               "15-16": 8,
               "17-18": 9,
               "19-20": 10}
    
    return dias[dia],bloques[bloque]



'''
La funcion calcula los topes y muestra el horario seleccionado.

    Parametros:
        horario (list): Lista de ramos seleccionados.
        data (list): Matriz de horario.
        num (int): Numero de horario.
        
    Retorno:
        La funcion no retorna nada.
'''
def Topes(horario, data, num):
    local_topes_problem = []
    for obj in horario:
        for hora in obj.horario.split(";"):
            dia, bloque = hora.split(" ")
            x, y = translate(dia, bloque)
            if data[y][x] != "-":
                local_topes_problem.append((obj.sigla, data[y][x]))
                data[y][x] = "TOPE"
            else:
                data[y][x] = obj.sigla

    ui = HorarioSeleccionado(data, local_topes_problem, horario, num)
    ui.mainloop()



'''
La funcion revisa la cantidad de conflictos de horarios en el horario dado.

    Parametros:
        horario (list): Lista de ramos seleccionados.
        
    Retorno:
        La funcion retorna el numero de topes.
'''
def revisar(horario):
    horarios_usados = []
    topes = 0

    for ramo in horario:
        bloques = ramo.horario.split(";")
        for bloque in bloques:
            if bloque in horarios_usados:
                topes += 1
            else:
                horarios_usados.append(bloque)

    return topes



'''
La funcion genera combinaciones de horarios con n ramos, considerando ramos obligatorios

    Parametros:
        data (list): Lista de ramos disponibles.
        horario_actual (list): Lista de ramos seleccionados actualmente.
        obligatorios (list): Lista con nombres de ramos obligatorios.
        mejor_horario (list): Lista de los mejores horarios encontrados hasta ahora.
        
    Retorno:
        La funcion retorna una lista de ramos con la mejor combinación.
'''
def ordenar(data, horario_actual, obligatorios, mejor_horario=None):
    if len(horario_actual) == numero_ramos:
        if all(any(ramo.nombre == oblig for ramo in horario_actual) for oblig in obligatorios):
            topes = revisar(horario_actual)
            if mejor_horario is None or topes < revisar(mejor_horario):
                mejor_horario = horario_actual[:]
        return mejor_horario

    for i in range(len(data)):
        ramo = data[i]
        if ramo not in horario_actual:
            nuevo_horario = horario_actual + [ramo]
            nuevo_mejor_horario = ordenar(data[i+1:], nuevo_horario, obligatorios, mejor_horario)
            if nuevo_mejor_horario:
                mejor_horario = nuevo_mejor_horario

    return mejor_horario


#Cargar datos de ramos
data = []
archivo = open("ramos.csv", "r")
rams = []
for line in archivo:
    ramo,sigla,paralelo,horario = line.split(",")
    data.append(Ramo(ramo,sigla,paralelo,horario))
    if ramo not in rams:
        rams.append(ramo)

archivo.close()





#Generar los horarios óptimos
mejores_horarios, min_topes = ordenar_todos(data, [], obligatorios)

print(f"Cantidad mínima de topes: {min_topes}")
print(f"Horarios óptimos encontrados: {len(mejores_horarios)}")

#Mostrar en la interfaz
app = Horario(mejores_horarios)
app.mainloop()