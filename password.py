import time
import random
import string

print("\033[1;33mHi!\033[0m\nYou're in password generator!\nPlease, enter:\n")
length = int(input("Length: "))
characters = string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()"

print("\nGenerating your secure password", end="", flush=True)
for i in range(3):         
    print(".", end="", flush=True)
    time.sleep(0.5)         
print("\n")

password = "".join(random.choice(characters) for _ in range(length))
time.sleep(0.5)
print("\033[1;32m✅ Done!\033[0m")
if length <=6:
    print("Weak password")
elif 6 < length <10:
    print("Little bit more")
elif length >= 10:
    print("Wow! Very strong password!")
time.sleep(0.3)
print(f"Your secure password is: \033[1;35m{password}\033[0m\n")
