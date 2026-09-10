#El tipo de dato listas es una secuencia ordenada de elementos que pueden estar
# commpuestyos por cadenas ,numeros o inlcuso otra listas.
#Las listas son mutables y usan indexacion basada en cero, lo que significa que 
#el primer elemento de la lista esta en el indice cero
ciudades= ["Lima", "Arequipa", "Puno"]
#Para accedder a un elemento de la lista ciudades, puede referenciar su numero de
#indice en la secuencia. aqui tienes un ejemplo de como acceder al primer elemento
#de la lista ciudad
print(ciudades[0])
#El indexado negativo se usa para acceder des el fiunal de la lsita
print(ciudades[-1])

#Otra forma de convertir en lista es 
nombre='Luhana'
print(list(nombre))
#Importante un iterable es un tipo especial de objeto que puede ser recorrido
#uno por uno

#Para poder saber el total de elementos de la lista use len()
print(len(ciudades))

#Para poder modificar un elemento de la lista puedes realizar

nombre=['Luhana', 'Claudia', 'Mateo']
nombre[0]='Liliana'

print(nombre)

print("Eliminamos un nombre usando del")

del nombre[2]
print(nombre)

print("Para ver si un elemento esta en la lista usamos in")

print("Claudia esta en la lista nombre: ","Claudia" in nombre)
#Lista anidada

estudiante=["Katy",17,["Peru","Lima", "Cercado de Lima"]]
print(estudiante[1])
print(estudiante[2][1])

#Desempaquetar
profesor=["Juan", "Fisica", 35]

nombre, curso, edad=profesor

print(nombre)
print(curso)
print(edad)

#Recolectar elemento de la lista
secretario=["Jose", "dia", 39]
nombre, *otrosDatos=secretario

print(otrosDatos)

#Operador slice

numeros=[1,2,3,4,5,6,7,8,8]

print(numeros[0:7:2])