numbers = [12, 8, 3, 2, 1]
print("Contenido de la lista:", numbers) 
numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)  

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)#Lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)

numbers[1] = numbers[4]#Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)#Imprimiendo contenido de la lista con intercambio.
print("\nLongitud de la lista:", len(numbers))#Longitud de la lista.
#Eliminando elementos
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)#Lista original.
numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)
numbers[1] = numbers[4]#Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)#Lista con intercambio.
print("\nLongitud de la lista:", len(numbers)) #Longitud de la lista.
del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.