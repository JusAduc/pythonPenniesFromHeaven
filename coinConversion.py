from math import remainder

amountOfHundreds=0
amountOfFiftys=0
amountOfTens=0
amountOfFives=0
amountOfOnes=0
amountOfQuarters=0
amountOfDimes=0
amountOfNickles=0
NewAmountOfPennies=0

raw_amountOfPennies = input("Inset your ammount of pennie here: ")
amountOfPennies = int(raw_amountOfPennies)
 
#100's
while amountOfPennies >= 10000:
    amountOfHundreds = amountOfHundreds + 1
    amountOfPennies = amountOfPennies - 10000
#50's
while amountOfPennies >= 5000:
    amountOfFiftys = amountOfFiftys + 1
    amountOfPennies = amountOfPennies - 5000
#10's
while amountOfPennies >= 1000:
    amountOfTens = amountOfTens + 1
    amountOfPennies = amountOfPennies - 1000
#5's
while amountOfPennies >= 500:
    amountOfFives = amountOfFives + 1
    amountOfPennies = amountOfPennies - 5000
#1's
while amountOfPennies >= 100:
    amountOfOnes = amountOfOnes + 1
    amountOfPennies = amountOfPennies - 100
#.25's
while amountOfPennies >= 25:
    amountOfQuarters = amountOfQuarters + 1
    amountOfPennies = amountOfPennies - 25
#.10's
while amountOfPennies >= 10:
    amountOfDimes = amountOfDimes + 1
    amountOfPennies = amountOfPennies - 10
#.05's
while amountOfPennies >= 5:
    amountOfNickles = amountOfNickles + 1
    amountOfPennies = amountOfPennies - 5

print("")
print(f"Amont Of Hundred Dollar Bills: {amountOfHundreds}")
print(f"Amont Of fifty Dollar Bills: {amountOfFiftys}")
print(f"Amont Of Ten Dollar Bills: {amountOfTens}")
print(f"Amont Of Five Dollar Bills: {amountOfFives}")
print(f"Amont Of One Dollar Bills: {amountOfOnes}")
print(f"Amont Of Quarters: {amountOfQuarters}")
print(f"Amont Of Dimes: {amountOfDimes}")
print(f"Amont Of Nickles: {amountOfNickles}")
print(f"Amont Of Pennies: {amountOfPennies}")