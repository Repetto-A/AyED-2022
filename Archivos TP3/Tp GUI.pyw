from ast import Sub
from struct import unpack
from telnetlib import X3PAD
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Entry, messagebox
import os, pickle, os.path,sys,datetime,io
from datetime import date
from turtle import left, right
from colorama import init, Fore, Back, Style
from notifypy import Notify
import requests

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

def Administraciones():
	global root, Adm, Menu_p, Packed, Submp

	Unpack()
	Adm=tk.Frame(root)
	Adm.pack(fill="both", expand=True)
	Packed="Adm"
	Adm.config(width=800, height=500, padx=5, pady=5)
	Adm.pack_propagate(0)
	ttk.Label(Adm, text="MENÚ ADMINISTRACIONES", font=("arial",20)).pack(padx=10, pady=10)
	botona=ttk.Button(Adm, text="TITULARES", width=29, command=Notificacion)
	botona.pack(padx=5, pady=5)
	botonb=ttk.Button(Adm, text="PRODUCTOS", width=29, command=Submenu_Prod)
	botonb.pack(padx=5, pady=5)
	botonc=ttk.Button(Adm, text="RUBROS", width=29)
	botonc.pack(padx=5, pady=5)
	botond=ttk.Button(Adm, text="RUBROS POR PRODUCTO", width=29)
	botond.pack(padx=5, pady=5)
	botone=ttk.Button(Adm, text="SILOS", width=29)
	botone.pack(padx=5, pady=5)
	botonf=ttk.Button(Adm, text="SUCURSALES", width=29, command=Notificacion)
	botonf.pack(padx=5, pady=5)
	botong=ttk.Button(Adm, text="PRODUCTO POR TITULAR", width=29, command=Notificacion)
	botong.pack(padx=5, pady=5)
	botonv=ttk.Button(Adm, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu)
	botonv.pack(padx=5, pady=5)

def Submenu_Prod():
	global root, Menu_p, Packed, Adm, Submp

	Unpack()
	Submp=tk.Frame(root)
	Submp.pack(fill="both", expand=True)
	Packed="Submp"
	Submp.config(width=800, height=500, padx=5, pady=5)
	Submp.pack_propagate(0)
	ttk.Label(Submp, text="SUB-MENÚ PRODUCTOS", font=("arial",20)).pack(padx=10, pady=10)
	botona=ttk.Button(Submp, text="ALTA", width=29)
	botona.pack(padx=5, pady=5)
	botonb=ttk.Button(Submp, text="BAJA", width=29)
	botonb.pack(padx=5, pady=5)
	botonc=ttk.Button(Submp, text="CONSULTA", width=29)
	botonc.pack(padx=5, pady=5)
	botond=ttk.Button(Submp, text="MODIFICACIÓN", width=29)
	botond.pack(padx=5, pady=5)
	botone=ttk.Button(Submp, text="VOLVER A ADMINISTRACIONES", width=29, command=Administraciones)
	botone.pack(padx=5, pady=5)

def Volver_Menu():
	global Adm,Menu_p, Packed, Submp

	Unpack()
	Menu_p.pack(fill="both", expand=True)
	Menu_p.pack_propagate(0)
	Packed="Menu_p"

def Menu():
	global Menu_p, Packed, root
	
	Menu_p=tk.Frame(root)
	Menu_p.pack(fill="both", expand=True)
	Packed="Menu_p"
	Menu_p.configure(width=800, height=500, padx=5, pady=5)
	Menu_p.pack_propagate(0)
	ttk.Label(Menu_p, text="MENÚ PRINCIPAL", font=("arial",20)).pack(padx=10, pady=10)
	boton1=ttk.Button(Menu_p, text="ADMINISTRACIONES", width=29, command=Administraciones)
	boton1.pack(padx=5, pady=5)
	boton2=ttk.Button(Menu_p, text="ENTREGA DE CUPOS", width=29, command=lambda:Menu_Pat('Cupos'))
	boton2.pack(padx=5, pady=5)
	boton3=ttk.Button(Menu_p, text="RECEPCIÓN", width=29, command=lambda:Menu_Pat('Recepcion'))
	boton3.pack(padx=5, pady=5)
	boton4=ttk.Button(Menu_p, text="REGISTRAR CALIDAD", width=29, command=lambda:Menu_Pat('Calidad'))
	boton4.pack(padx=5, pady=5)
	boton5=ttk.Button(Menu_p, text="REGISTRAR PESO BRUTO", width=29, command=lambda:Menu_Pat("PBruto"))
	boton5.pack(padx=5, pady=5)
	boton6=ttk.Button(Menu_p, text="REGISTRAR DESCARGA", width=29, command=Notificacion)
	boton6.pack(padx=5, pady=5)
	boton7=ttk.Button(Menu_p, text="REGISTRAR TARA", width=29, command=lambda:Menu_Pat("Tara"))
	boton7.pack(padx=5, pady=5)
	boton8=ttk.Button(Menu_p, text="REPORTES", width=29, command=Reportes)
	boton8.pack(padx=5, pady=5)
	boton9=ttk.Button(Menu_p, text="LISTADO DE SILOS Y RECHAZOS", width=29, command=Listado)
	boton9.pack(padx=5, pady=5)
	boton0=ttk.Button(Menu_p, text="FIN DEL PROGRAMA", command=salirAplicacion, width=29)
	boton0.pack(padx=5, pady=5)

def Unpack():
	global Packed, Menu_p, Submp, Adm, Pat, Cup, Rec, Cal
	
	if(Packed=="Menu_p"):
		Menu_p.pack_forget()
	elif(Packed=="Submp"):
		Submp.pack_forget()
	elif(Packed=="Adm"):
		Adm.pack_forget()
	elif(Packed=="Pat"):
		Pat.pack_forget()
	elif(Packed=="Cup"):
		Cup.pack_forget()
	elif(Packed=="Cal"):
		Cal.pack_forget()
	elif(Packed=="PBru"):
		PBru.pack_forget()
	elif(Packed=="Rec"):
		Rec.pack_forget()
	elif(Packed=="Des"):
		Des.pack_forget()
	elif(Packed=="Tar"):
		Tar.pack_forget()
	elif(Packed=="Rep"):
		Rep.pack_forget()

def Menu_Pat(Op_menu):
	global Pat, root, Patente, Packed, Menu_p

	Unpack()
	Pat=tk.Frame(root)
	Pat.pack(fill="both", expand=True)
	Packed="Pat"
	Pat.config(width=800, height=500, padx=5, pady=5)
	Pat.pack_propagate(0)
	ttk.Label(Pat, text="INGRESO DE PATENTE", font=("arial",20)).pack(padx=10, pady=10)
	Patente=tk.StringVar()
	Cuadrat=tk.Entry(Pat, textvariable=Patente, justify="center", width=20).pack(ipadx=5,ipady=5,padx=10, pady=10)
	Send_button=ttk.Button(Pat, text="Validar", command=lambda:Valida_pat(Op_menu), width=8).pack(ipadx=3,ipady=3,padx=10,pady=10)  #.place(relx=0.61, rely=0.13)
	botonmenu=ttk.Button(Pat, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=10, pady=10)

def Valida_pat(Op_menu):
	global Patente, Packed, Menu_p

	X=Patente.get()
	if(X=='V') or (X.isalnum()==True) and (len(X)==6) or (len(X)==7):
		Unpack()
		if(Op_menu=="Cupos"):
			Cupos()
		elif(Op_menu=="Recepcion"):
			Recepcion()
		elif(Op_menu=="Calidad"):
			Calidad()
		elif(Op_menu=="PBruto"):
			PBruto()
		elif(Op_menu=="Descarga"):
			Descarga()
		elif(Op_menu=="Tara"):
			Tara()

	else:
		valor=messagebox.askretrycancel("Patente inválida", "¿Desea intentarlo nuevamente?")
		if valor==False:
			Unpack()
			Packed="Menu_p"
			Menu_p.pack(fill="both", expand=True)
			Menu_p.pack_propagate(0)
	
def Cupos():
	global Packed, Cup

	Cup=tk.Frame(root)
	Cup.pack(fill="both", expand=True)
	Cup.config(width=800, height=500, padx=5, pady=5)
	Cup.pack_propagate(0)
	Packed="Cup"
	Title=ttk.Label(Cup, text="ENTREGA DE CUPOS", font=("arial",20)).pack(padx=10, pady=10)
	botonmenu=ttk.Button(Cup, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=5)

def Recepcion():
	global Packed, Rec

	Rec=tk.Frame(root)
	Rec.pack(fill="both", expand=True)
	Rec.config(width=800, height=500, padx=5, pady=5)
	Rec.pack_propagate(0)
	Packed="Rec"
	Title=ttk.Label(Rec, text="RECEPCIÓN", font=("arial",20)).pack(padx=10, pady=10)
	botonmenu=ttk.Button(Rec, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=5)

def Calidad():
	global Packed, Cal

	Cal=tk.Frame(root)
	Cal.pack(fill="both", expand=True)
	Cal.config(width=800, height=500, padx=5, pady=5)
	Cal.pack_propagate(0)
	Packed="Cal"
	Title=ttk.Label(Cal, text="REGISTRAR CALIDAD", font=("arial",20)).pack(padx=10, pady=10)
	botonmenu=ttk.Button(Cal, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=5)
		
def PBruto():
	global Packed, PBru

	PBru=tk.Frame(root)
	PBru.pack(fill="both", expand=True)
	PBru.config(width=800, height=500, padx=5, pady=5)
	PBru.pack_propagate(0)
	Packed="PBru"
	Title=ttk.Label(PBru, text="REGISTRAR PESO BRUTO", font=("arial",20)).pack(padx=10, pady=10)
	botonmenu=ttk.Button(PBru, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=5)

def Descarga():
	global Packed, Des

	Des=tk.Frame(root)
	Des.pack(fill="both", expand=True)
	Des.config(width=800, height=500, padx=5, pady=5)
	Des.pack_propagate(0)
	Packed="Des"
	Title=ttk.Label(Des, text="REGISTRAR DESCARGA", font=("arial",20)).pack(padx=10, pady=10)
	botonmenu=ttk.Button(Des, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=5)
		
def Tara():
	global Packed, Tar

	Tar=tk.Frame(root)
	Tar.pack(fill="both", expand=True)
	Tar.config(width=800, height=500, padx=5, pady=5)
	Tar.pack_propagate(0)
	Packed="Tar"
	Title=ttk.Label(Tar, text="REGISTRAR TARA", font=("arial",20)).pack(padx=10, pady=10)
	botonmenu=ttk.Button(Tar, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=5)

def Reportes():
	global Packed, Rep

	if not(os.path.exists("PatenteMenor.png")):
		Download("abc123","PatenteMenor") #También puede ir en el command del menú
	Unpack()
	Rep=tk.Frame(root)
	Rep.pack(fill="both", expand=True)
	Rep.config(width=800, height=500, padx=5, pady=5)
	Rep.pack_propagate(0)
	Packed="Rep"
	Title=ttk.Label(Rep, text="REPORTES", font=("arial",20)).pack(padx=10, pady=10)
	ImagenPatMenor=tk.PhotoImage(file="PatenteMenor.png")
	MarcoPatMenor= ttk.Label(Rep, image=ImagenPatMenor).pack(padx=5, pady=5)
	botonmenu=ttk.Button(Rep, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).pack(padx=5, pady=5)


def Listado():
	pass

def Download(pat, name):

	name= str(name + ".png")
	link=("http://matriculasdelmundo.com/gARG1.php?textARG1=" + pat)
	r = requests.get(link)
	with open(name,'wb') as f:
		f.write(r.content)

def Notificacion():

	Mantenimiento = Notify(default_notification_icon="code.ico")
	Mantenimiento.title = "Función en construcción!"
	Mantenimiento.message = "Por favor intente nuevamente con otra opcion."
	Mantenimiento.send()

def main_window():
	global root
	root = tk.Tk()
	root.config(width=800, height=500, padx=5, pady=5)
	root.title("Sistema de gestión para cerealeras")
	root.iconbitmap("code.ico")
	#root.resizable(0,0)
	img = tk.PhotoImage(file="Fondo.png")
	style = darkstyle(root)
	Menu()
	root.mainloop()


main_window()