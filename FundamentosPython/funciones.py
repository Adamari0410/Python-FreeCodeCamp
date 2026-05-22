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