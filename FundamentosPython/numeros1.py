#============================Como trabajas con enteros y numero de punto flotante?=========================================


#Con estos se puede realizar lo que son operaciones matematicas 
#1.Enteros: Son numeros sin punto decimal, ya sean positivos o negativos 

my_int_1=56
my_int_2=-4

print ("Imprimimos el tipo de dato de my_int_1 y my_int_2")
print (type(my_int_1))

print (type(my_int_2))

#1.1. Suma de enteros

suma = my_int_1+my_int_2

print (f'La suma es: {suma}')

#1.2. Resta en python

resta= my_int_1-my_int_2

print (f'La resta es: {resta}')

#1.3.Multiplicacion

multiplicacion=my_int_1*my_int_2

print (f'La multiplicacion es: {multiplicacion}')


#1.4. Division

division=my_int_1/my_int_2


print (f'La division es: {division}')

#2. Numeros flotantes 

my_float_1=-12.0
my_float_2=4.9

print(type(my_float_1))

print(type(my_float_2))

print ("Imprimimos el tipo de dato de my_float_1 y my_float_2")


#2.1. Suma de flotantes

suma = my_float_1+my_float_2

print (f'La suma es: {suma}')

#2.2. Resta en python

resta= my_float_1-my_float_2

print (f'La resta es: {resta}')

#2.3.Multiplicacion

multiplicacion=my_float_1*my_float_2

print (f'La multiplicacion es: {multiplicacion}')


#2.4. Division

division=my_float_1/my_float_2


print (f'La division es: {division}')

#Si sumas un entero con un float, el resultado es de tipo float

suma_1=my_float_1 +my_int_1

print(type(suma_1))

#Modulo en python

modulo_int=my_int_1%my_int_2
modulo_float=my_float_1%my_float_2

print(f'El modulo entero es: {modulo_int}')
print(f'El modulo flotante es: {modulo_float}')

#Division entera

division_entera_int=my_int_1//my_int_2
division_entera_float=my_float_1//my_float_2

print(f'La division entera de int : {division_entera_int}')
print(f'La division flotante de float es: {division_entera_float}')

#Potencia


exp_int=my_int_1**my_int_2
exp_float=my_float_1**my_float_2


print(f'La potencia de  enteros es: {exp_int}')
print(f'La potencia de float es: {exp_float}')

#================FUNCIONES DE CONVERSION==========================
#Funcion float(argumento)
con_float=float(my_int_1)
print(con_float)
print(type(con_float))

#Funcion int(argumento)
con_int=int(my_float_1)
print(con_int)
print(type(con_int))

#!Se puede usar lo mismo para convertir una cadena de numeros a int o float
#Funcion round(): Redondea

my_int_3=4.456
my_int_4=5.183

redondear_int_3=round(my_int_3)
redondear_int_4=round(my_int_4,1)

print(redondear_int_3)
print(redondear_int_4)

#Funcion abs(): De vuelve el valor absoluto de un numero

my_numero_5=-5.34

absoluto_5=abs(my_numero_5)

print(absoluto_5)

#Funcion pow():Eleva un numero a la potencia

potencia=pow(5,2)

print(potencia)#25
#tambien se puede usar de forma modular

potencia_1=pow(5,2,10)
print(potencia_1)#5#tambien se puede usar de forma modular
