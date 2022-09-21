Algoritmo Cupos
	Leer Patente
	Mientras Patente!="V" Hacer
		Mientras Agno<2022 or Agno>2023 Hacer
			Leer Agno
		FinMientras
		Leer Mes
		Mientras Mes<1 or Mes>12 Hacer
			//Leer Mes
		FinMientras
		Leer Dia
		Mientras Dia<1 or Dia>31 Hacer
			Leer Dia
		FinMientras
		// Leer y ValCodProdCargado
		// ValCuposAnt
		self.Estado = 'P'
		// Formatear datos
		// pickle.dump y flush()
		Escribir "¿Desea continuar? S/N"
		Leer Continuar
		Si Continuar='N' Entonces
			Patente = 'V'
		FinSi
	FinMientras
FinAlgoritmo
