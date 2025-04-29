def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q
print("select operation")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice = input("enter choice(a/b/c/d): ")
num = int(input("enter num 1: "))
num1 = int(input("enter num2: "))
if choice == 'a':
    print("num" + "num1" "= ", add(num, num1))
elif choice == 'b':
    print("num" - "num1" "= ", subtract(num, num1))
elif choice == 'c':
    print("num" * "num1" "= ", multiply(num, num1))
elif choice == 'd':
    print("num" / "num1" "= ", divide(num, num1))
else: 
    print("invalid")