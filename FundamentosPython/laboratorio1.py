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
