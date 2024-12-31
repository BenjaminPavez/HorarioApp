# -----------------------------------------------------------------------------
#
# HorarioApp
#
# Desarrollado por: Benjamin Pavez
#
# Fecha Inicio: 28-12-2024
#
# Fecha Ultima Modificacion: 29-12-2024
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
#
# DESCRIPCIÓN:
# Programa principal de HorarioApp (main.py).
#
# -----------------------------------------------------------------------------
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from customtkinter import *
from PIL import Image
from tkinter import messagebox, ttk, simpledialog
from tkcalendar import DateEntry, Calendar
from datetime import datetime
from CTkListbox import *
from CTkTable import *
import tkinter as tk


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


class Horario(CTk):
    # Constructor
    def __init__(self, wea, topes_problem, horario):
        super().__init__()

        self.geometry("1000x800")
        self.title("Generador de Horarios")
        self.configure(bg="#2b2b2b")  # Opcional: fondo oscuro

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        title_label = CTkLabel(self, text="Horario 2025-1: Minimizar cantidad de Topes", 
                               text_color="white", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, pady=10, sticky="n")

        topes_label = CTkLabel(self, text=f"Cantidad de Topes: {len(topes_problem)}", 
                               font=("Helvetica", 12))
        topes_label.grid(row=1, column=0, pady=10, sticky="n")

        frametabla = CTkFrame(master=self, corner_radius=10)
        frametabla.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        table = CTkTable(frametabla, row=11, column=9, values=wea, width=130, height=10, corner_radius=10)
        table.pack(expand=True, fill="both", padx=10, pady=10)


        #Ramos
        observations_label = CTkLabel(self, text="Asignaturas", font=("Helvetica", 12))
        observations_label.grid(row=3, column=0, pady=10, sticky="n")

        observations_frame = CTkFrame(self, corner_radius=10)
        observations_frame.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")

        for i in horario:
            CTkLabel(observations_frame, text=f"{i}", 
                     font=("Helvetica", 12)).pack(anchor="w", padx=10)
            
        #Topes 
        observations_label = CTkLabel(self, text="Topes", font=("Helvetica", 12))
        observations_label.grid(row=3, column=0, pady=10, sticky="n")

        observations_frame = CTkFrame(self, corner_radius=10)
        observations_frame.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")

        for i, (ramo1, ramo2) in enumerate(topes_problem):
            CTkLabel(observations_frame, text=f"El ramo {ramo1} topa con {ramo2}", 
                     font=("Helvetica", 12)).pack(anchor="w", padx=10)

        self.rowconfigure(2, weight=3)
        self.rowconfigure(4, weight=2)

        
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




def translate(dia, bloque):
    bloque = bloque.strip("\n")
    """
    Traduce un día y bloque a índices de la matriz horaria.

    :param dia: Día (ejemplo: 'Lunes').
    :param bloque: Bloque (ejemplo: '9-10').
    :return: Índices (x, y) correspondientes en la matriz.
    """
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
    
    return bloques[bloque], dias[dia]


topes_problem = []
#data es una lista con los ramos SIN REPETIR
def Topes(horario):
    tope = 0
    for obj in horario:
        for hora in obj.horario.split(";"):
            dia,bloque = hora.split(" ")
            x,y = translate(dia,bloque)
            if Dataframe[y][x] != "-":
                Dataframe[y][x] = "TOPE"
                topes_problem.append((obj.sigla,Dataframe[y][x]))
                tope += 1
            else:
                Dataframe[y][x] = obj.sigla


    ui = Horario(Dataframe,topes_problem, horario)
    ui.mainloop()

def revisar(horario):
    """
    Verifica la cantidad de conflictos de horarios en el horario dado.
    """
    horarios_usados = []
    topes = 0

    for ramo in horario:
        bloques = ramo.horario.split(";")  # Divide los bloques horarios
        for bloque in bloques:
            if bloque in horarios_usados:
                topes += 1
            else:
                horarios_usados.append(bloque)

    return topes



def ordenar(data, horario_actual, obligatorios, mejor_horario=None):
    """
    Genera combinaciones de horarios con 7 ramos, considerando ramos obligatorios.
    
    :param data: Lista de ramos disponibles.
    :param horario_actual: Lista de ramos seleccionados actualmente.
    :param obligatorios: Lista con nombres de ramos obligatorios.
    :param mejor_horario: El mejor horario encontrado hasta ahora.
    :return: Lista de ramos con la mejor combinación.
    """
    if len(horario_actual) == 7:
        # Verifica que todos los obligatorios estén presentes
        if all(any(ramo.nombre == oblig for ramo in horario_actual) for oblig in obligatorios):
            topes = revisar(horario_actual)
            if mejor_horario is None or topes < revisar(mejor_horario):
                mejor_horario = horario_actual[:]  # Actualiza el mejor horario
        return mejor_horario

    for i in range(len(data)):
        ramo = data[i]
        # Asegurarse de no incluir el mismo ramo-paralelo más de una vez
        if ramo not in horario_actual:
            nuevo_horario = horario_actual + [ramo]
            nuevo_mejor_horario = ordenar(data[i+1:], nuevo_horario, obligatorios, mejor_horario)
            if nuevo_mejor_horario:
                mejor_horario = nuevo_mejor_horario

    return mejor_horario


#Cargar datos de ramos
data = []
archivo = open("ramos.csv", "r")
for line in archivo:
    ramo,sigla,paralelo,horario = line.split(",")
    data.append(Ramo(ramo,sigla,paralelo,horario))

#Ramos obligatorios
obligatorios = ["Computacion Cientifica", "Gestion de Proyectos Informaticos", "Inteligencia Artificial", "Sistemas Distribuidos"]

mejor_horario = ordenar(data, [], obligatorios)
print("Mejor horario encontrado:", mejor_horario)
Topes(mejor_horario)




'''
#Ejemplo de uso
Ramo1 = Ramo("Computacion Cientifica","INF-285","200","Martes 9-10;Jueves 9-10;Viernes 3-4")
Ramo1 = Ramo("Computacion Cientifica","INF-285","201","Lunes 1-2;Martes 3-4;Miercoles 5-6")
Ramo2 = Ramo("Gestion de Proyectos Informaticos","INF-360","200","Jueves 3-4;Jueves 5-6")
Ramo3 = Ramo("Inteligencia Artificial","INF-295","200","Lunes 5-6;Lunes 7-8;Martes 3-4;Martes 5-6")
Ramo4 = Ramo("Sistemas Distribuidos","INF-343","200","Martes 5-6;Martes 9-10")
Ramo5 = Ramo("Computacion Distribuida para Big Data","INF-356","200","Lunes 13-14;Miercoles 13-14")
Ramo6 = Ramo("Taller Criptografia Aplicada","INF-358","200","Martes 11-12;Martes 13-14")
Ramo7 = Ramo("Testing de Interfaces Usuarios","INF-338","200","Miercoles 3-4;Miercoles 5-6")

wea = [['-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-', '-']
           ]
horario = [Ramo1,Ramo2,Ramo3,Ramo4,Ramo5,Ramo6,Ramo7]

topes_problem = []
#data es una lista con los ramos SIN REPETIR
def Topes(horario):
    tope = 0
    for obj in horario:
        print("-------------------------------------------------------------------------------")
        print("Ramo: "+obj.nombre)
        print("Sigla: "+obj.sigla)
        print("Paralelo: "+obj.paralelo)
        for hora in obj.horario.split(";"):
            dia,bloque = hora.split(" ")
            print("Dia: "+dia)
            print("Bloque: "+bloque)
            x,y = translate(dia,bloque)
            if wea[y][x] != "-":
                topes_problem.append((obj.sigla,wea[y][x]))
                tope += 1
            else:
                wea[y][x] = obj.sigla

            print(x,y)
        print("-------------------------------------------------------------------------------\n")
    print("Horario: ")
    ui = Horario(wea,topes_problem)
    ui.mainloop()


Topes(horario)
'''