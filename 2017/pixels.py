# file = open("przyklad.txt")
file = open("dane.txt")

temp = file.readlines()
pixels = []

for line in temp:
    line = list(map(int, line.strip().split()))
    pixels.append(line)

file.close()

# 6.1 find brightest and darkest pixel

minPixel = pixels[0][0]
maxPixel = pixels[0][0]

minList = []
maxList = []

for line in pixels:
    minPixel = int(min(line))
    maxPixel = int(max(line))
    minList.append(minPixel)
    maxList.append(maxPixel)

print("6.1\ndarkest: {} brightest: {}".format(min(minList), max(maxList)))

# 6.2 how many rows should be deleted for the picture to be symmetrical

counter = 0

for line in pixels:
    for i in range(0, len(line)//2):
        if line[i] != line[319 - i]:
            counter += 1
            break

print("6.2\nfor removal: {}".format(counter))

# 6.3 find contrasting neighbouring pixels in rows/columns

neighbourCounter = 0

for row in range(len(pixels)):
    for column in range(len(pixels[0])):
        neighbour = 0
        if column != 0 and abs(pixels[row][column - 1] - pixels[row][column]) > 128:
            neighbour = 1
        if column < len(pixels[0]) - 1 and abs(pixels[row][column + 1] - pixels[row][column]) > 128:
            neighbour = 1
        if row != 0 and abs(pixels[row - 1][column] - pixels[row][column]) > 128:
            neighbour = 1
        if row < len(pixels) - 1 and abs(pixels[row + 1][column] - pixels[row][column]) > 128:
            neighbour = 1
        neighbourCounter += neighbour

print("6.3\nneighbouring pixels: {}".format(neighbourCounter))

# 6.4 longest column of same colour pixels

smolLineList = []

for row in range(len(pixels) - 2):
    for column in range(len(pixels[0])):
        currentRow = row
        smolLine = 1
        while pixels[currentRow][column] == pixels[currentRow + 1][column]:
            smolLine += 1
            currentRow += 1
        if smolLine > 1:
            smolLineList.append(smolLine)

print("6.4\nlongest line: {}".format(max(smolLineList)))
