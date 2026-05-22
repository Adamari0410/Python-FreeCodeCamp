def apply_discount(price, discount):
    
    
    if not isinstance(price,(int, float)):
         return ('The price should be a number')
        
    elif not isinstance(discount,(int, float)):
         return ('The discount should be a number')
           
    elif price<= 0:
         return('The price should be greater than 0')
         return 1
    elif discount < 0 or discount > 100 :
         return ('The discount should be between 0 and 100')
         return 1
    price-=price*0.010*discount
    
    return price
    
descuento=apply_discount(100,20)
print(f'El descuento es: {descuento}')