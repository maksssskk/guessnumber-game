import random
import time

#hello
print("\033[1;33mHi!\033[0m\nYou`re in 'Guess Number' game!\nWanna play?😏")

#generating number
number = random.randint(1, 100)
num = None

while num != number:
    num = int(input("Print number: "))

        for char in text:
            print(char, end="", flush=True)
            time.sleep(0.03)
        print("\n") 
        
    if num < number:
        print("Little bit more")
    elif num > number:
        print("Ohh, less")
    elif num == number:
        print("You win!\nKoniec zabawy")
        break
