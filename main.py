# yil = int(input(" yil kiriting: "))
#
# asr = (yil - 1) // 100 + 1
# print(f"{yil} - {asr}-asrga tegishli")


massiv = [4, 4, 4, 4, 5, 4, 4]

b = 4

for x in massiv:
    if x == b:
        print("umumiy sonlar", 4)
    else:
        print(f"bu yerda {x} ajralib turibdi ")
        break





import random

number = random.randint(1, 100)
print("Men 1 dan 100 gacha son o'yladim. Topa olasizmi?")
while True:
    guess = int(input("Sizning taxminingiz: "))
    if guess < number:
        print("Xato. Men o'ylagan son bundan katta.")
    elif guess > number:
        print("Xato. Men o'ylagan son bundan kichik.")
    else:
        print(f"Tabriklayman! Men {number} sonini o'ylagan edim.")
        break
