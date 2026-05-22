#Como funcionan las funciones en python
#1. input(): Nos permite ingresar entrada del usuario
paola=input('ingrese su nombre')

print(type(paola))
#2. Tambien pordemos nuestras propias funicnes perzonalisadas como ejn el siguiente ejemplo

def saludo():
    print('Hola, como estas')
saludo()
#3. Funcion con parametros

def suma (a, b): #parametros
    print(f'La suma de {a} y {b} es : {a+b}')
suma(5,7)#argumentos
#4. COn return

def suma_calculadora(a,d):
    return a+d

suma_final=suma_calculadora(5,7)
print(suma_final)


#Que es el ambito (scope) en python y como funciona?
"""
Este ambito controla la vida vida util de una variable,
como se accede a esta desde diferentes puntos
del codigo.  
    
para determina corectamente el  ambito, python sigue la LEGB:
-Ambito local (l): Variables definidas en funicones o clase
-Ambito envolvente(E):Variables defnidas en funciones anidadas o de cierre
-Ambito global: Variables definidas al nivel superior del modulo o archivo
-Ambito incoporado9B): Nombres reservados en python para funciones, modulos, palabra clave y objetos 
predefnidos.    
"""
#1. Ambito local:La variable solo puede ser accedida desde una funcion o clase.
def my_func():
    my_var=10
    print (my_var) # my_var solo funciona desde la funcion

#2. Ambito envolvente;Una funcion dentro de otra funcion puede acceder a las variables de 
#la funcion superios, pero las funciones externaas,no pueden acceder a las funciones
#anidadas

def outer_func():
    msg ="Hello there!"
    def inner_func():
        print(msg)
    inner_func()
outer_func()
#-Ejemplo con nonlocal

def apellidos():
    apellido="Linares"
    def paola():
        nonlocal nombre
        nombre="Paola"
        print(apellido)
    
    nombre="Paola"
    print(nombre)

apellidos()

#3. Ambito global: Variables que se declara fuera de una funcion o clase,
#se puede acceder  desde cualquier parte del programa

my_global=1200

def imprimir():
    print(my_global)

print(my_global)

#-Siqueremos que una variable que esta en una funcion se ccesible de forma global 
# usamos la palabra global

my_var_1=7
def mostrar_variables():
    
    print(my_var_1)
    
    global my_var_2
    my_var_2=10
    
    print (my_var_2)
mostrar_variables()
    
print(my_var_2)

#Tambien la podemos usar para modificar una palabra global

def mostrar_variable():
    global my_var_1
    my_var_1=30

mostrar_variable()
print(my_var_1)
#4. el ambito incorporado son todas aquellas funciones que ya estan definidas previamente
print(str(45))
print(type(5))
    

