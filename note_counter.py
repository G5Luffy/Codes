Amount = int(input("Enter withdrawl amount: "))
n1 = Amount//100
n2 = (Amount%100)//50
n3 = ((Amount%100)%50)//10
print("note of Rs.100 ", n1)
print("note of Rs.50 ", n2)
print("note of Rs.10 ", n3)