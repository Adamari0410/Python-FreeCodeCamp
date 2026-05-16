#Cadenas:Secuencia de caracteres, en python estos estan dentro de comillas simples #o dobles
my_str_1='hello'
my_str_2="Wordl"

##Si se necesita una cadena de multiples lineas, podemos usar lo que es comillas t#riples
my_str_3='''Mi nombre es Lilian,
soy una persona muy feliz'''

#Si tenemos lo que es comillas dentro de la cadena podemos realizar lo que es 
#1.- Usar comillas opuestas
name="me llamo 'Paola'"
#2. Usar lo que es "\"
descripcion="Ella tiene cabello \"morado\""

#Para verificar si una subcadena pertenece a una cadena se usa lo que es el in
comida_favorita="Mi comida favorita es el ceviche"
print("la cadena comida_favorita contiene:" , comida_favorita)
print("La palabra 'comida' esta dentro de la cadena?")
print("comida" in comida_favorita)

#Para revizar el tamano de la cadena se usa la fucion "len()"

print("La longitud de la cadena comida_favorita es:",len(comida_favorita))

#Para revizar que letra ocupa un indice se usa corchetes, tener en cuenta que los #indices empiezan desde el numero 0.


print("La letra que se ubica en el indice 4 es :", comida_favorita[4])

#Se puede acceder al ultimo caracter de una cadena con -1


print("La letra que se ubica en el ultimo indice  es :", comida_favorita[-1])

saludo='hola'
saludo='hello'
print(saludo)

#No se puede realizar saludo[0]=H

#-------------Que son las concatenaciones de cadenas y la interpolacion de cadenas
#1. COncatenacion de cadenas

my_str1='hola'
my_str2='lilian'

concatenacion=my_str1+"  " + my_str2

print(concatenacion)

#Esto solo funciona con cadenas

#Si queremos concatener un int con una cadena usamos lo que es str() para converti#r un entero a cadena

my_str3="Cuantos hijos tienes?"
cantidad_hijos=4

tengo_hijos=my_str3+' '+str(cantidad_hijos)
print(tengo_hijos)


#Tambien se puede usar lo que es += para la concatenacion

my_str3+=str(cantidad_hijos)

print(my_str3)

#-----Interpolacion de cadenas---------------------------
#Lo usamos para poder inserta variables o expresiones en una cadena

nombre='Luhana'
age=4

name_age= f'Mi nombre es {nombre}, mi edad es de {age} '

print(name_age)


#=================Que es el corte de cadenas y como funciona=====================
#Este extrae una parte de la cadena 

mi_nombre='Luhana Flores'

print(mi_nombre[0:5]) # Esto solo te muestra la la sub cadena Paola
#Tambien podemos incluir un tercer parametro, que nos ayudara a modificar el incre#mento

print(mi_nombre[0: : 2])


#==========Cuales son algunos metodos comunes de cadenas=========================

#1.Upper(): Convierte una cadena en MAYUSCULA

print(mi_nombre.upper())

#2.lower(): Devuelve una cadena con todos los caracteres convertidos en minusculas

print('Mi mobre convertido en minusculas es:'+mi_nombre.lower())

#3. strip(): Elimina los caracteres de inicio y final, si no se le pasa argumento elimina los espacios en blanco del inicio y fin

texto=('Me gusto la manzana')

print('Resultado usando strip para eliminar la a: '+ texto.strip('Me gusto'))

#4. replace(): Se usa para remplazar palabras de la cadena

texto=('amo el pollo, tambien amo la salsa')

print('Texto sin usar lo que es replace: ' +texto)

print('Texto usando lo que es replace cambiando amo por odio:'+ texto.replace('amo','odio'))


#5. split(): Divide una cadena en una lista de cadenas de acuerdo a un separador

ingredientes=('pescado, limon, camote, maiz, lechuga,cilandro')
print('Como esta organizado ingredientes antes de usar split:'+ingredientes )
print(ingredientes.split(','))

#6. join(): 

lista_ingredientes=ingredientes.split(',')

print(''.join(lista_ingredientes))

#7. startwith():De vuelve verdadero o falso para verificar si una cadena empieza con el prefijo

prefijo= mi_nombre.startswith('Luhana')
print('mi nombre empieza con Paola?: ')
print(prefijo)

#8. endswith(): Devuelve verdadero o falso si el sufijo esta en la cadena

print('mi nombre termina en Flores?')

print(mi_nombre.endswith('Flores'))

#9. find(): Devuelve el indice de la cadena que se esta buscando

print(mi_nombre.find('Flores'))

#10. count(); Devuelve el numero de veces que aparece una sub cadena en la cadena 

print('El numero de veces que aparece la letra a en mi nombre es: ' +str(mi_nombre.count('a')))

#11. capitalize():Devuelve la cadena con la primera letra en mayuscula 

prueba='paola'

print(prueba.capitalize())

#12. isupper(): Devuelve True si todas las letras son mayusculas en la cadena

print(prueba.isupper())

#13. islower(): Devuelve true si las letras son minusculas de la cadena 


print(prueba.islower())

#14. title(): Devuelve una cadena con cada palabra con mayuscula

print(ingredientes.title())
