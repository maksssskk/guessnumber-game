import time

sentence = input("Sentence: ")
sen = (sentence.lower()).replace(" ", "")
        
print("\nThinking in this 🤔", end="", flush=True)
for i in range(3):         
    print(".", end="", flush=True)
    time.sleep(0.5)         
print("\n")

if sen.isalpha() == True:
    if sen == sen[::-1]:
        print("This sentence is palidrom ✅")
    else:
        print("What a pitty! This sentence is not palidrom 🥲\nPlease, type another")
else:
    print("--")