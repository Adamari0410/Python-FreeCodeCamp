"""
Para este laboratorio, usarás sentencias condicionales para determinar si es posible desplazarte según el clima,
la distancia a recorrer y la disponibilidad de un vehículo.
Objetivo: Cumplir con las historias de usuario a continuación y pasar todas las pruebas para completar el laboratorio.

User Stories:

Debes crear las siguientes variables:
distance_mi (un número que representa la distancia a recorrer en millas)
is_raining (un booleano que representa si el usuario está experimentando clima lluvioso actualmente)
has_bike (un booleano que representa si el usuario tiene una bicicleta)
has_car (un booleano que representa si el usuario tiene un coche)
has_ride_share_app (un booleano que representa si el usuario tiene una app que le permite solicitar un viaje)
Debes usar sentencias condicionales para determinar si es posible el desplazamiento basado en los valores de estas variables.
Debes usar las sentencias if, elif y else para evaluar las categorías de distancia en orden ascendente.
Si distance_mi es un valor falso:
Deberías imprimir False.
Si la distancia es menor o igual a 1 milla:
Debes imprimir True solo si no está lloviendo.
De lo contrario, deberías imprimir False.
Si la distancia es mayor que 1 milla y menor o igual a 6 millas:
Debes imprimir True solo si la persona tiene una bicicleta y no está lloviendo.
De lo contrario, deberías imprimir False.
Si la distancia es mayor a 6 millas:
Debes imprimir True si la persona tiene un coche o tiene una aplicación de viaje compartido.
De lo contrario, deberías imprimir False.

"""


distance_mi=5
is_raining=True
has_bike=True
has_car=True
has_ride_share_app=True



if distance_mi==False:
    print(False)
elif distance_mi <=1: 
    if is_raining==False:
        print(True)
    else:
        print(False)

if distance_mi>1 and distance_mi<=6:
    if has_bike==True  and  is_raining ==False :
        print(True)
    else:
        print(False)
elif distance_mi>6:
    if has_car==True or has_ride_share_app==True:
        print(True)
    else:
        print(False)
