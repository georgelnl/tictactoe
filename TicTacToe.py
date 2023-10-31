import random
import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


class InvalidMoveException(Exception):
    """Exception raised when user makes a move that is no longer available"""

    def __init__(self, position):
        self.position = position
        super().__init__(f'Invalid move, position {position} is not available')


class Game:

    def __init__(self):
        """Initiliazises a new game"""
        self.available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.board = {1: ' ',
                      2: ' ',
                      3: ' ',
                      4: ' ',
                      5: ' ',
                      6: ' ',
                      7: ' ',
                      8: ' ',
                      9: ' '}
        self.row = '\n' + '-' * 9
        self.col = ' | '
        print('Player is [0] and computer is [X]')
        logging.info('Game initialised')

    def display_board(self, row, col, board):
        """Prints out the board"""
        print(self.board[1] + self.col + self.board[2] + self.col + self.board[3] + self.row + '\n' + self.board[4]
              + self.col + self.board[5] + self.col + self.board[6] + self.row + '\n' + self.board[7] + self.col
              + self.board[8] + self.col + self.board[9] + self.row)


def check_win(player, board):
    """
        Checks if the player has won.

        player attributed should be 'O' for the user, and 'X' for the computer

    """
    win_conditions = [
        [1, 2, 3], [1, 4, 7], [1, 5, 9],
        [2, 5, 8], [3, 6, 9], [4, 5, 6],
        [7, 8, 9], [3, 5, 7]
    ]

    for condition in win_conditions:
        # Checks for user win
        if all(board[i] == player for i in condition) and player == 'O':
            game.display_board(row=game.row, col=game.col, board=game.board)
            print('*** Congratulations ! You won ! ***')
            logging.info("Game ended, user won.")
            return True
        # Checks for computer win
        elif all(board[i] == player for i in condition) and player == 'X':
            game.display_board(row=game.row, col=game.col, board=game.board)
            print('*** You lost ! ***')
            logging.info("Game ended, computer won.")
            return True

    return False  # if no player has won yet, returns False


def user_move():
    """This simulates a user move"""
    while True:
        try:
            print(f"Moves available: {', '.join(map(str, a))}")
            m = int(input('Make your move! [1-9] : '))
            if m not in a:
                logging.warning(f'Invalid user move, position {m} is not available')
                raise InvalidMoveException(m)
        except ValueError:
            print("You need to input a number")
            logging.warning("User input non-numerical value as a move")
        except InvalidMoveException as e:
            print(e)
        except Exception as e:
            print(e)
        else:
            a.remove(m)  # removes move from the available moves list
            game.board[m] = 'O'  # puts the users mark on the board
            if check_win(player='O', board=game.board):
                return True
            return False


def comp_move():
    """This simulates a computer move"""
    if game_active(a):
        c = random.choice(a)
        a.remove(c)  # removes move from the available moves list
        game.board[c] = 'X'  # puts the computer's mark on the board
        print('The computer chose', c)
        if check_win(player='X', board=game.board):
            return True
        return False
    else:
        return True  # ends the game if no moves available for computer to play


def game_active(a):
    """Checks if there are still available moves to be played. If not, it means the game has ended."""
    if len(a) > 0:
        return True
    else:
        return False


game = Game()
a = game.available

while game_active(a):  # Game runs as long as there are available moves to make
    game.display_board(row=game.row, col=game.col, board=game.board)  # Display board at start of each turn
    if user_move():
        break
    if comp_move():
        break
    else:
        logging.info("Turn ended, both players have played.")
else:  # if at end of turn, user hasn't won, computer hasn't won, and no available moves are left, then it is a tie.
    game.display_board(row=game.row, col=game.col, board=game.board)
    print("It's a tie!")
    logging.info("Game ended in a tie.")
