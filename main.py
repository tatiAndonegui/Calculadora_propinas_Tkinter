#Creación de una aplicación tkinter

#Objetivo: Crear una aplicación tkinter que demuestre los conceptos
#aprendidos sobre tkinter incluyendo la creación de ventanas, widgets,
#manejo de eventos y manipulación de widgets.

#Descripción: Debes crear una aplicación tkinter simple que funcione
#como una calculadora de propinas. La aplicación debe tener una
#interfaz con un campo de entrada para el monto de la cuenta y
#botones para calcular la propina. Debes usar etiquetas para mostrar los
#resultados.


import tkinter as tk

root = tk.Tk()

#configuro titulo de la ventana
root.title("Calculadora de propinas")

#configurar tamaño de la ventana y el titulo
root.geometry("400x300")
root.title("mi ventana")

#creamos un label y mostramos etiqueta en la ventana
etiqueta = tk.Label(root,text="Monto de la cuenta")
etiqueta.pack() 

#entrada de texto
entrada =tk.Entry(root)
entrada.pack()

def calcular_propina():
    monto = float(entrada.get())
    propina = (monto * 0.15)
    etiqueta.config(text=f'su propina es {propina}!')

propina_15=tk.Button(root,text="Propina del 15%", command= calcular_propina)
propina_15.pack()


#muestro la ventana  , siempre debe ir al final
root.mainloop()
