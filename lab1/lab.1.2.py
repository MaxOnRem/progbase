numbers = []
for x in range(10):
    numbers.append(int(input("Enter number №%i: " %(x+1))))
maxNumb = numbers[0]
for y in range(10):
    if numbers[y] > maxNumb:
        maxNumb = numbers[y]
print("Максимальне число - ", maxNumb)