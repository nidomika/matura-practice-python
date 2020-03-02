file = open("dane_6_1.txt")
words1 = file.read().split()

file = open("dane_6_2.txt")
words2 = file.read().split()

file = open("dane_6_3.txt")
words3 = file.read().split()

file.close()


# 6.1 encode to cesars with one key = 107

def first():
    wordsCesar1 = []
    k = 107 % 26

    for word in words1:
        newWord = ''
        for letter in word:
            newLetter = ord(letter) + k
            while newLetter < 65 or newLetter > 90:
                if newLetter > 90:
                    newLetter -= 26
                elif newLetter < 65:
                    newLetter += 26
            newWord = newWord + chr(newLetter)
        wordsCesar1.append(newWord)
    return wordsCesar1


# 6.2 decode from cesars BUT every second item is the key
# (the matura exam team made a mistake in dane_6_2.txt and it was impossible to solve this problem)

def second():
    wordsCesar2 = []

    for i in range(0, len(words2), 2):
        newWord = ''
        k = int(words2[i + 1])
        for letter in words2[i]:
            newLetter = ord(letter) - k
            while newLetter < 65 or newLetter > 90:
                if newLetter > 90:
                    newLetter -= 26
                elif newLetter < 65:
                    newLetter += 26
            newWord = newWord + chr(newLetter)
        wordsCesar2.append(newWord)
    return wordsCesar2


# 6.3 every second word is the first but encoded with unknown key => print those that are incorrectly encoded

def third():
    wordsCesar3 = []

    for i in range(0, len(words3), 2):
        newWord = ''
        if ord(words3[i][0]) > ord(words3[i + 1][0]):
            k = 26 - (ord(words3[i][0]) - ord(words3[i + 1][0]))
        else:
            k = (ord(words3[i + 1][0]) - ord(words3[i][0]))
        for letter in words3[i]:
            newLetter = ord(letter) + k
            while newLetter < 65 or newLetter > 90:
                if newLetter > 90:
                    newLetter -= 26
                elif newLetter < 65:
                    newLetter += 26
            newWord = newWord + chr(newLetter)  # encoded
        if newWord != words3[i + 1]:
            wordsCesar3.append(words3[i])
    return wordsCesar3


print("\n6.1\n", first(), "\n6.2\n", second(), "\n6.3\n", third())
