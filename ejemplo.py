import tkinter as tk
#EJEMPLO 1
#se crea la ventana principal
#root = tk.Tk()
#configuro titulo de la ventana
#root.title("Mi primer tkinter")

#configurar tamaño de la ventana y el titulo
#root.geometry("400x300")
#root.title("mi titulo")

#creamos un label y mostramos etiqueta en la ventana
#etiqueta = tk.Label(root,text="Hola!")
#etiqueta.pack() #siempre se pone pack al finalizar cada uno

#boton 
##boton=tk.Button(root,text="haz click")
#boton.pack()

#entrada de texto
#entrada =tk.Entry(root)
#entrada.pack()
#muestro la ventana  , siempre debe ir al final
#root.mainloop()

#EJEMPLO 2 Hacemos un manejo de evento con funcion------------

#def saludar():
    #etiqueta.config(text="aca estoy")

#root = tk.Tk()
#root.title("Mi primer tkinter")

#etiqueta = tk.Label(root,text="presiona el boton")
#etiqueta.pack() 

#boton=tk.Button(root,text="Saludar", command=saludar)
#boton.pack()

#etiqueta = tk.Label(root,text="que bien que presionaste el boton")
#etiqueta.pack() 

#muestro la ventana  , siempre debe ir al final
#root.mainloop()

#EJEMPLO 3 Hacemos un manejo de evento con funcion------------

#root = tk.Tk()
#root.title("obtener y mostrar datos de entrada")

#entrada =tk.Entry(root)
#entrada.pack()

#def mostrar_nombre():
    #nombre=entrada.get()
    #etiqueta.config(text=f'hola, {nombre}!')

#etiqueta= tk.Label(root,text="ingrese su nombre: ")
#etiqueta.pack()

#boton=tk.Button(root,text="Saludar", command= mostrar_nombre)
#boton.pack()
#muestro la ventana  , siempre debe ir al final
#root.mainloop()

#EJEMPLO 4 Ejemplo de Framework ------------

#root = tk.Tk()
#root.title("ejemplo de diseño de frames")


#configurar tamaño de la ventana y el titulo
#root.geometry("400x300")
#root.title("mi titulo")

#frame1= tk.Frame(root, borderwidth=2,relief="solid")
#frame1.pack(side="left",padx=10,pady=50)

#frame2= tk.Frame(root, borderwidth=2,relief="ridge")
#frame2.pack(side="right",padx=20,pady=10)

#label1=tk.Label(frame1,text="Frame 1")
#label1.pack()

#label2=tk.Label(frame2,text="Frame 2")
#label2.pack()

#muestro la ventana  , siempre debe ir al final
#root.mainloop()


#EJEMPLO 5 Ejemplo de Framework con GRID ------------

#root = tk.Tk()
#root.title("ejemplo de colocacion en un grid")

#label1=tk.Label(root, text="Nombre: ")
#label2=tk.Label(root, text="Contraseña: ")

#entry1= tk.Entry(root)
#entry2= tk.Entry(root, show="*")

#label1.grid(row=0,column=0)
#label2.grid(row=1,column=0)
#entry1.grid(row=0,column=1)
#entry2.grid(row=1,column=1)
#NO PONER PACK POR QUE EL GRID SOLO LO EMPAQUETA

#configurar tamaño de la ventana y el titulo
#root.geometry("400x300")
#root.title("mi titulo")

#muestro la ventana  , siempre debe ir al final
#root.mainloop()

#EJEMPLO 6 Manipulacion de widgets ------------

#root = tk.Tk()
#root.title("ejemplo de manipulacion de widget con cambio de propiedades")

#etiqueta= tk.Label(root,text="hola")
#etiqueta.pack()

#cambia la fuente
#etiqueta.config(font=("Comic Sans",14))

#cambia el color de fondo y del texto
#etiqueta.config(bg="pink",fg="green")

#muestro la ventana  , siempre debe ir al final
#root.mainloop()


#EJEMPLO 7 habilitar o deshabilitar botones ------------

#root = tk.Tk()
#root.title("ejemplo de habilitar o deshabilitar botones ")

#etiqueta= tk.Label(root,text="prueba ")
#etiqueta.pack()

#def habilitar():
    #boton.config(state="normal")

#def deshabilitar():
    #boton.config(state="disabled")    


#boton=tk.Button(root,text="haz click", state="disabled")
#boton.pack()

#este es un boton deshabilitado que no hace nada 
#boton_habilitar=tk.Button(root,text="habiltar boton", command=habilitar)
#boton_habilitar.pack()

#boton_deshabilitar=tk.Button(root,text="deshabiltar boton", command=deshabilitar)
#boton_deshabilitar.pack()

#muestro la ventana  ,siempre debe ir al final
#root.mainloop()

#EJEMPLO 8 mostrar y ocultar------------

#root = tk.Tk()
#root.title("ejemplo de mostrar y ocultar")


#def ocultar_etiqueta():
    #etiqueta.pack_forget()

#def mostrar_etiqueta():
    #etiqueta.pack()

#boton_ocultar=tk.Button(root,text="ocultar etiqueta", command=ocultar_etiqueta)
#boton_ocultar.pack()

#boton_mostrar=tk.Button(root,text="mostrar etiqueta", command=mostrar_etiqueta)
#boton_mostrar.pack()

#etiqueta= tk.Label(root,text="esto es una etiqueta ")
#etiqueta.pack()

#muestro la ventana  ,siempre debe ir al final
#root.mainloop()
