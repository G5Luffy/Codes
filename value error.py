try :
    num = int(input("enter number: "))
    print(num)
except ValueError as ex:
    print("exception: ", ex)

print("I am outside the try block")