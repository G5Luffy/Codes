print("enter marks of 4 subjects")
math = int(input("maths: "))
science = int(input("science: "))
o_math = int(input("o_math: "))
english = int(input("english: "))
sum = math+science+o_math+english
print("Sum of all subjects: ", sum)
perc = (sum/400)*100
print(end = "Percent Mark = ")
print(perc)