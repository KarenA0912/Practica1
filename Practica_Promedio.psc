Proceso Practica_Promedio
	
	//Definimos las variables
	Definir terminos Como Entero
	Definir suma Como Real
	Definir contador Como Entero
	Definir promedio Como Real
	
	//Se pregunta cuantos terminos son para obtener el promedio
	Escribir "Ingrese la cantidad de teminos que desea promediar:"
	Leer terminos
	
	//Se inicia en cero la suma
	suma <- 0
	
	//Se utiliza la estructura "Para" para llevar un control de los cantidad de 
	//terminos que nos indicaron en un principip y asi poder pedir los datos.
	//y se van acomulando en la variable de suma para despues hacer una division
	//de suma entre el numero de terminos y asi poder obtener el promedio
	
	Para contador<-1 Hasta terminos Hacer
		Escribir "Ingrese la cantidad ",contador,":"
		Leer cantidad
		suma <- suma + cantidad
	FinPara
	
	
	//Se le asigna a la variable promedio el valor de la division de suma entre promedio
	promedio <- suma / terminos
	
	//Se muestra en pantalla el resultado
	Escribir "El promedio es: ",promedio
	
FinProceso
