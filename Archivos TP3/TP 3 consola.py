from ast import If, Pass, While
from codecs import Codec
import os, pickle, os.path,sys,datetime,io
from re import A
from datetime import date
from datetime import datetime
from colorama import init, Fore, Back, Style

class Productos():

    def __init__(self):
        self.Cod = ''
        self.Prod= ''
        self.Estado= 'A'

class Cupo():

    def __init__(self):
        self.Patente = ''
        self.Agno = 0
        self.Mes = 0
        self.Dia = 0
        self.Estado = ''
        self.Cod = -1
        self.Bruto = 0
        self.Tara= 0

    def Busqueda_Cupos(self,Pat,Agno,Mes,Dia,Estado1,Estado2):
        global ArcFisiOp, ArcLogOp

        Agno,Mes,Dia = str(Agno),str(Mes),str(Dia)
        t=os.path.getsize(ArcFisiOp)
        ArcLogOp.seek(0)
        Reg=Cupo()
        while ArcLogOp.tell() < t:
            Reg=pickle.load(ArcLogOp)
            if(Reg.Patente.strip()==Pat):
                if(Reg.Agno==Agno) and (Reg.Mes==Mes) and (Reg.Dia==Dia):
                    if(Estado1==''):
                        return -1 # Hay otro camión cargado
                    else:
                        if(Reg.Estado==Estado1):
                            if(Estado2!=''):
                                Reg.Estado=Estado2
                                Reg.Guardar_Cambios()
                                return 2 # Todo ok y cambiado
                        else:
                            return 1 # Estado y fecha validados
    
    def Guardar_Cambios(self):

        Formateo_Cupo(self)
        with open(ArcFisiOp,"wb") as f:
            pickle.dump(self, f)

class Rubros():

    def __init__(self):
        self.CodR = -1
        self.Nombre = ''
    

    def Val_nombre(self):
        
        Nom=str(input(Fore.CYAN+Style.BRIGHT+'\n[V- Para volver al menú anterior] <Hasta 30 carácteres> Ingrese el nombre del rubro: ').capitalize())
        Carac=len(Nom)
        if(Nom=='V') or (Carac<30):
            return Nom
        else:
            os.system("cls")
            return True  

    def Alta(self,NombreR,CodR):
        pos=self.Busqueda(NombreR,CodR)
        if(pos==-1):
            ArcLogRubros.seek(0)
            self.Nombre=NombreR
            self.CodR=CodR
            self.Formateo()
            pickle.dump(self, ArcLogRubros)
            ArcLogRubros.flush()
            return -1 # No están en uso
        elif(pos==1):
            return 1 # Ya está cargado exactamente igual
        elif(pos==2):
            return 2 # Código en uso
        elif(pos==3):
            return 3 # Nombre en uso

    def Listado(self):

        os.system("cls")
        t = os.path.getsize(ArcFisiRubros)
        if t==0:
            input("[Enter para volver al menú anterior] - No hay productos cargados!")
        else:
            ArcLogRubros.seek(0,0)
            print("+--------------------+----------+")
            print("|Rubro               |Código    |")
            print("+--------------------+----------+")
            while ArcLogRubros.tell() < t:
                self=pickle.load(ArcLogRubros)
                Rubro = self.Nombre.strip()
                CodR = self.CodR.strip()
                Muestra = "|{:<20}|{:>10}|".format(Rubro, CodR)
                print(Muestra)
                print("+--------------------+----------+")

    def Formateo(self):
        self.Nombre = str(self.Nombre)
        self.Nombre = self.Nombre.ljust(30, ' ')
        self.CodR = str(self.CodR)
        self.CodR = self.CodR.ljust(1)

    def Busqueda(self,Nom,Cod):
        global ArcFisiRubros, Puntero
        t=os.path.getsize(ArcFisiRubros)
        ArcLogRubros.seek(0)
        while ArcLogRubros.tell() < t:
            Puntero=ArcLogRubros.tell() #Lo dejé por si se usa a futuro
            self=pickle.load(ArcLogRubros)
            if(self.CodR.strip() == Cod):
                if(self.Nombre.strip() == Nom):
                    return 1 # Nombre y código usados
                else:
                    return 2 # Código usado
            elif(self.Nombre.strip() == Nom):
                return 3 # Nombre usado

        return -1 #No hay coincidencias

class Silos(): # Terminar
    
    def __init__(self):
        self.CodS= 0
        self.Nombre=''
        self.CodP=0
        self.Stock=0

class RubrosxProd(): # Terminar
    
    def __init__(self):
        self.CodR = 0            # Ej 1 Humedad, 2 Girasol, 3 Maíz, 4 Soja y 5 Trigo
        self.CodP = 0            # Ej 1 Cebada, 2 Girasol, 3 Maíz, 4 Soja y 5 Trigo
        self.ValMin = 0.0
        self.ValMax = 100.0
    

    def Alta(self):
        # Pedir código del producto
        # Listar los rubros dependiendo del producto ingresado
        pass

def ValidarEnteros(nro, min, max):
    try:
        nro = int(nro)
        if nro >= min and nro <= max:
            return False
        else:
            return True
    except:
        return True

def ValidarPat():
    print(f'''{Fore.CYAN+Style.BRIGHT}-------------INGRESE LA PATENTE DEL VEHÍCULO-------------
{Fore.RED+Style.BRIGHT}<Debe ser alfanumérica y tener entre 6 y 7 carácteres>
{Fore.CYAN+Style.BRIGHT}---------------------------------------------------------{Style.RESET_ALL}''')
    Patente=str(input(Fore.CYAN+Style.BRIGHT+'\nPatente del vehículo [V- Para volver al menú anterior]: ').upper())
    Carac=len(Patente)
    if(Patente=='V') or ((Patente.isalnum()==True) and (Carac==6) or (Carac==7)):
        return Patente
    else:
        os.system("cls")
        return True

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
    global ArcFisiProd, ArcLogOp, ArcFisiOp, ArcLogRubros, ArcFisiRubros, ArcLogRubrosXProd, ArcFisiRubrosXProd, ArcLogSilos, ArcFisiSilos, ArcLogProd

    init(autoreset=True)

    ArcFisiOp = 'D:\Archivos_tp\OPERACIONES.DAT'
    if not os.path.exists(ArcFisiOp):
        ArcLogOp = open(ArcFisiOp, "w+b")
    else:
        ArcLogOp = open(ArcFisiOp, "r+b")
    
    ArcFisiProd = 'D:\Archivos_tp\PRODUCTOS.DAT'
    if not os.path.exists(ArcFisiProd):
        ArcLogProd = open(ArcFisiProd, "w+b")
    else:
        ArcLogProd = open(ArcFisiProd, "r+b")

    ArcFisiRubros = 'D:\Archivos_tp\RUBROS.DAT'
    if not os.path.exists(ArcFisiRubros):
        ArcLogRubros = open(ArcFisiRubros, "w+b")
    else:
        ArcLogRubros = open(ArcFisiRubros, "r+b")

    ArcFisiRubrosXProd = 'D:\Archivos_tp\RUBROS-X-PRODUCTOS.DAT'
    if not os.path.exists(ArcFisiRubrosXProd):
        ArcLogRubrosXProd = open(ArcFisiRubrosXProd, "w+b")
    else:
        ArcLogRubrosXProd = open(ArcFisiRubrosXProd, "r+b")
    
    ArcFisiSilos = 'D:\Archivos_tp\SILOS.DAT'
    if not os.path.exists(ArcFisiSilos):
        ArcLogSilos = open(ArcFisiSilos, "w+b")
    else:
        ArcLogSilos = open(ArcFisiSilos, "r+b")

    Menu()

def Menu():
    global ArcLogOp, ArcLogRubros, ArcLogRubrosXProd, ArcLogSilos

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
            Calidad()
        elif (Opc == 5):
            Peso_bruto()
        elif (Opc == 6):
            print('Proceso en construcción')
            input('<Enter para volver al menú principal>')
        elif (Opc == 7):
            Tara()
        elif (Opc == 8):
            Reportes()
        elif (Opc == 9):
            Listado()
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
                ArcLogOp.close()
                ArcLogRubros.close()
                ArcLogRubrosXProd.close()
                ArcLogSilos.close()
                input(Fore.CYAN+Style.BRIGHT+'\nGracias por usar este programa!')
            elif(Confirmación=='C'):
                Opc=-1

def Administraciones():
    
    Opci = ''
    while (Opci.upper() != 'V'):
        os.system("cls")
        Pantalla_Admin()
        Opci=str(input(Fore.CYAN+Style.BRIGHT+'\nIngrese la opción que desea operar: ').upper())
        while(Opci<'A' or Opci>'G') and (Opci!='V'):
            Opci = str(input(Fore.RED+Style.BRIGHT+'Opción incorrecta - Entre A y G [V para Volver]: ').upper())
        if(Opci == 'A') or (Opci == 'F') or (Opci == 'G'):
            print(Fore.RED+Style.BRIGHT+'Esta funcionalidad se encuentra en construcción!')
            Opci=input('V para volver: ').upper()
        elif(Opci == 'B'):
            Sub_menu_admin()
        elif(Opci == 'C'):
            Alta_rubro()
        elif(Opci == 'D'):
            Asign_rub()
        elif(Opci == 'E'):
            Alta_silo()

def Alta_rubro(): # Agregar bajas y modificaciones si queremos mejorarlo
    Opci=''
    while(Opci!='V'):
                os.system("cls")
                print(f'''{Fore.CYAN+Style.BRIGHT}----------------------------------
OPCION C - Alta de un rubro
----------------------------------{Style.RESET_ALL}''')
                Reg=Rubros()
                CodR=input("<Valor entero de hasta 2 cifras> - ¿Qué código desea asignarle al rubro?: ")
                while(ValidarEnteros(CodR,0,99)):
                    CodR=input("<Valor entero de hasta 2 cifras> - ¿Qué código desea asignarle al rubro?: ").upper()
                Nom=Reg.Val_nombre()
                while(Nom==True):
                    Nom=Reg.Val_nombre()
                if(Nom=='V'):
                    Opci='V'
                else:
                    res=Reg.Alta(Nom,CodR)
                    if(res==-1):
                        print("Rubro cargado correctamente!")
                    elif(res==2):
                        ArcLogRubros.seek(Puntero,0)
                        Reg=pickle.load(ArcLogRubros)
                        print(f"El código que elegiste ya fue utilizado en el rubro \"{Reg.Nombre.strip()}\"")
                    elif(res==1) or (res==3):
                        print("El rubro que intentas cargar ya existe!")
                        input("<Enter para volver al menú anterior>")
                    print()
                    Confir=input("¿Desea cargar otro rubro? Y/N: ").upper()
                    while(Confir!='Y') and (Confir!='N'):
                        Confir=input("¿Desea cargar otro rubro? Y/N: ").upper()
                    if(Confir=='N'):
                        Opci='V'

def Asign_rub(): # Agregar bajas y modificaciones si queremos mejorarlo
    global Cod

    Opci=''
    while(Opci!='V'):
                os.system("cls")
                print(f'''{Fore.CYAN+Style.BRIGHT}----------------------------------
OPCION D - Asignación de un rubro a un producto
----------------------------------{Style.RESET_ALL}''')
                print()
                Reg=RubrosxProd()
                ArcLogRubrosXProd.seek(0)
                RegRub=Rubros()
                RegRub.Listado()
                print()
                CodR=input("Ingrese el código del rubro que desea asignar a un producto: ")
                res=RegRub.Busqueda('',CodR)
                while(res==-1):
                    os.system("cls")
                    RegRub.Listado()
                    print()
                    CodR=input("El código ingresado no le pertenece a ningún rubro, inténtelo nuevamente: ")
                    res=RegRub.Busqueda('',CodR)
                print()
                Reg.CodR=CodR
                #os.system("cls")
                Listado_total()
                print()
                ArcLogRubros.seek(Puntero,0)
                RegRub=pickle.load(ArcLogRubros)
                print(f"A qué producto quiere asignarle el rubro \"{RegRub.Nombre}\"?: ")
                print()
                ValidarCod('C', 'G', 'M', 'S', 'T', 'V') # Revisar que haya que hacerlo con un código entero, no char
                print()
                print("El rubro esperará una respuesta de \"sí o no\" o un valor numérico?")
                print("\'S\' para sí o no")
                print("\'N\' para un valor numérico")
                tmp=input("¿Qué respuesta recibirá el rubro?").upper()
                while(tmp!='S') and (tmp!='N'):
                    tmp=input("¿Qué respuesta recibirá el rubro?").upper()
                if(tmp=='N'): # Num
                    ValMin=input("[De 0 a 100] - Ingrese el valor mínimo que aceptará ese rubro: ")
                    while(ValidarFloats(ValMin,0,100)):
                        ValMin=input("[De 0 a 100] - Ingrese el valor mínimo que aceptará ese rubro: ")
                    Reg.ValMin=ValMin
                    ValMax=input("[De 0 a 100] - Ingrese el valor mínimo que aceptará ese rubro: ")
                    while(ValidarFloats(ValMax,0,100)):
                        ValMax=input("[De 0 a 100] - Ingrese el valor mínimo que aceptará ese rubro: ")
                    Reg.ValMax=ValMax
                    print(f'''El rubro número {CodR} ha sido asignado correctamente al producto {Prod}!
Aceptará valores entre {ValMin} y {ValMax}.
''')
                else: # BOOLEANA
                    tmp=input("El producto será válido en caso de recibir una respuesta de sí o de no? S/N").upper()
                    while(tmp!='S') and (tmp!='N'):
                        tmp=input("El producto será válido en caso de recibir una respuesta de sí o de no? S/N").upper()
                    if(tmp=='N'):
                        Reg.ValMax=0 # Ante "False" debería ser bueno el prooducto
                        Reg.ValMin=-1
                    else:
                        Reg.ValMax=1 # Ante "True" debería ser bueno el prooducto
                        Reg.ValMin=-1
                # Formatear
                Opci=''
                while(Opci!='V') and (Opci!='S'):
                    print('''
¿Qué desea hacer a continuación?

\'S\' para seguir
\'V\' para volver al menú anterior
''')
                    Opci=input("Opción: ").upper()

def Alta_silo(): # Seguir
    Opci=''
    while(Opci!='V'):
        os.system("cls")
        print(f'''{Fore.CYAN+Style.BRIGHT}----------------------------------
OPCION E - Alta de un silo
----------------------------------{Style.RESET_ALL}''')
        Listado_total()
        Opci=input('[V Para volver al menú de Administraciones] - ¿Para qué producto desea cargar un rubro?').upper()

def Sub_menu_admin():
    global ArcFisiProd
    
    Opci=''
    while(Opci!='V'):
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
        while(Opci!='A') and (Opci!='B') and (Opci!='C') and (Opci!='M') and (Opci!='V'):
            Opci=input("[V Para volver al menú anterior] - Error, ingrese una opción válida: ").upper()
        if(Opci == 'A'):
            Alta_prod()
        elif(Opci == 'B'):
            Baja_prod()
        elif(Opci == 'C'):
            print(f'''{Fore.CYAN+Style.BRIGHT}------------------------------
OPCION C - Consulta de productos
------------------------------{Style.RESET_ALL}''')
            Consulta_Prod()
            input('<Enter para volver al menú anterior>')
        elif(Opci == 'M'):
            Modificar_prod()

def ValidarFloats(nro, min, max):
    try:
        nro = float(nro)
        if nro >= min and nro <= max:
            return False
        else:
            return True
    except:
        return True

def Valida_prod(Prod): # En desuso de momento
    try:
        Prod=str(Prod).upper()
        if (Prod!='TRIGO' and Prod!='SOJA' and Prod!='MAÍZ' and Prod!='MAIZ' and Prod!='GIRASOL' and Prod!='CEBADA'):
            return True
        else:
            return False
    except:
        return True

def ValidarCod(l1, l2, l3, l4, l5 ,l6):
    global Prod,Cod

    Cod=input(f"[V - Para volver al menú anterior] Ingrese el código del producto a seleccionar: {Style.RESET_ALL}").upper()
    while (Cod != l1) and (Cod != l2) and (Cod != l3) and (Cod != l4) and (Cod != l5) and (Cod != l6):
        Cod=input(f"{Fore.CYAN+Style.BRIGHT}[V - Para volver al menú anterior] {Fore.RED+Style.BRIGHT} Error, el producto que seleccionó no es válido. <Intentelo nuevamente>: {Style.RESET_ALL}").upper()
    if(Cod=='C'):
        Prod='CEBADA'
    elif(Cod=='G'):
        Prod='GIRASOL'
    elif(Cod=='M'):
        Prod='MAÍZ'
    elif(Cod=='S'):
        Prod='SOJA'
    elif(Cod=='T'):
        Prod='TRIGO'

def Listado_total():
    Productos = [
    {
        "Producto": "CEBADA",
        "Código": "C",
    },
    {
        "Producto": "GIRASOL",
        "Código": "G",
    },
    {
        "Producto": "MAÍZ",
        "Código": "M",
    },    {
        "Producto": "SOJA",
        "Código": "S",
    },    {
        "Producto": "TRIGO",
        "Código": "T",
    },
]

    print("+--------------------+----------+")
    print("|Producto            |Código    |")
    print("+--------------------+----------+")
    for p in Productos:
        Producto = p["Producto"]
        Codi = p["Código"]
        Muestra = "|{:<20}|{:>10}|".format(Producto, Codi)
        print(Muestra)
        print("+--------------------+----------+")
        print()

def Busqueda_prod(p,x,e):
    global ArcLogProd

    t=os.path.getsize(ArcFisiProd)
    ArcLogProd.seek(0)
    Producto=Productos()
    while ArcLogProd.tell() < t:
        Puntero=ArcLogProd.tell()
        Producto=pickle.load(ArcLogProd)
        if(x=='Prod'):
            if(Producto.Prod.strip()==p):
                if(e!=''):
                    Producto.Estado=e
                    Formateo_Prod(Producto)
                    ArcLogProd.seek(Puntero,0)
                    pickle.dump(Producto, ArcLogProd)
                    ArcLogProd.flush()
                return Producto.Estado
        elif(x=='Cod'):
            if(Producto.Cod==p):
                if(e!=''):
                    Producto.Estado=e
                    Formateo_Prod(Producto)
                    ArcLogProd.seek(Puntero,0)
                    pickle.dump(Producto, ArcLogProd)
                    ArcLogProd.flush()
                    return Puntero
                else:
                    return Producto.Estado
    return -1

def Alta_prod():
    global Cod, Prod

    os.system("cls")
    print(f'''{Fore.CYAN+Style.BRIGHT}----------------------------------
OPCION A - Alta de un producto
----------------------------------{Style.RESET_ALL}''')
    Cod=''
    while(Cod!='V'):
        ArcLogProd.seek(0)
        Producto=Productos()
        Listado_total()
        ValidarCod('C', 'G', 'M', 'S', 'T', 'V')
        if(Cod!='V'):
            res=Busqueda_prod(Prod,'Prod','')
            if(res==-1):
                Producto.Prod=Prod
                Producto.Cod=Cod
                Formateo_Prod(Producto)
                pickle.dump(Producto, ArcLogProd)
                ArcLogProd.flush()
                print()
                print("Producto cargado correctamente!")
                print()
            elif(res=='I'):
                Busqueda_prod(Cod,'Cod','A')
                print()
                print("Producto cargado correctamente!")
                print()
            else:
                print()
                print("El producto ya se encuentra cargado!")
                print()
            Seguir=input("¿Desea cargar otro producto? Y/N: ").upper()
            while Seguir!='Y' and Seguir!='N':
                Seguir=input("¿Desea cargar otro producto? Y/N: ").upper()
            if(Seguir=='N'):
                Cod='V'
            os.system("cls")

def Baja_prod():
    global Prod, Cod
    
    os.system("cls")
    print(f'''{Fore.CYAN+Style.BRIGHT}-------------------------------
OPCION B - Baja de un producto
-------------------------------''')
    t = os.path.getsize(ArcFisiProd)
    if t==0:
        input("No hay productos cargados! <Enter para volver al menú anterior>")
    else:
        Cod=''
        while(Cod!='V'):
            print()
            Consulta_Prod()
            print()
            ValidarCod('C', 'G', 'M', 'S', 'T', 'V')
            if(Cod!='V'):
                res=Busqueda_prod(Cod,'Cod','I')
                if(res == -1):
                    print("El producto no se encontró en la lista!")
                else:
                    print("Producto dado de baja correctamente!")
                Cod=input("[V - Para volver al menú anterior] - Enter para dar de baja otro producto: ").upper()
                os.system("cls")

def Consulta_Prod():

    os.system("cls")
    t = os.path.getsize(ArcFisiProd)
    if t==0:
        input("[Enter para volver al menú anterior] - No hay productos cargados!")
    else:
        reg=Productos()
        ArcLogProd.seek(0,0)
        print("+--------------------+----------+")
        print("|Producto            |Código    |")
        print("+--------------------+----------+")
        while ArcLogProd.tell() < t:
            reg=pickle.load(ArcLogProd)
            if(reg.Estado=='A'):
                Producto = reg.Prod
                Cod = reg.Cod
                Muestra = "|{:<20}|{:>10}|".format(Producto, Cod)
                print(Muestra)
                print("+--------------------+----------+")

def Modificar_prod():
    global Prod, Cod, Productos

    os.system("cls")
    print(f'''{Fore.CYAN+Style.BRIGHT}----------------------------------------
OPCION M - Modificación de un producto
----------------------------------------{Style.RESET_ALL}''')
    t = os.path.getsize(ArcFisiProd)
    if t==0:
        print("No hay productos cargados!")
    else:
        Cod=''
        while(Cod!='V'):
            print()
            Consulta_Prod()
            print()
            ValidarCod('C', 'G', 'M', 'S', 'T', 'V')
            if(Cod!='V'):
                res=Busqueda_prod(Cod,'Cod','')
                if(res == -1): # Verifica que no esté cargado
                    print("El producto no se encontró en la lista!")
                    Cod=input('[V para salir] - Enter para  intentarlo nuevamente: ')
                elif(res ==  'I'):
                    print("El producto seleccionado ha sido dado de baja!")
                else:
                    CodAux=Cod
                    ProdAux=Prod
                    print(f"A continuación, seleccione el producto por el cuál desea sustituir {Prod}")
                    print()
                    Listado_total()
                    ValidarCod('C', 'G', 'M', 'S', 'T', 'V')
                    if(Cod!='V'):
                        res=Busqueda_prod(Cod,'Cod','')
                        if(res == -1): # Verifica que el segundo no esté cargado
                            Busqueda_prod(CodAux,'Cod','I') # Da de baja el primer producto
                            Producto=Productos()
                            Producto.Prod=Prod
                            Producto.Cod=Cod
                            Formateo_Prod(Producto)
                            pickle.dump(Producto, ArcLogProd)
                            ArcLogProd.flush()
                            print("Producto modificado correctamente!")
                            Cod=input("[V - Para volver al menú anterior] - Enter para modificar otro producto: ").upper()
                            os.system("cls")
                        elif(res=='I'):
                            Busqueda_prod(Cod,'Cod','A')
                            Busqueda_prod(CodAux,'Cod','I')
                        else:
                            print()
                            print(f"El producto por el que desea sustituir {ProdAux} ya se encuentra cargado.")
                            Cod=input("[V - Para volver al menú anterior] - Enter para modificar otro producto: ").upper
                            os.system("cls")

def Cupos(): #Para mejorar, podría haber opción de modificar el cupo en caso de equivocarse

    Patente=''
    while(Patente!='V'):
        os.system('cls')
        RegCup=Cupo()
        Patente=ValidarPat()
        while Patente==True:
            input('Error, la patente debe ser alfanumérica y tener entre 6 y 7 carácteres <Enter para intentarlo nuevamente>')
            os.system('cls')
            Patente=ValidarPat()
        if(Patente!='V'):
            Val_Fecha()
            if(RegCup.Busqueda_Cupos(Patente,Agno,Mes,Dia,'','')==-1):
                input("Cupo ya otorgado <Enter para volver al menú principal>")
                Patente='V'
            else:
                os.system("cls")
                print("¿De qué producto será la carga del camión?")
                print()
                Consulta_Prod()
                print()
                CodP=input("[V - Para volver al menú principal] - Ingrese el código del producto que cargará: ").upper()
                res=Busqueda_prod(CodP,'Cod','')
                while(res==-1):
                    if(CodP=='V'):
                        Patente='V'
                        res=0
                    else:
                        print("Error, el código de producto seleccionado no está cargado!")
                        CodP=input("[V - Para volver al menú principal] - Ingrese el código del producto que cargará: ").upper()
                        res=Busqueda_prod(CodP,'Cod','')
                print()
                if(CodP!='V'):
                    Revisión_cupo_creado(Patente,CodP,Agno,Mes,Dia)
                    print()
                    RegCup.Patente=Patente
                    RegCup.Cod=CodP
                    RegCup.Agno=Agno
                    RegCup.Mes=Mes
                    RegCup.Dia=Dia
                    RegCup.Estado='P'
                    Confir=input("¿Desea confirmar la creación del cupo? Y/N: ").upper()
                    while(Confir!='Y') and (Confir!='N'):
                        Confir=input("¿Desea confirmar la creación del cupo? Y/N: ").upper()
                    if(Confir=='Y'):
                        RegCup.Guardar_Cambios()
                        print('--------------------------')
                        print("Cupo creado exitosamente!")
                        print('--------------------------')
                        print()
                        Confir=input("¿Desea pedir un cupo para otro camión? Y/N: ").upper()
                        while(Confir!='Y') and (Confir!='N'):
                            Confir=input("¿Desea pedir un cupo para otro camión? Y/N: ").upper()
                        if(Confir=='N'):
                            Patente='V'
                    else:
                        pass # Opción de modificar la carga?
                
def Revisión_cupo_creado(Patente,CodP,Agno,Mes,Dia):
    os.system("cls")
    Datos = [
    {
        "Dato": "Patente",
        "Valor": Patente,
    },
    {
        "Dato": "Carga",
        "Valor": CodP,
    },
    {
        "Dato": "Fecha",
        "Valor": f"{Dia}/{Mes}/{Agno}",
    }
]

    print("+--------------------+----------+")
    print("|Dato                |Valor     |")
    print("+--------------------+----------+")
    for p in Datos:
        Dato = p["Dato"]
        Valor = p["Valor"]
        Muestra = "|{:<20}|{:>10}|".format(Dato, Valor)
        print(Muestra)
        print("+--------------------+----------+")
        print()

def Formateo_Prod(vrProd):

    vrProd.Prod = str(vrProd.Prod)
    vrProd.Prod = vrProd.Prod.ljust(7, ' ')
    vrProd.Estado = str(vrProd.Estado)
    vrProd.Estado = vrProd.Estado.ljust(1)
    vrProd.Cod = str(vrProd.Cod)
    vrProd.Cod = vrProd.Cod.ljust(1)

def Formateo_Cupo(vrCup):

    vrCup.Patente = str(vrCup.Patente)
    vrCup.Patente = vrCup.Patente.ljust(7, ' ')
    vrCup.Agno = str(vrCup.Agno)
    vrCup.Agno = vrCup.Agno.ljust(4, ' ')
    vrCup.Mes = str(vrCup.Mes)
    vrCup.Mes = vrCup.Mes.ljust(1, ' ')
    vrCup.Dia = str(vrCup.Dia)
    vrCup.Dia = vrCup.Dia.ljust(2, ' ')
    vrCup.Estado = str(vrCup.Estado)
    vrCup.Estado = vrCup.Estado.ljust(1)
    vrCup.Cod = str(vrCup.Cod)
    vrCup.Cod = vrCup.Cod.ljust(1)
    vrCup.Bruto = str(vrCup.Bruto)
    vrCup.Bruto = vrCup.Bruto.ljust(5, ' ')
    vrCup.Tara = str(vrCup.Tara)
    vrCup.Tara = vrCup.Tara.ljust(5, ' ')

def Val_Fecha():
    global Agno, Mes, Dia

    os.system("cls")
    now= datetime.now()
    max=now.year + 1
    print(f"[Enter para seleccionar el año actual: {now.year}] - Ingrese el año de llegada del camión: ")
    Agno=input(f"<No se puede pedir cupos para una fecha más lejana al año {max}>.  Año: ")
    if(Agno==''):
        Agno=now.year
    while ValidarEnteros(Agno,now.year,max):
        Agno=input("Error, no puede solicitar un cupo con más de un año de diferencia a la fecha actual. Inténtelo nuevamente:")
        if(Agno==''):
            Agno=now.year
    Agno=int(Agno)
    if(Agno==now.year):
        min=now.month
        max=12
        Mes=input(f"[Enter para seleccionar el mes actual: {now.month}] Ingrese el Mes de llegada del camión: ")
        if(Mes==''):
            Mes=now.month
    else:
        max=now.month
        min=1
        Mes=input(f"[De {min} a {max}] Ingrese el Mes de llegada del camión: ")
    while ValidarEnteros(Mes,min,max):
        Mes=input(f"Error, ingrese un mes válido![Entre {min} y {max}]:")
    Mes=int(Mes)
    if(Mes==1) or (Mes==3) or (Mes==5) or (Mes==7) or (Mes==8) or (Mes==10) or (Mes==12):
        max=31
    elif(Mes==2):
        max=28
    else:
        max=30
    if(Mes==now.month):
        if(Agno==now.year):
            min=now.day
            Dia=input(f"[Enter para seleccionar el Día de hoy: {now.day}] Ingrese el Día de llegada del camión: ")
            if(Dia==''):
                Dia=now.day
        else:
            max=now.day
            min=1
            Dia=input(f"[De {min} a {max}] Ingrese el día de llegada del camión: ")
    else:
        min=1
    while ValidarEnteros(Dia,min,max):
        Dia=input(f"[De {min} a {max}] Error, ingrese el día de llegada del camión: ")
    Dia=int(Dia)

def Recepción():

    Reg=Cupo()
    Patente=''
    while(Patente!='V'):
        os.system('cls')
        Patente=ValidarPat()
        while Patente==True:
            input('Error, la patente debe ser alfanumérica y tener entre 6 y 7 carácteres <Enter para intentarlo nuevamente>')
            os.system('cls')
            Patente=ValidarPat()
        now= datetime.now()
        res=Reg.Busqueda_Cupos(Patente,now.year,now.month,now.day,'P','A')
        if(res==2):
            print("Recepción realizada correctamente!")
            print()
            Confir=input("¿Desea recibir otro camión? Y/N: ").upper()
            while(Confir!='Y') and (Confir!='N'):
                Confir=input("¿Desea recibir otro camión? Y/N: ").upper()
            if(Confir=='N'):
                Patente='V'
        else:
            print("No hay ningún cupo guardado para este camión el día de hoy!")
            input("<Enter para volver al menú principal>").upper()
            Patente='V'
        
def Calidad():

    Reg=Cupo()
    Patente=''
    while(Patente!='V'):
        os.system('cls')
        Patente=ValidarPat()
        while Patente==True:
            input('Error, la patente debe ser alfanumérica y tener entre 6 y 7 carácteres <Enter para intentarlo nuevamente>')
            os.system('cls')
            Patente=ValidarPat()
        now= datetime.now()
        res=Reg.Busqueda_Cupos(Patente,now.year,now.month,now.day,'A','')
        # Evaluar cada rubro del producto dependiendo de la carga del camión
        # Print de cada rubro para ese producto en concreto y las medidas que debe pasar
        # Si no pasa dos rubros está rechazado
        # (Hay que ordenar rubros.dat de forma creciente por cod rubro)
        # Usar búsqueda dicotómica
        # Cambiar el estado a C


def Peso_bruto():
    os.system('cls')
    Patente=ValidarPat()
    while(Patente!='V'):
        while Patente==True:
            input('Error, la patente debe ser alfanumérica y tener entre 6 y 7 carácteres <Enter para intentarlo nuevamente>')
            os.system('cls')
            Patente=ValidarPat()
        input('Patente ya validada, seguir desde acá')

def Tara():
    os.system('cls')
    Patente=ValidarPat()
    while(Patente!='V'):
        while Patente==True:
            input('Error, la patente debe ser alfanumérica y tener entre 6 y 7 carácteres <Enter para intentarlo nuevamente>')
            os.system('cls')
            Patente=ValidarPat()
        input('Patente ya validada, seguir desde acá')

def Pantalla_Reportes():
    os.system('cls')
    print(f'{Fore.CYAN+Style.BRIGHT}------------MENÚ REPORTES------------')
    print(f'''{Style.RESET_ALL}\nA- Cantidad de cupos otorgados
B- Cantidad total de camiones recibidos
C- Cantidad total de camiones de cada producto
D- Peso neto total de cada producto
E- Peso neto total de cada producto
F- Promedio del peso neto de producto por camión de ese producto
G- Patente del camión de cada producto que menor cantidad de dicho producto cargó
V- Volver al MENU PRINCIPAL

{Fore.CYAN+Style.BRIGHT}---------------------------------------------{Style.RESET_ALL}''')

def Reportes():
    Opci=""
    while(Opci!='V'):
        Pantalla_Reportes()
        input('Seguir con el flujo del programa desde acá')
        Opci=input('V para volver: ').upper()

def Listado():
    Opci=''
    os.system('cls')
    while(Opci!='V'):
        print(f'{Fore.CYAN+Style.BRIGHT}------------Listado de Silos y Rechazados------------')
        print(f'''{Style.RESET_ALL}\nA- Mostrar el silo con mayor stock
B- Cantidad total de camiones recibidos
V- Volver al MENU PRINCIPAL

{Fore.CYAN+Style.BRIGHT}-----------------------------------------------------{Style.RESET_ALL}''')
        Opci=input('V para volver: ').upper()

#Yo agregaría una opción como la G pero del mayor, de onda nomas

# Recordar validar que el producto que tengan los camiones que se carguen esté en el archivo y que si no hay porductos cargados te mande a admin

### Programa Principal ###

Inicializar()