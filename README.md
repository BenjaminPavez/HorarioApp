> [!NOTE]  
> Última Versión en Rama main.

# <img src="https://github.com/user-attachments/assets/efe92f90-efe9-4090-bce7-50ff474bfd52" alt="HorarioApp" width="40"> HorarioApp


**HorarioApp** es una aplicación diseñada para ayudar a los estudiantes a crear horarios académicos optimizados. A partir de los horarios disponibles en SIGA, minimiza los topes y organiza las asignaturas de manera eficiente, generando horarios personalizados que se pueden exportar en formato PDF.

![Screenshot 2025-01-02 231656](https://github.com/user-attachments/assets/d9068ce2-d59b-4c01-91e2-5b2063421c28)


Este proyecto está pensado para facilitar la planificación académica de estudiantes universitarios, especialmente sansanos, proporcionando una experiencia intuitiva y funcional.


## Requerimientos

- Python >= 3.10
- Tkinter

## Instrucciones de Uso

Para instalar las dependencias necesarias para HorarioApp, instala las siguientes dependencias:

```sh
pip install customtkinter
pip install tkcalendar
pip install CTkListbox
pip install reportlab
pip install CTkTable
```

Ahora debes llenar el archivo `ramos.csv` con tus ramos, si hay ramos con mas de un paralelo tambien lo tienes que anotar, aqui un ejemplo :

```sh
Nombre_Asignatura_1,Sigla_Asignatura_1,Paralelo_Asignatura_1,Horario_1_Asignatura_1;Horario_2_Asignatura_1;Horario_3_Asignatura_1
Nombre_Asignatura_2,Sigla_Asignatura_2,Paralelo_Asignatura_1,Horario_1_Asignatura_2;Horario_2_Asignatura_2;Horario_3_Asignatura_2
Nombre_Asignatura_3,Sigla_Asignatura_3,Paralelo_Asignatura_3,Horario_1_Asignatura_3;Horario_2_Asignatura_3
...
```
Despues debes modificar el archivo `main.py` indicando el semestre, la carrera, la cantidad de ramos que quieres tomar y los ramos obligatorios

Luego para ejecutar el archivo `main.py` :

```sh
python main.py
```

## ⚠️ **IMPORTANTE**

Este es un proyecto propio y puede presentar bugs o errores.

2024-2
