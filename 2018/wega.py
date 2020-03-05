file = open("przyklad.txt")
# file = open("sygnaly.txt")
signals = file.read().split()
file.close()

# 4.1 every 10th letter in every 40th word concatenated a creates new word

newWord = ''

for word in range(39, len(signals), 40):
    newWord += signals[word][9]

print("4.1\nprzeslanie: {}".format(newWord))

# 4.2 find word with the most unique letters

wordList = []
wordCountList = []

for word in signals:
    letterCount = {}
    for letter in word:
        letterCount[letter] = letterCount.get(letter, 0) + 1
    counter = ''
    newList = letterCount.keys()
    smolLetterCount = len(newList)
    for key in newList:
        counter += key
    wordList.append(counter)
    wordCountList.append(smolLetterCount)

# xddddddddddddddddddddddddd
print("6.2\nmost unique letters: {} {}".format(wordList[wordCountList.index(max(wordCountList))], max(wordCountList)))
# xddddddddddddddddddddddddd

# 4.3 difference between every letter is <= 10
# so basically biggest ascii - smallest ascii <= 10

for word in signals:
    maximum = word[0]
    minimum = word[0]
    for letter in word:
        if ord(letter) > ord(maximum):
            maximum = letter
        if ord(letter) < ord(minimum):
            minimum = letter
    if ord(maximum) - ord(minimum) <= 10:
        print(word)