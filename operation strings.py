string1 = input("enter own string: ")
string2 = ('')
for i in string1:
    string2 = i + string2
print("\nthe original string = ", string1)
print("\nthe reverse string = ", string2)