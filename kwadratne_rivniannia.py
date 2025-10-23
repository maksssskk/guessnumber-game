import math

print("\033[1;33mHi!\033[0m\nYou're in quadratic equation solver!\nPlease, enter numbers 🧮 ")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a != 0:
    delta = b**2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        print(f"First solution: {x1}, Second solution: {x2}")
    elif delta == 0:
        x = -b / 2 * a 
        print(f"Solution: {x}")
    else:
        print("Has no solution!")
elif a == 0:
    if b != 0:
        x = -c / b
        print(f"Solution: {x:.2f}")
    elif b == 0:
        if c != 0:
            print("Has no solution!")
        elif c == 0:
            print("x є R")