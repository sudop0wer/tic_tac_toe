import subprocess


class Game():

    def __init__(self, turn=2, win=0, board=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]):
        self.turn = turn
        self.win = win
        self.board = board

    def make_move(self, x, y):
        x = int(x)
        y = int(y)
        if self.turn == 1:
            self.board[x-1][y-1] = 1
            self.turn = 2

        elif self.turn == 2:
            self.board[x-1][y-1] = 2
            self.turn = 1

    def check_move(self, x, y):
        x = int(x)
        y = int(y)
        if x >= 0 and x <= 3 and y >= 0 and y <= 3:
            if self.board[x-1][y-1] == 0:
                return 1
            else:
                print("Wrong move!")
                return 0
        else:
            print("Please type correct coordinates!")
            return 0

    def display_board(self):
        for i in range(3):
            print("╭――-╮" * 3)
            for j in range(3):
                print(f"| {
                      "X" if self.board[i][j] == 2 else "O" if self.board[i][j] == 1 else " "} |", end='')
            print("")
            print("╰―-―╯" * 3)

    def check_win(self):
        for i in range(3):
            a = 0
            if self.board[i][a] == self.board[i][a+1] == self.board[i][a+2]:
                return self.board[i][a]
            elif self.board[a][i] == self.board[a+1][i] == self.board[a+2][i]:
                return self.board[a][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[1][1]
        else:
            return 0


game1 = Game()
subprocess.run("clear")

while game1.win == 0:

    print("""
▀▀█▀▀ ▀█▀ ░█▀▀█ 　 ▀▀█▀▀ ─█▀▀█ ░█▀▀█ 　 ▀▀█▀▀ ░█▀▀▀█ ░█▀▀▀
─░█── ░█─ ░█─── 　 ─░█── ░█▄▄█ ░█─── 　 ─░█── ░█──░█ ░█▀▀▀
─░█── ▄█▄ ░█▄▄█ 　 ─░█── ░█─░█ ░█▄▄█ 　 ─░█── ░█▄▄▄█ ░█▄▄▄""")
    print("\n Welcome to TicTacToe!")
    print("To specify the move you want to make, specify a value for row,column (like 1,3)")

    game1.display_board()

    if game1.check_win() == 1:
        print("Player O wins!")
        break
    elif game1.check_win() == 2:
        print("Player X wins!")
        break

    move = input(f"Player {"X" if game1.turn == 2 else "O"} move>> ")
    move_list = move.split(',')
    if game1.check_move(move_list[0], move_list[1]):
        game1.make_move(move_list[0], move_list[1])
    else:
        continue

    subprocess.run("clear")

    subprocess.run("clear")
