Algoritmo Tp3
	Escribir Inicializar
	Opc <- -1
	Mientras Opc!=0 Hacer
		Escribir Pantalla
		Leer Opc
		Segun Opc  Hacer
			9:
				Escribir Listado
			8:
				Escribir Reportes
			7:
				Escribir Tara
			6:
				Escribir 'Opción en mantenimiento!'
			5:
				Escribir Peso_bruto
			4:
				Escribir Calidad
			3:
				Escribir Recepcion
			2:
				Escribir Cupos
			1:
				Escribir Administraciones
			0:
				Escribir '¿Está seguro de que desea salir del programa?'
				Escribir 'S- Salir'
				Escribir 'C- Cancelar'
				Leer Confirmacion
				Mientras (Confirmacion!='N') Hacer
					Escribir 'Opción incorrecta, ingrese S para salir o C para cancelar'
					Leer Confirmacion
				FinMientras
				Si Confirmacion='S' Entonces
					Opc <- 0
				SiNo
					Opc <- -1
				FinSi
			De Otro Modo:
				Escribir 'Opción inválida, <Entre 0 y 9>'
				Leer Opc
		FinSegun
	FinMientras
FinAlgoritmo
