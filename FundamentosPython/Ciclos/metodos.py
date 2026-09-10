#~~~~~~~~~~~~~~~METODOS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#append():Agregar un elemento al final de la lista
paises=["Peru", 'Chile', 'Bolivia', 'Ecuador']
print("Antes de agregar: ", paises)
paises.append("Colombia")
print("Despues de agrega Colombia: ", paises)
#Tambien podemos usar append() para agregar una lista a otra
ciudades=['Lima', 'Bogota','Paracas','Santiago de Chile']
paises.append(ciudades)

print('Agregamos una lista de ciudades a la lissta paises', paises)

#Pero si queremos Agregaar todos los elementos de ciudades a paises
#usamos extend()
paises=["Peru", 'Chile', 'Bolivia', 'Ecuador']
paises.extend(ciudades)

print("Si queremos agregar los elementos de una lista a otra usamos extend:",paises)

#insert: Para insertar un dato en un indice especifico.

paises.insert(0, "Mexico")
print("Agregamos el pais Mexico en un indice especifico con insert", paises)

#remove: Para eliminar un elemento con su valor, solo elimina la primera ocurrencia que encuentra
ciudades.remove("Lima")
print('Eliminamos un elmento (Lima) con remove, este usa su valor ', ciudades)

#pop(): Para eliminar un elemento segun su indice
ciudades.pop(0)
print('De ciudades podemos eliminar Bogota usando el pop(0)', ciudades)

#clear(): Lo usamos para vaciar una lista
ciudades.clear()
print('Vaciamos una list ausando lo que es clear()', ciudades)

