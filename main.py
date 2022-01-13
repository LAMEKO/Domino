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
    draw = 0
    for i in range(1, 7):
        if domino_snake[0][0] == domino_snake[-1][-1] and len([y for x in domino_snake for y in x if y == i]) >= 8:
            draw = 1
    if draw == 1:
        status = ("The game is over. It's a draw!")
        finish = True
    if len(player_pieces) == 0:
        finish = True
        status = "The game is over. You won!"
    elif len(computer_pieces) == 0:
        finish = True
        status = "The game is over. The computer won!"
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
    if finish:
        break
    if player == "player":  # player turn
        player = 'computer'
        status = "Computer is about to make a move. Press Enter to continue..."
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
    elif player == "computer":  # computer turn
        while True:
            player = "player"
            status = "It's your turn to make a move. Enter your command."
            input()
            digit_score = dict()
            for pieces in computer_pieces:
                for j in pieces:
                    for domino_pieces in domino_snake:
                        if str(pieces) in digit_score:
                            digit_score[j] += domino_pieces.count(j)
                        else:
                            digit_score[j] = domino_pieces.count(j)
            # for key in ai_score:
            #     print(key, "=", ai_score[key])
            computer_pieces_score = []
            for pieces in computer_pieces:
                tmp = 0
                for j in pieces:
                    tmp += int(digit_score[j])
                computer_pieces_score.append([pieces, tmp])
            available_computer_pieces = []
            for pieces in computer_pieces_score:
                for x in [0, 1]:
                    if (pieces[0][x] in domino_snake[0] or pieces[0][x] in domino_snake[-1]) and pieces not in available_computer_pieces:
                        available_computer_pieces.append(pieces)
            if len(available_computer_pieces) == 0:
                try:
                    computer_pieces.append(stock_pieces[0])
                    stock_pieces.pop(0)
                    break
                except:
                    break
            max_ = available_computer_pieces[0][1]
            elem = available_computer_pieces[0][0]
            for pieces in available_computer_pieces:
                # print(pieces)
                if max_ < pieces[1]:
                    max_ = pieces[1]
                    elem = pieces[0]
            piece_number = computer_pieces.index(elem)
            if computer_rules_right(computer_pieces_=computer_pieces, piece_number_=piece_number):
                domino_snake.append(computer_pieces[piece_number])
                computer_pieces.pop(piece_number)
                break
            elif computer_rules_left(computer_pieces_=computer_pieces, piece_number_=piece_number):
                domino_snake.insert(0, computer_pieces[piece_number])
                computer_pieces.pop(piece_number)
                break
            else:
                try:
                    computer_pieces.append(stock_pieces[0])
                    stock_pieces.pop(0)
                    break
                except:
                    break
