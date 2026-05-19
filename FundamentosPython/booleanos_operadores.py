

#Como funcionan las declaraciones condicionales y los operadores logicos

print(3>4)#False
print(3<4)#True
print(3==4)#False
print(3!=4)#True
print(3>=4)#False
print(3<=4)#True

#Condicional mas basico es if:

age=18

if age>=18:

    print('You are an adult') #You are an adult
#En el ejeplo de arriba es importante la identacion caso contrario sale error
#Se recomienda usar 4 espacios


#Ahora realizamos la condicional con else

if age>=18:
    print('You are an adult')
else:
    print('You are not adult')

#Ahora usamos las clausulas elif para usar mas condiciones


if age>=65:
    print('Usted es adulto mayor')
elif age>=40:
    print('Usted tiene mas de 40 anios')
elif age>=30:
    print('Usted tienen  mas de 30 anios')
else:
    print ('Usted es joven')



#Que son los valores Truthy y Falsy, y como funciona los operadores booleanos y cortocircuito?

#Anidados 

is_citizen=True
age_1=25

if is_citizen:
    if age>=18:
        print('You are citizen an you are an adult')
else:
    print('You are not citizen')

#La funcion bool funciona para ver si un valor es falso o verdadero

print(bool(False))#false
print(bool(True))#True

#Tambien se tiene lo que son los operadores booleanos que son: AND, OR, NOT
#1. AND

if is_citizen and age>=18:
    print('You are citizen and you are an adult')
else:
    print('You are not citizen')


#2. Or

age_2=19

is_student=True

if age<18 or is_student:
    print('Usted es un estudiante')
else:
    print('Usted no es un estudiante')



#3. NOT: Este convierte valores de True a false(viceversa)

print(not '')#True
print(not 'Hello')#False


