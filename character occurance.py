string = input("Please enter a word: ")
char = input("input character: ")
i = 1
count = 1
while(i < len(string)):
    if(string[i] == char):
     count = count + 1
    i = i + 1
print("total number of times", char, "has occured =" , count)