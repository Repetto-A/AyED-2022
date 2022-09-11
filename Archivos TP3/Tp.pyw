import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

def darkstyle(root):
   
    style = ttk.Style(root)
    root.tk.call('source', 'azure dark/azure dark.tcl')
    style.theme_use('azure')
    style.configure("Accentttk.Button", foreground='white')
    style.configure("Togglettk.Button", foreground='white')
    return style

def salirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
	if valor=="yes":
		root.destroy()

def salirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
	if valor=="yes":
		root.destroy()



def botonesMenu():
	boton1=ttk.Button(root, text="ADMINISTRACIONES", width=29)
	boton1.place(relx=0.41, rely=0.16)
	boton2=ttk.Button(root, text="ENTREGA DE CUPOS", width=29)
	boton2.place(relx=0.41, rely=0.16)
	boton3=ttk.Button(root, text="RECEPCIÓN", width=29)
	boton3.place(relx=0.41, rely=0.23)
	boton4=ttk.Button(root, text="REGISTRAR CALIDAD", width=29)
	boton4.place(relx=0.41, rely=0.30)
	boton5=ttk.Button(root, text="REGISTRAR PESO BRUTO", width=29)
	boton5.place(relx=0.41, rely=0.37)
	boton6=ttk.Button(root, text="REGISTRAR DESCARGA", width=29)
	boton6.place(relx=0.41, rely=0.44)
	boton7=ttk.Button(root, text="REGISTRAR TARA", width=29)
	boton7.place(relx=0.41, rely=0.51)
	boton8=ttk.Button(root, text="REPORTES", width=29)
	boton8.place(relx=0.41, rely=0.58)
	boton9=ttk.Button(root, text="LISTADO DE SILOS Y RECHAZOS", width=29)
	boton9.place(relx=0.41, rely=0.65)
	boton0=ttk.Button(root, text="FIN DEL PROGRAMA", command=salirAplicacion, width=29)
	boton0.place(relx=0.41, rely=0.72)



def main_window():
	global root
	root = tk.Tk()
	root.config(width=800, height=500, padx=5, pady=5)
	root.title("Primer intento de prototipo")
	root.resizable(0,0)
	img = tk.PhotoImage(file="Fondo.png")
	style = darkstyle(root)
	botonesMenu()
	ttk.Label(root, text="MENÚ PRINCIPAL", font=("arial",20)).place(relx=0.388, rely=0.04)
	root.mainloop()


main_window()