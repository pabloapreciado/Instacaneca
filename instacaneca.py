from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from turtle import heading
import estilos
import re

#-------------------------
#Funciones de operaciones
#-------------------------
def calcular():
    def limpiarString(entrada) -> cade:
        def normalize(entradasa):
            replacements = (
                ("á", "a"),
                ("é", "e"),
                ("í", "i"),
                ("ó", "o"),
                ("ú", "u"),
            )
            for a, b in replacements:
                entradasa = entradasa.replace(a, b).replace(a.upper(), b.upper())
            return entradasa

        salid = normalize(entrada)  # Quitar tíldes
        salid = salid.lower()  # Poner en minúscula
        salid = salid.strip()  # Quitar tabulaciones
        salid = re.sub(r"\s+", "", salid)  # Quitar espacios

        return list(salid)  # Retorna como lista

    cad = limpiarString(cade.get())
    
    

    organicos = ["cascarasdefrutas", "cascarasdeverdura", "restosdealimentos", "frutas", "cascaradefruta", "verdura",
                 "fruta", "verduras", "cascaradebanano", "banano", "manzana", "maracuya", "pimenton", ] 
    reciclaje = ["plastico", "vidrio", "metal", "papel", "carton","bolsas","bolsadeplatico","bolsasdeplastico","lata",
    "latadealuminio","latadegaseosa","envase","envasedepapel","envasedeleche","envasedeyogurt","empaquedepapas","botella",
    "botelladegaseosa"] 
    peligroso = ["papelhigienico", "servilletas", "comidapreparada", "guantes", "tapabocas"]

    # if list != cad:   if (cad==organico or cad==reciclage or)
    if (cad == organicos,reciclaje,peligroso):
        for i in organicos:
            salid = list(i)
            if set(cad) == set(salid):
                at_resultado.insert(tk.INSERT, "\nDeposite en orgánicos ->Caneca Verde" )
            #else:
            #    at_resultado.insert(tk.INSERT, "\n")

        for i in reciclaje:
            salid = list(i)
            if set(cad) == set(salid):
                at_resultado.insert(tk.INSERT, "\nDeposite en reciclaje ->Caneca Blanca")
            #else:
            #    at_resultado.insert(tk.INSERT," ")

        for i in peligroso:
            salid = list(i)
            if set(cad) == set(salid):
                at_resultado.insert(tk.INSERT, "\nDeposite en peligroso ->Caneca Negra\n/Roja")
            #else:
            #    at_resultado.insert(tk.INSERT, "\n")
    else:
        at_resultado.insert(tk.INSERT, "\nEscriba otra tipo de basura")


def borrar():
    messagebox.showinfo("Programa1", "Los datos seran borrados")
    cade.set("Digite la basura")
    at_resultado.delete("1.0", "end")


def salir():
    messagebox.showinfo("Programa1", "Gracias por usar este Programa")
    ventana_principal.destroy()
#Creacio objeto tk, ventana_principal
ventana_principal = tk.Tk()

#Titulo de la ventana principal
ventana_principal.title("instaneca")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#Dimensiones de la ventana
ventana_principal.geometry('480x500')

#Color fondo ventana
ventana_principal.config(bg=estilos.COLOR_FONDO_FRAMES)

"""Agregar frames o paneles a la 
ventana principal"""


#--------------------
#Variables globales - Variables de control
#--------------------
cade = tk.StringVar()

"""Agregar frames o paneles a la ventana principal"""

#---------------------------
#Frame de entrada de datos
#---------------------------
frame_entrada = tk.Frame(ventana_principal)
frame_entrada.config(bg=estilos.COLOR_FONDO_FRAMES, width=480, height=200)
frame_entrada.pack(fill=tk.BOTH, padx=10, pady=10)

#Etiqueta de texto (Label)
titulo = tk.Label(frame_entrada,text="INSTA-CANECA")
titulo.config(bg=estilos.COLOR_FONDO_FRAMES, fg="black", font=("Monaco", 20))
titulo.place(x=110, y=10)

# Imagen
logo_pag = tk.PhotoImage(file="iconodereciclaje.png")
label_logo = tk.Label(frame_entrada, image=logo_pag)
label_logo.place(x=340, y=10)

#Agrego un objeto canvas
c = tk.Canvas(frame_entrada)
c.place(x=45, y=100)
#Etiqueta X
label_cade = tk.Label(frame_entrada, text="Digita el residuo que vas a desechar ")
label_cade.config(bg=estilos.COLOR_LETRA, fg="black", font=("Didot", 14))
label_cade.place(x=45, y=100)
# Caja de texto x
entry_cade = tk.Entry(frame_entrada, textvariable=cade)
entry_cade.config(font=("Monaco", (12)))
entry_cade.focus_set()
entry_cade.place(x=60, y=140)


#-----------------------
#Frame para operaciones
#-----------------------
frame_operaciones = tk.Frame(ventana_principal)
frame_operaciones.config(bg=estilos.COLOR_FONDO_FRAMES1)
frame_operaciones.pack(fill=tk.BOTH, padx=20, pady=20)
frame_operaciones.columnconfigure(0,weight=1)
frame_operaciones.columnconfigure(2,weight=1)
frame_operaciones.columnconfigure(2,weight=1)

# Boton Calcular
boton_calcular = tk.Button(frame_operaciones, text="Calcular", command=calcular)
boton_calcular.config(bg=estilos.COLOR_CALCULAR,fg="white")
boton_calcular.grid(row=0, column=0, padx=10, pady=10)

# Boton borrar
boton_borrar = tk.Button(frame_operaciones, text="Borrar", command=borrar)
boton_borrar.config(bg=estilos.COLOR_CALCULAR,fg="white")
boton_borrar.grid(row=0, column=1, padx=10, pady=10)
#boton_borrar.place(x=100, y=50)

# Boton Salir
boton_salir = tk.Button(frame_operaciones, text="Salir", command=salir)
boton_salir.config(bg=estilos.COLOR_SALIR,fg="white")
boton_salir.grid(row=0, column=2, padx=10, pady=10)

#----------------------
#Frame para resultados
#----------------------
frame_resultados = tk.Frame(ventana_principal)
frame_resultados.config(bg=estilos.COLOR_FONDO_FRAMES, width=500, height=300)
frame_resultados.pack(fill=tk.BOTH, padx=45, pady=10)

#Area de texto resultados
at_resultado = tk.Text(frame_resultados, width=100, height=10)
at_resultado.grid(row=5, column=5)
sb_resultado = tk.Scrollbar(frame_resultados, command=at_resultado.yview)
sb_resultado.grid(row=5, column=1, sticky="nsew" )

"""Desplegamos la ventana principal
en pantalla"""
ventana_principal.mainloop()