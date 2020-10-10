num = int(input("Enter a three-digit number: "))
while num < 100 or num > 999:
    print("Oops, you have written a not suitable number")
    num = int(input("Enter a three-digit number (XXX) : "))
digit1 = num // 100
digit2 = (num % 100) // 10
digit3 = num % 10
if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
    print("Дві цифри збігаються")
else: 
    print("Немає однакових цифр")


