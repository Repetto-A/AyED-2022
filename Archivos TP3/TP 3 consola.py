from ast import If, Pass
import os, pickle, os.path,sys,datetime,io
from datetime import date
from colorama import init, Fore, Back, Style

def ValidarEnteros(nro, min, max):
    try:
        nro = int(nro)
        if nro >= min and nro <= max:
            return False
        else:
            return True
    except:
        return True

def ValidarPat(Patente):
    Carac=len(Patente)
    if(Patente=='V'):
        return False
    elif(Patente.isalnum()==False) or (Carac<6) or (Carac>7):
        return True
    return False

def Pantalla():
	os.system('cls')
	print(f'''{Fore.CYAN+Style.BRIGHT}---------------MENÚ PRINCIPAL---------------''')
	print(f'''{Style.RESET_ALL}\n1- Administraciones
2- Entrega de cupos
3- Recepción
4- Registrar calidad
5- Registrar peso bruto
6- Registrar descarga
7- Registrar tara
8- Reportes
9- Listado de silos y rechazos
0- Fin del programa

{Fore.CYAN+Style.BRIGHT}--------------------------------------------{Style.RESET_ALL}''')

def Pantalla_Admin():
    os.system('cls')
    print(f'{Fore.CYAN+Style.BRIGHT}------------MENÚ ADMINISTRACIONES------------')
    print(f'''{Style.RESET_ALL}\nA- Titulares
B- Productos
C- Rubros
D- Rubros por producto
E- Silos
F- Sucursales
G- Producto por titular
V- Volver al MENU PRINCIPAL

{Fore.CYAN+Style.BRIGHT}---------------------------------------------{Style.RESET_ALL}''')

def Inicializar():
    global ArcLogAlu, ArcFisiAlu

    init(autoreset=True)
    ArcFisiAlu = 'D:\Ale\Programación\Proyectos\Alumnos.dat'
    if not os.path.exists(ArcFisiAlu):
        ArcLogAlu = open(ArcFisiAlu, "w+b")
    else:
        ArcLogAlu = open(ArcFisiAlu, "r+b")
    Menu()

def Menu():
    os.system("cls")
    Opc = -1
    while (Opc != 0):
        os.system("cls")
        Pantalla()
        Opc=input(Fore.CYAN+Style.BRIGHT+'\nIngrese la opción que desea operar: ')
        while (ValidarEnteros(Opc, 0, 9)):
            Opc = input(Fore.RED+Style.BRIGHT+'Opción incorrecta - Entre 0 y 9: ')
        Opc = int(Opc)
        if (Opc == 1):
            Administraciones()
        elif (Opc == 2):
            Cupos()
        elif (Opc == 3):
            Recepción()
        elif (Opc == 4):
            pass
        elif (Opc == 5):
            pass
        elif (Opc == 6):
            print('Proceso en construcción')
            input('<Enter para volver al menú principal>')
        elif (Opc == 7):
            pass
        elif (Opc == 8):
            pass
        elif (Opc == 9):
            pass
        else:
            print(Style.RESET_ALL+'')
            print('¿Está seguro de que desea salir del programa?')
            print(Fore.RED+Style.BRIGHT+'\nRecuerde que esta acción NO se puede deshacer')
            print('S- Salir')
            print('C- Cancelar')
            Confirmación=str(input(Style.RESET_ALL+'').upper())
            while(Confirmación!='S' and Confirmación!='C'):
                print('')
                print(Fore.RED+Style.BRIGHT+'Opción incorrecta, intentalo nuevamente: ')
                Confirmación=str(input().upper())
            if(Confirmación=='S'):
                ArcLogAlu.close()
                print(Fore.CYAN+Style.BRIGHT+'\nGracias por usar este programa!')
                input()
            elif(Confirmación=='C'):
                Opc=-1

def Administraciones():
    Opci = ''
    while ((Opci.upper()) != 'V'):
        os.system("cls")
        Pantalla_Admin()
        Opci=str(input(Fore.CYAN+Style.BRIGHT+'\nIngrese la opción que desea operar: ').upper())
        while(Opci<'A' or Opci>'G') and (Opci!='V'):
            Opci = str(input(Fore.RED+Style.BRIGHT+'Opción incorrecta - Entre A y G [V para Volver]: ').upper())
        if(Opci == 'A') or (Opci == 'F') or (Opci == 'G'):
            print(Fore.RED+Style.BRIGHT+'Esta funcionalidad se encuentra en construcción!')
            input()
        elif(Opci == 'B'):
            Sub_menu()
        elif(Opci == 'C') or (Opci == 'D') or (Opci == 'E'):
            print('A- ALTA')
            input()

def Sub_menu():
    os.system('cls')
    print(f'''{Fore.CYAN+Style.BRIGHT}--------------SUBMENÚ PRODUCTOS--------------
{Style.RESET_ALL}\nA- ALTA
B- BAJA
C- CONSULTA
M- MODIFICACION
V- VOLVER AL MENU ANTERIOR

{Fore.CYAN+Style.BRIGHT}---------------------------------------------
''')
    Opci=str(input().upper())
    while(Opci!='V'):
        if(Opci == 'A'):
            pass
        elif(Opci == 'B'):
            pass
        elif(Opci == 'C'):
            pass
        elif(Opci == 'M'):
            pass
        Opci='V'                              #Ya que está en construcción, fuerzo la salida al menú anterior

def Cupos():
    os.system('cls')
    print(f'''{Fore.CYAN+Style.BRIGHT}-------------INGRESE LA PATENTE DEL VEHÍCULO-------------
{Fore.RED+Style.BRIGHT}<Debe ser alfanumérica y tener entre 6 y 7 carácteres>
{Fore.CYAN+Style.BRIGHT}---------------------------------------------------------{Style.RESET_ALL}''')
    Patente=str(input(Fore.CYAN+Style.BRIGHT+'\nPatente del vehículo [V- Para volver al menú anterior]: ').upper())
    while(Patente!='V'):
        while ValidarPat(Patente):
            Patente=str(input(f'{Fore.RED+Style.BRIGHT}\nError, ingrese la patente del vehículo [V- Para volver al menú anterior]: {Style.RESET_ALL}').upper())
        input('Patente ya validada, seguir desde acá')
        Patente='V'                                      #Fuerzo que vuelva al menú principal porque está en construcción todavía

# Recordar validar que el producto que tengan los camiones que se carguen esté en el archivo y que si no hay porductos cargados te mande a admin

def Recepción():
    os.system('cls')


### Programa Principal ###

Inicializar()