file = open("liczby.txt")
numbers = file.read().split()
file = file.close

# 1. more 0s than 1s

counterAll = 0

for number in numbers:
    counter0 = 0
    counter1 = 0

    for bite in number:
        if bite == '0':
            counter0 += 1
        else:
            counter1 += 1
    if counter0 > counter1:
        counterAll += 1

print("1.", counterAll)

# 2. %2 and %8

counter2 = 0
counter8 = 0

for number in numbers:
    if not (int(number, 2) % 2):
        counter2 += 1
        if not (int(number, 2) % 8):
            counter8 += 1

print("2. %2:", counter2, "%8:", counter8)

# 3. min and max + their line

print("3. min line:", numbers.index(min(numbers)) + 1, "max line:", numbers.index(max(numbers)) + 1)
