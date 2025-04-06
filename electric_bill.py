units =int(input("enter units consumed: "))
if(units<50):
    amount = units *2.60
    surcharge = 25
elif(units<=100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge =35