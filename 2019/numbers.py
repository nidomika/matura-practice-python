from math import factorial, gcd

file = open("przyklad.txt")
# file = open("liczby.txt")
temp = file.read().split()
file.close()

numbers = []

for number in temp:
    numbers.append(int(number))

# 4.1 count every power of 3

powerList = []
power = 1
i = 0

while 3 ** i < 100000:
    powerList.append(3 ** i)
    i += 1

counter1 = 0

for number in numbers:
    for powerElement in powerList:
        if number == powerElement:
            counter1 += 1

print("4.1\nnumber of powers of 3 in file: {}".format(counter1))

# 4.2 the number is equal to sum of factorial of its numbers

counter2 = 0

for number in temp:
    sumFactorial = 0
    for digit in number:
        sumFactorial += factorial(int(digit))
    if sumFactorial == int(number):
        counter2 += 1

print("4.2\nnumber of numbers equal to their sum of factorials: {}".format(counter2))

# 4.3 longest subsequence with equal NWD (GCD)

# counter3 = 0
# firstGCD = 0
# secondGCD = 0
#
# for i in range(len(numbers) - 2):
#     firstGCD = gcd(numbers[i], numbers[i + 1])
#     secondGCD = gcd(numbers[i + 1], numbers[i + 2])
#     if firstGCD == secondGCD:
#         counter3 += 1
#     else:
#         counter3 = 0
#
# print(counter3)

# no, not working
# yet
