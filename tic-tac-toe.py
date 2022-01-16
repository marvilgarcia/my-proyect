'''base = []
row = []
for i in range (1,10):
    row.append(i)
    if i % 3 == 0:
        base.append(row)
        row = []
board = base[:]'''
import turtle

def draw_board():

    for i in range(2):
         
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)

    for i in range(2):

        drawer.penup()
        drawer.goto(-100 + 200 * i, 300 )
        drawer.pendown()
        drawer.fordward(600)

    num = 1
    for i in range(3):
        for j in range (3):
            drawer.penup()
            drawer.goto(-290 + j *200, 280 - i  * 200 )
            drawer.pendown()

            drawer.write(num, font = ("Arial", 12))
    num += 1

def addX(row, column):

    screen.update

drawer = turtle.Turtle()

drawer.pensize(10)
drawer.ht()

screen = turtle.Screen()
screen.tracer(0)

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()