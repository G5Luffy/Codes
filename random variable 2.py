
import random

playing = True

number = str(random.randint(0, 100))

print("I will generate a random number from 0 to 100, and you will have to guess the number.")

print("The game ends when you get it right!")

while playing:

     guess = input("Give me your best guess \n")


if guess == number:

 print("You win the game!")
 print("The number was:", number)
 playing = False

else:

   print("Your guess was incorrect. Try again.\n") 