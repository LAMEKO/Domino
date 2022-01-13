import random


def stock_pieces_generate():
    result = []
    for i in range(0, 7):
        for j in range(i, 7):
            result.append([i, j])
    random.shuffle(result)
    return result


def distribute(stock_pieces_):
    player_pieces_ = []
    computer_pieces_ = []
    player_pieces_ = stock_pieces_[0:7]
    del stock_pieces_[0:7]
    computer_pieces_ = stock_pieces_[0:7]
    del stock_pieces_[0:7]
    return [player_pieces_, computer_pieces_]


def nostartingpieces(player_pieces_, computer_pieces_):
    for i in range(7):
        if player_pieces_[i][0] == player_pieces_[i][1]:
            return True
        if player_pieces_[i][0] == player_pieces_[i][1]:
            return True
    return False


def player_rules_right(player_pieces_, piece_number_):
    for i in player_pieces_[piece_number_]:
        if i in domino_snake[-1]:
            return True
    return False


def player_rules_left(player_pieces_, piece_number_):
    for i in player_pieces_[piece_number_]:
        if i in domino_snake[0]:
            return True
    return False


def computer_rules_right(computer_pieces_, piece_number_):
    for i in computer_pieces_[piece_number_]:
        if i in domino_snake[-1]:
            return True
    return False


def computer_rules_left(computer_pieces_, piece_number_):
    for i in computer_pieces_[piece_number_]:
        if i in domino_snake[0]:
            return True
    return False


domino_snake = []
stock_pieces = stock_pieces_generate()
player_pieces, computer_pieces = distribute(stock_pieces)
while not nostartingpieces(player_pieces, computer_pieces):
    stock_pieces = stock_pieces_generate()
    player_pieces, computer_pieces = distribute(stock_pieces)
equal_elems_player = []
equal_elems_computer = []
for i in range(7):
    if player_pieces[i][0] == player_pieces[i][1]:
        equal_elems_player.append(player_pieces[i])
    if computer_pieces[i][0] == computer_pieces[i][1]:
        equal_elems_computer.append(computer_pieces[i])
if len(equal_elems_computer) == 0:
    domino_snake.append(max(equal_elems_player))
    player_pieces.remove(max(equal_elems_player))
elif len(equal_elems_player) == 0:
    domino_snake.append(max(equal_elems_computer))
    computer_pieces.remove(max(equal_elems_computer))
elif max(equal_elems_computer) > max(equal_elems_player):
    domino_snake.append(max(equal_elems_computer))
    computer_pieces.remove(max(equal_elems_computer))
else:
    domino_snake.append(max(equal_elems_player))
    player_pieces.remove(max(equal_elems_player))
if len(player_pieces) > len(computer_pieces):
    status = "It's your turn to make a move. Enter your command."
    player = 'player'
else:
    status = "Computer is about to make a move. Press Enter to continue..."
    player = 'computer'
finish = False
while True:
    if len(player_pieces) == 0:
        finish = True
        status = "The game is over. You won!"
    elif len(computer_pieces) == 0:
        finish = True
        status = "The game is over. The computer won!"
    elif domino_snake[-1][-1] == domino_snake[0][0] and len(domino_snake) != 1:
        count = 0
        for x in [0, 1]:
            for y in [-2, -1]:
                if domino_snake[0][x] == domino_snake[-1][y]:
                    for i in domino_snake:
                        count += i.count(domino_snake[0][0])
        if count >= 8:
            status = "The game is over. It's a draw!"
            finish = True
    print("======================================================================")
    print(f"Stock size: {len(stock_pieces)}\n")
    print(f"Computer pieces: {len(computer_pieces)}\n")
    if len(domino_snake) <= 6:
        print(*domino_snake)
    else:
        print(*domino_snake[0:3], '...', *domino_snake[-3:])
    print("\nYour pieces:")
    for i in range(len(player_pieces)):  # printing player pieces
        print(f"{i + 1}:{player_pieces[i]}")
    print('\nStatus:', status)
    if finish == True:
        break
    if player == "player":  # player turn
        while True:
            try:
                piece_number = int(input())
                if piece_number > 0:
                    piece_number -= 1
                    if not player_rules_right(player_pieces_=player_pieces, piece_number_=piece_number):
                        print("Illegal move. Please try again.")
                        continue
                    domino_snake.append((player_pieces[piece_number]))
                    player_pieces.pop(piece_number)
                elif piece_number < 0:
                    piece_number *= -1
                    piece_number -= 1
                    if not player_rules_left(player_pieces_=player_pieces, piece_number_=piece_number):
                        print("Illegal move. Please try again.")
                        continue
                    domino_snake.insert(0, player_pieces[piece_number])
                    player_pieces.pop(piece_number)
                elif piece_number == 0:
                    try:
                        player_pieces.append(stock_pieces[0])
                        stock_pieces.pop(0)
                    except:
                        break
                break
            except:
                print("Invalid input. Please try again.")
                continue
        player = 'computer'
        status = "Computer is about to make a move. Press Enter to continue..."
        continue
    elif player == "computer":  # computer turn
        input()
        piece_number = random.randint(-len(computer_pieces), len(computer_pieces))
        while True:
            try:
                if piece_number > 0:
                    piece_number -= 1
                    if not computer_rules_right(computer_pieces_=computer_pieces, piece_number_=piece_number):
                        continue
                    domino_snake.append(computer_pieces[piece_number])
                    computer_pieces.pop(piece_number)
                elif piece_number < 0:
                    piece_number *= -1
                    piece_number -= 1
                    if not computer_rules_left(computer_pieces_=computer_pieces, piece_number_=piece_number):
                        continue
                    domino_snake.insert(0, computer_pieces[piece_number])
                    computer_pieces.pop(piece_number)
                elif piece_number == 0:
                    try:
                        computer_pieces.append(stock_pieces[0])
                        stock_pieces.pop(0)
                    except:
                        break
                break
            except:
                continue
        player = "player"
        status = "It's your turn to make a move. Enter your command."
        continue
