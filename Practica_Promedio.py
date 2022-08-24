# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Definimos las variables
	terminos = int()
	suma = float()
	contador = int()
	promedio = float()
	# Se pregunta cuantos terminos son para obtener el promedio
	print("Ingrese la cantidad de teminos que desea promediar:")
	terminos = int(input())
	# Se inicia en cero la suma
	suma = 0
	# Se utiliza la estructura "Para" para llevar un control de los cantidad de 
	# terminos que nos indicaron en un principip y asi poder pedir los datos.
	# y se van acomulando en la variable de suma para despues hacer una division
	# de suma entre el numero de terminos y asi poder obtener el promedio
	for contador in range(1,terminos+1):
		print("Ingrese la cantidad ",contador,":")
		cantidad = float(input())
		suma = suma+cantidad
	# Se le asigna a la variable promedio el valor de la division de suma entre promedio
	promedio = suma/terminos
	# Se muestra en pantalla el resultado
	print("El promedio es: ",promedio)

