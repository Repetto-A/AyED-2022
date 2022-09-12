from ast import Sub
from struct import unpack
from telnetlib import X3PAD
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Entry, messagebox
import os, pickle, os.path,sys,datetime,io
from datetime import date
from colorama import init, Fore, Back, Style

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
	ttk.Label(Adm, text="MENÚ ADMINISTRACIONES", font=("arial",20)).place(relx=0.312, rely=0.04)
	botona=ttk.Button(Adm, text="TITULARES", width=29)
	botona.place(relx=0.41, rely=0.16)
	botonb=ttk.Button(Adm, text="PRODUCTOS", width=29, command=Submenu_Prod)
	botonb.place(relx=0.41, rely=0.23)
	botonc=ttk.Button(Adm, text="RUBROS", width=29)
	botonc.place(relx=0.41, rely=0.30)
	botond=ttk.Button(Adm, text="RUBROS POR PRODUCTO", width=29)
	botond.place(relx=0.41, rely=0.37)
	botone=ttk.Button(Adm, text="SILOS", width=29)
	botone.place(relx=0.41, rely=0.44)
	botonf=ttk.Button(Adm, text="SUCURSALES", width=29)
	botonf.place(relx=0.41, rely=0.51)
	botong=ttk.Button(Adm, text="PRODUCTO POR TITULAR", width=29)
	botong.place(relx=0.41, rely=0.58)
	botonv=ttk.Button(Adm, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu)
	botonv.place(relx=0.41, rely=0.65)

def Submenu_Prod():
	global root, Menu_p, Packed, Adm, Submp

	Unpack()
	Submp=tk.Frame(root)
	Submp.pack(fill="both", expand=True)
	Packed="Submp"
	Submp.config(width=800, height=500, padx=5, pady=5)
	ttk.Label(Submp, text="SUB-MENÚ PRODUCTOS", font=("arial",20)).place(relx=0.312, rely=0.04)
	botona=ttk.Button(Submp, text="ALTA", width=29)
	botona.place(relx=0.41, rely=0.16)
	botonb=ttk.Button(Submp, text="BAJA", width=29)
	botonb.place(relx=0.41, rely=0.23)
	botonc=ttk.Button(Submp, text="CONSULTA", width=29)
	botonc.place(relx=0.41, rely=0.30)
	botond=ttk.Button(Submp, text="MODIFICACIÓN", width=29)
	botond.place(relx=0.41, rely=0.37)
	botone=ttk.Button(Submp, text="VOLVER A ADMINISTRACIONES", width=29, command=Administraciones)
	botone.place(relx=0.41, rely=0.44)

def Volver_Menu():
	global Adm,Menu_p, Packed, Submp

	Unpack()
	Menu_p.pack(fill="both", expand=True)
	Packed="Menu_p"

def Menu():
	global Menu_p, Packed, root
	
	Menu_p=tk.Frame(root)
	Menu_p.pack(fill="both", expand=True)
	Packed="Menu_p"
	Menu_p.configure(width=800, height=500, padx=5, pady=5)
	ttk.Label(Menu_p, text="MENÚ PRINCIPAL", font=("arial",20)).place(relx=0.388, rely=0.04)
	boton1=ttk.Button(Menu_p, text="ADMINISTRACIONES", width=29, command=Administraciones)
	boton1.place(relx=0.41, rely=0.16)
	boton2=ttk.Button(Menu_p, text="ENTREGA DE CUPOS", width=29, command=lambda:Cupos('Cupos'))
	boton2.place(relx=0.41, rely=0.23)
	boton3=ttk.Button(Menu_p, text="RECEPCIÓN", width=29, command=lambda:Recepcion('Recepcion'))
	boton3.place(relx=0.41, rely=0.30)
	boton4=ttk.Button(Menu_p, text="REGISTRAR CALIDAD", width=29, command=lambda:Calidad('Calidad'))
	boton4.place(relx=0.41, rely=0.37)
	boton5=ttk.Button(Menu_p, text="REGISTRAR PESO BRUTO", width=29, command=lambda:PBruto("PBruto"))
	boton5.place(relx=0.41, rely=0.44)
	boton6=ttk.Button(Menu_p, text="REGISTRAR DESCARGA", width=29, command=lambda:Descarga("Descarga"))
	boton6.place(relx=0.41, rely=0.51)
	boton7=ttk.Button(Menu_p, text="REGISTRAR TARA", width=29, command=lambda:Tara("Tara"))
	boton7.place(relx=0.41, rely=0.58)
	boton8=ttk.Button(Menu_p, text="REPORTES", width=29, command=Reportes)
	boton8.place(relx=0.41, rely=0.65)
	boton9=ttk.Button(Menu_p, text="LISTADO DE SILOS Y RECHAZOS", width=29, command=Listado)
	boton9.place(relx=0.41, rely=0.72)
	boton0=ttk.Button(Menu_p, text="FIN DEL PROGRAMA", command=salirAplicacion, width=29)
	boton0.place(relx=0.41, rely=0.79)

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

def Menu_Pat():
	global Pat, root, Patente, Packed, Menu_p

	Unpack()
	Pat=tk.Frame(root)
	Pat.pack(fill="both", expand=True)
	Packed="Pat"
	Pat.config(width=800, height=500, padx=5, pady=5)
	ttk.Label(Pat, text="INGRESO DE PATENTE", font=("arial",20)).place(relx=0.3, rely=0.04)
	Patente=tk.StringVar()
	CuadroPat=tk.Entry(Pat, textvariable=Patente, justify="center", width=20).place(relx=0.41, rely=0.16, height=30)
	Send_button=ttk.Button(Pat, text="Validar", command=Valida_pat, width=8).place(relx=0.30, rely=0.16)
	botonmenu=ttk.Button(Pat, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).place(relx=0.36, rely=0.25)
def Valida_pat():
	global Patente, Packed, Menu_p, Op

	X=Patente.get()
	if(X=='V') or (X.isalnum()==True) and (len(X)==6) or (len(X)==7):
		Unpack()
		if(Op=="Cupos"):
			Cupos(None)
		elif(Op=="Recepcion"):
			Recepcion(None)
		elif(Op=="Calidad"):
			Calidad(None)
		elif(Op=="PBruto"):
			PBruto(None)
		elif(Op=="Descarga"):
			Descarga(None)
		elif(Op=="Tara"):
			Tara(None)

	else:
		valor=messagebox.askretrycancel("Patente inválida", "¿Desea intentarlo nuevamente?")
		if valor==False:
			Unpack()
			Packed="Menu_p"
			Menu_p.pack(fill="both", expand=True)
	
def Cupos(Opcion_Menu):
	global Packed, Cup, Op

	if(Opcion_Menu=="Cupos"):
		Op=Opcion_Menu
		Opcion_Menu=""
		Menu_Pat()
	else:
		Cup=tk.Frame(root)
		Cup.pack(fill="both", expand=True)
		Cup.config(width=800, height=500, padx=5, pady=5)
		Packed="Cup"
		Title=ttk.Label(Cup, text="ENTREGA DE CUPOS", font=("arial",20)).place(relx=0.34, rely=0.04)
		botonmenu=ttk.Button(Cup, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).place(relx=0.388, rely=0.5)

def Recepcion(Opcion_Menu):
	global Packed, Rec, Op

	if(Opcion_Menu=="Recepcion"):
		Op=Opcion_Menu
		Opcion_Menu=""
		Menu_Pat()
	else:
		Rec=tk.Frame(root)
		Rec.pack(fill="both", expand=True)
		Rec.config(width=800, height=500, padx=5, pady=5)
		Packed="Rec"
		Title=ttk.Label(Rec, text="RECEPCIÓN", font=("arial",20)).place(relx=0.40, rely=0.04)
		botonmenu=ttk.Button(Rec, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).place(relx=0.388, rely=0.5)

def Calidad(Opcion_Menu):
	global Packed, Cal, Op

	if(Opcion_Menu=="Calidad"):
		Op=Opcion_Menu
		Opcion_Menu=""
		Menu_Pat()
	else:
		Cal=tk.Frame(root)
		Cal.pack(fill="both", expand=True)
		Cal.config(width=800, height=500, padx=5, pady=5)
		Packed="Cal"
		Title=ttk.Label(Cal, text="REGISTRAR CALIDAD", font=("arial",20)).place(relx=0.33, rely=0.04)
		botonmenu=ttk.Button(Cal, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).place(relx=0.388, rely=0.5)
		
def PBruto(Opcion_Menu):
	global Packed, PBru, Op

	if(Opcion_Menu=="PBruto"):
		Op=Opcion_Menu
		Opcion_Menu=""
		Menu_Pat()
	else:
		PBru=tk.Frame(root)
		PBru.pack(fill="both", expand=True)
		PBru.config(width=800, height=500, padx=5, pady=5)
		Packed="PBru"
		Title=ttk.Label(PBru, text="REGISTRAR PESO BRUTO", font=("arial",20)).place(relx=0.29, rely=0.04)
		botonmenu=ttk.Button(PBru, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).place(relx=0.388, rely=0.5)	

def Descarga(Opcion_Menu):
	global Packed, Des, Op

	if(Opcion_Menu=="Descarga"):
		Op=Opcion_Menu
		Opcion_Menu=""
		Menu_Pat()
	else:
		Des=tk.Frame(root)
		Des.pack(fill="both", expand=True)
		Des.config(width=800, height=500, padx=5, pady=5)
		Packed="Des"
		Title=ttk.Label(Des, text="REGISTRAR DESCARGA", font=("arial",20)).place(relx=0.32, rely=0.04)
		botonmenu=ttk.Button(Des, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).place(relx=0.388, rely=0.5)
		
def Tara(Opcion_Menu):
	global Packed, Tar, Op

	if(Opcion_Menu=="Tara"):
		Op=Opcion_Menu
		Opcion_Menu=""
		Menu_Pat()
	else:
		Tar=tk.Frame(root)
		Tar.pack(fill="both", expand=True)
		Tar.config(width=800, height=500, padx=5, pady=5)
		Packed="Tar"
		Title=ttk.Label(Tar, text="REGISTRAR TARA", font=("arial",20)).place(relx=0.358, rely=0.04)
		botonmenu=ttk.Button(Tar, text="VOLVER AL MENÚ PRINCIPAL", width=29, command=Volver_Menu).place(relx=0.388, rely=0.5)

def Reportes():
	pass

def Listado():
	pass




def main_window():
	global root
	root = tk.Tk()
	root.config(width=800, height=500, padx=5, pady=5)
	root.title("Sistema de gestión para cerealeras")
	root.resizable(0,0)
	img = tk.PhotoImage(file="Fondo.png")
	style = darkstyle(root)
	Menu()
	root.mainloop()


main_window()