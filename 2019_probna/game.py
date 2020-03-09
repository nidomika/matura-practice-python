file1 = open("plansza.txt")
file2 = open("robot.txt")
temp = file1.readlines()
players = file2.read().split()
board = []

for item in temp:
    board.append(item.strip().split())

file1.close()
file2.close()

# 4.1 how many disqualified

disqualified = 0

for player in players:
    positionX = 1
    positionY = 1
    for move in player:
        if move == 'N':
            positionX -= 1
        elif move == 'E':
            positionY += 1
        elif move == 'S':
            positionX += 1
        elif move == 'W':
            positionY -= 1
        if positionX < 1 or positionY < 1 or positionX > len(board) or positionY > len(board):
            disqualified += 1
            break
print("4.1\ndisqualified: {}".format(disqualified))

# 4.2 index of player with best score

scoreBoard = []

for player in players:
    points = int(board[0][0])
    positionX = 0
    positionY = 0
    for move in player:
        if move == 'N':
            positionX -= 1
        elif move == 'E':
            positionY += 1
        elif move == 'S':
            positionX += 1
        elif move == 'W':
            positionY -= 1
        points += int(board[positionX][positionY])
        if positionX < 0 or positionY < 0 or positionX >= len(board) or positionY >= len(board):
            points = -1
            break
    scoreBoard.append(points)

print("4.2\nindex with highest score: {}\nscore: {}".format(scoreBoard.index(max(scoreBoard)) + 1, max(scoreBoard)))

# 4.3 highest amount of moves in the one row (W or E)

longestMove = 0

for player in players:
    counterMove = 0
    for move in player:
        if move == 'E' or move == 'W':
            counterMove += 1
        else:
            counterMove = 0
        if counterMove > longestMove:
            longestMove = counterMove

for player in players:
    counterMove = 0
    for move in player:
        if move == 'E' or move == 'W':
            counterMove += 1
        else:
            counterMove = 0
        if counterMove == longestMove:
            print("4.3\nindex with most in one row: {}\nscore: {}".format(players.index(player) + 1, longestMove))
