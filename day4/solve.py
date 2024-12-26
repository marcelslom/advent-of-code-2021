class Board:

    def __init__(self, board_lines):
        self.board = []
        for line in board_lines:
            self.board.append([int(x.strip()) for x in line.split()])
        self.status = []
        for row in self.board:
            self.status.append([False] * len(row))
        
    def win(self):
        for row in self.status:
            if all(row):
                return True

        for i in range(len(self.status[0])):
            b = True
            for row in self.status:
                b = b & row[i]
            if b:
                return True
        
        return False

    def mark_number(self, number):
        for y, row in enumerate(self.board):
            for x, element in enumerate(row):
                if element == number:
                    self.status[y][x] = True

    def score(self):
        sum = 0
        for y, row in enumerate(self.status):
            for x, element in enumerate(row):
                if not element:
                    sum += self.board[y][x]
        return sum

BOARD_SIZE = 5
boards = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    numbers = [int(x) for x in lines[0].split(',')]
    board_lines = []
    for i in range(2,len(lines)):
        line = lines[i].strip()
        if line:
            board_lines.append(line)
        if len(board_lines) == BOARD_SIZE:
            boards.append(Board(board_lines))
            board_lines = []

#1st part
for number in numbers:
    for board in boards:
        board.mark_number(number)
        if board.winner():
            print(number)
            print(board.score())
            print(number * board.score())
            break
    else:
        continue
    break

#2nd part
filtered = boards
for i, number in enumerate(numbers):
    for board in filtered:
        board.mark_number(number)
    
    if len(filtered) == 1:
        last = filtered[0]
        if last.winner():
            print(number)
            print(last.score())
            print(number * last.score())
            break
    else:
        filtered = list(filter(lambda x: not x.winner(), filtered))
