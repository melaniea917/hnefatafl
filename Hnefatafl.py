empty = '#'
defender = "D"
king = "K"
attacker = "A"
escape = "E"
A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
H = 7
I = 8
J = 9
K = 10
rows = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
        [escape, empty, empty, attacker, attacker, attacker, attacker, attacker, empty, empty, escape],
        [empty, empty, empty, empty, empty, attacker, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
        [attacker, empty, empty, empty, empty, defender, empty, empty, empty, empty, attacker],
        [attacker, empty, empty, empty, defender, defender, defender, empty, empty, empty, attacker],
        [attacker, attacker, empty, defender, defender, king, defender, defender, empty, attacker, attacker],
        [attacker, empty, empty, empty, defender, defender, defender, empty, empty, empty, attacker],
        [attacker, empty, empty, empty, empty, defender, empty, empty, empty, empty, attacker],
        [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, empty, attacker, empty, empty, empty, empty, empty],
        [escape, empty, empty, attacker, attacker, attacker, attacker, attacker, empty, empty, escape]]


def print_board():
    row_number = 0
    for row in rows:
        print(str(row_number) + " " + str(row))
        row_number += 1


won = False
turn = "defender"
while not won:
    print_board()
    row = ''
    column = ''
    if turn == "defender":
        print("defender's turn")
        valid_move = False
        while not valid_move:
            is_piece = False
            while not is_piece:
                row = input("Enter row of piece to move: ")
                if int(row) < 1 or int(row) > 11:
                    valid = False
                else:
                    valid = True
                while not valid:
                    if int(row) < 1 or int(row) > 11:
                        row = input("Invalid row. Please enter the row of the piece to move: ")
                    else:
                        valid = True

                column = input("Enter column of piece to move: ")
                if column < 'A' or column > 'K':
                    valid = False
                else:
                    valid = True
                while not valid:
                    if column < 'A' or column > 'K':
                        column = input("Invalid column. Please enter the column of the piece to move: ")
                    else:
                        valid = True

                if column == 'A':
                    column = A
                elif column == 'B':
                    column = B
                elif column == 'C':
                    column = C
                elif column == 'D':
                    column = D
                elif column == 'E':
                    column = E
                elif column == 'F':
                    column = F
                elif column == 'G':
                    column = G
                elif column == 'H':
                    column = H
                elif column == 'I':
                    column = I
                elif column == 'J':
                    column = J
                elif column == 'K':
                    column = K

                if rows[int(row)][column] == empty:
                    print("No piece is in selected location. Please try again.")
                elif rows[int(row)][column] == escape:
                    print("Cannot select escape location. Please try again.")
                elif rows[int(row)][column] == attacker:
                    print("Defender cannot select attacker pieces. Please try again.")
                else:
                    is_piece = True

            move_row = input("Enter row where piece is to move: ")
            if int(move_row) < 1 or int(move_row) > 11:
                valid = False
            else:
                valid = True
            while not valid:
                if int(move_row) < 1 or int(move_row) > 11:
                    move_row = input("Invalid row. Please enter the row where piece is to move: ")
                else:
                    valid = True

            move_column = input("Enter column where piece is to move: ")
            if move_column < 'A' or move_column > 'K':
                valid = False
            else:
                valid = True
            while not valid:
                if move_column < 'A' or move_column > 'K':
                    move_column = input("Invalid column. Please enter the column where piece is to move: ")
                else:
                    valid = True

            if move_column == 'A':
                move_column = A
            elif move_column == 'B':
                move_column = B
            elif move_column == 'C':
                move_column = C
            elif move_column == 'D':
                move_column = D
            elif move_column == 'E':
                move_column = E
            elif move_column == 'F':
                move_column = F
            elif move_column == 'G':
                move_column = G
            elif move_column == 'H':
                move_column = H
            elif move_column == 'I':
                move_column = I
            elif move_column == 'J':
                move_column = J
            elif move_column == 'K':
                move_column = K

            if not row == move_row and not column == move_column:
                print("Pieces can only move in a straight line vertically or horizontally. Please try again.")
            elif row == move_row and column == move_column:
                print("Piece was sent to the same spot, movement cancelled. Please try again.")
            else:
                index = 0
                piece = rows[int(row)][column]
                set_piece = True
                if row == move_row:
                    if column > move_column:
                        index = column - 1
                        while index >= move_column:
                            if not rows[int(row)][index] == empty and not (piece == king and rows[int(row)][index] == escape):
                                print("The selected piece does not have a clear path to the destination. Pieces may not"
                                      " move through other pieces, and only the King can enter the corner escape "
                                      "locations. Please try again.")
                                set_piece = False
                                break
                            index -= 1
                    else:
                        index = column + 1
                        while index <= move_column:
                            if not rows[int(row)][index] == empty and not (piece == king and rows[int(row)][index] == escape):
                                print("The selected piece does not have a clear path to the destination. Pieces may not"
                                      " move through other pieces, and only the King can enter the corner escape "
                                      "locations. Please try again.")
                                set_piece = False
                                break
                            index += 1
                else:
                    if row > move_row:
                        index = int(row) - 1
                        while index >= int(move_row):
                            if not rows[index][column] == empty and not (piece == king and rows[index][column] == escape):
                                print("The selected piece does not have a clear path to the destination. Pieces may not"
                                      " move through other pieces, and only the King can enter the corner escape "
                                      "locations. Please try again.")
                                set_piece = False
                                break
                            index -= 1
                    else:
                        index = int(row) + 1
                        while index <= int(move_row):
                            if not rows[index][column] == empty and not (piece == king and rows[index][column] == escape):
                                print("The selected piece does not have a clear path to the destination. Pieces may not"
                                      " move through other pieces, and only the King can enter the corner escape "
                                      "locations. Please try again.")
                                set_piece = False
                                break
                            index += 1

                if set_piece:
                    rows[int(row)][column] = empty
                    rows[int(move_row)][move_column] = piece
                    valid_move = True
            row = int(move_row)
            column = move_column
    else:
        print("attacker's turn")
        valid_move = False
        while not valid_move:
            is_piece = False
            while not is_piece:
                row = input("Enter row of piece to move: ")
                if int(row) < 1 or int(row) > 11:
                    valid = False
                else:
                    valid = True
                while not valid:
                    if int(row) < 1 or int(row) > 11:
                        row = input("Invalid row. Please enter the row of the piece to move: ")
                    else:
                        valid = True

                column = input("Enter column of piece to move: ")
                if column < 'A' or column > 'K':
                    valid = False
                else:
                    valid = True
                while not valid:
                    if column < 'A' or column > 'K':
                        column = input("Invalid column. Please enter the column of the piece to move: ")
                    else:
                        valid = True

                if column == 'A':
                    column = A
                elif column == 'B':
                    column = B
                elif column == 'C':
                    column = C
                elif column == 'D':
                    column = D
                elif column == 'E':
                    column = E
                elif column == 'F':
                    column = F
                elif column == 'G':
                    column = G
                elif column == 'H':
                    column = H
                elif column == 'I':
                    column = I
                elif column == 'J':
                    column = J
                elif column == 'K':
                    column = K

                if rows[int(row)][column] == empty:
                    print("No piece is in selected location. Please try again.")
                elif rows[int(row)][column] == escape:
                    print("Cannot select escape location. Please try again.")
                elif rows[int(row)][column] == defender or rows[int(row)][column] == king:
                    print("Attacker cannot select defender pieces. Please try again.")
                else:
                    is_piece = True

            move_row = input("Enter row where piece is to move: ")
            if int(move_row) < 1 or int(move_row) > 11:
                valid = False
            else:
                valid = True
            while not valid:
                if int(move_row) < 1 or int(move_row) > 11:
                    move_row = input("Invalid row. Please enter the row where piece is to move: ")
                else:
                    valid = True

            move_column = input("Enter column where piece is to move: ")
            if move_column < 'A' or move_column > 'K':
                valid = False
            else:
                valid = True
            while not valid:
                if move_column < 'A' or move_column > 'K':
                    move_column = input("Invalid column. Please enter the column where piece is to move: ")
                else:
                    valid = True

            if move_column == 'A':
                move_column = A
            elif move_column == 'B':
                move_column = B
            elif move_column == 'C':
                move_column = C
            elif move_column == 'D':
                move_column = D
            elif move_column == 'E':
                move_column = E
            elif move_column == 'F':
                move_column = F
            elif move_column == 'G':
                move_column = G
            elif move_column == 'H':
                move_column = H
            elif move_column == 'I':
                move_column = I
            elif move_column == 'J':
                move_column = J
            elif move_column == 'K':
                move_column = K

            if not row == move_row and not column == move_column:
                print("Pieces can only move in a straight line vertically or horizontally. Please try again.")
            elif row == move_row and column == move_column:
                print("Piece was sent to the same spot, movement cancelled. Please try again.")
            else:
                index = 0
                set_piece = True
                if row == move_row:
                    if column > move_column:
                        index = column - 1
                        while index >= move_column:
                            if not rows[int(row)][index] == empty:
                                print("The selected piece does not have a clear path to the destination. Pieces may not"
                                      " move through other pieces, and only the King can enter the corner escape "
                                      "locations. Please try again.")
                                set_piece = False
                                break
                            index -= 1
                    else:
                        index = column + 1
                        while index <= move_column:
                            if not rows[int(row)][index] == empty:
                                print("The selected piece does not have a clear path to the destination. Pieces may not"
                                      " move through other pieces, and only the King can enter the corner escape "
                                      "locations. Please try again.")
                                set_piece = False
                                break
                            index += 1
                else:
                    if row > move_row:
                        index = int(row) - 1
                        while index >= int(move_row):
                            if not rows[index][column] == empty:
                                print("The selected piece does not have a clear path to the destination. Pieces may not"
                                      " move through other pieces, and only the King can enter the corner escape "
                                      "locations. Please try again.")
                                set_piece = False
                                break
                            index -= 1
                    else:
                        index = int(row) + 1
                        while index <= int(move_row):
                            if not rows[index][column] == empty:
                                print("The selected piece does not have a clear path to the destination. Pieces may not"
                                      " move through other pieces, and only the King can enter the corner escape "
                                      "locations. Please try again.")
                                set_piece = False
                                break
                            index += 1

                if set_piece:
                    piece = rows[int(row)][column]
                    rows[int(row)][column] = empty
                    rows[int(move_row)][move_column] = piece
                    valid_move = True
            row = int(move_row)
            column = move_column

    # See if the King reached one of the corners and escaped
    if rows[1][0] == 'K':
        print_board()
        print("The King escaped!")
        won = True
    elif rows[1][10] == 'K':
        print_board()
        print("The King escaped!")
        won = True
    elif rows[11][0] == 'K':
        print_board()
        print("The King escaped!")
        won = True
    elif rows[11][10] == 'K':
        print_board()
        print("The King escaped!")
        won = True
    # See if the defender captured any pieces
    elif turn == "defender":
        # Nest the if statements to avoid out of index errors
        if row - 2 > 0:
            if (rows[row - 2][column] == 'D' or rows[row - 2][column] == 'K') and rows[row - 1][column] == 'A':
                rows[row - 1][column] = empty
                print("The defenders captured an attacker!")
        # Nest the if statements to avoid out of index errors
        if row + 2 < 12:
            if (rows[row + 2][column] == 'D' or rows[row + 2][column] == 'K') and rows[row + 1][column] == 'A':
                rows[row + 1][column] = empty
                print("The defenders captured an attacker!")
        # Nest the if statements to avoid out of index errors
        if column - 2 >= 0:
            if (rows[row][column - 2] == 'D' or rows[row][column - 2] == 'K') and rows[row][column - 1] == 'A':
                rows[row][column - 1] = empty
                print("The defenders captured an attacker!")
        # Nest the if statements to avoid out of index errors
        if column + 2 < 11:
            if (rows[row][column + 2] == 'D' or rows[row][column + 2] == 'K') and rows[row][column + 1] == 'A':
                rows[row][column + 1] = empty
                print("The defenders captured an attacker!")
    # See if the attacker captured any pieces
    else:
        # Nest the if statements to avoid out of index errors
        if row - 2 > 0:
            # See if a defender piece has been captured between two Attackers
            if rows[row - 2][column] == 'A' and rows[row - 1][column] == 'D':
                rows[row - 1][column] = empty
                print("The attackers captured an defender!")
            # See if the King has been captured between four Attackers
            if column + 1 <= K and column - 1 >= A:
                if rows[row - 2][column] == 'A' and rows[row - 1][column] == 'K' and rows[row - 1][column + 1] == 'A' and rows[row - 1][column - 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
            # See if the King has been captured between three Attackers and the right side
            elif column == K:
                if rows[row - 2][column] == 'A' and rows[row - 1][column] == 'K' and rows[row - 1][column - 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
            # See if the King has been captured between three Attackers and the left side
            elif column == A:
                if rows[row - 2][column] == 'A' and rows[row - 1][column] == 'K' and rows[row - 1][column + 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
        # Nest the if statements to avoid out of index errors
        if row - 1 == 1:
            # See if the King has been captured by three Attackers and the top of the board. Since King would have escaped
            # in a corner, there shouldn't be a need to check that the columns are within bounds when at the top of the board.
            if rows[row - 1][column] == 'K' and rows[row - 1][column + 1] == 'A' and rows[row - 1][column - 1] == 'A':
                print_board()
                won = True
                print("The attackers captured the King!")
        # Nest the if statements to avoid out of index errors
        if row + 2 < 12:
            # See if a defender piece has been captured between two Attackers
            if rows[row + 2][column] == 'A' and rows[row + 1][column] == 'D':
                rows[row + 1][column] = empty
                print("The attackers captured an defender!")
            # See if the King has been captured between four Attackers
            if column + 1 <= K and column - 1 >= A:
                if rows[row + 2][column] == 'A' and rows[row + 1][column] == 'K' and rows[row + 1][column + 1] == 'A' and rows[row + 1][column - 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
            # See if the King has been captured between three Attackers and the right side
            elif column == K:
                if rows[row + 2][column] == 'A' and rows[row + 1][column] == 'K' and rows[row + 1][column - 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
            # See if the King has been captured between three Attackers and the left side
            elif column == A:
                if rows[row + 2][column] == 'A' and rows[row + 1][column] == 'K' and rows[row + 1][column + 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
        # Nest the if statements to avoid out of index errors
        if row + 1 == 11:
            # See if the King has been captured by three Attackers and the bottom of the board. Since King would have escaped
            # in a corner, there shouldn't be a need to check that the columns are within bounds when at the bottom of the board.
            if rows[row + 1][column] == 'K' and rows[row + 1][column + 1] == 'A' and rows[row + 1][column - 1] == 'A':
                print_board()
                won = True
                print("The attackers captured the King!")
        # Nest the if statements to avoid out of index errors
        if column - 2 >= A:
            # See if a defender piece has been captured between two Attackers
            if rows[row][column - 2] == 'A' and rows[row][column - 1] == 'D':
                rows[row][column - 1] = empty
                print("The attackers captured an defender!")
            # See if the King has been captured between four Attackers
            if row + 1 <= 11 and row - 1 >= 1:
                if rows[row][column - 2] == 'A' and rows[row][column - 1] == 'K' and rows[row - 1][column - 1] == 'A' and rows[row + 1][column - 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
            # See if the King has been captured between three Attackers and the bottom side
            elif row == 11:
                if rows[row][column - 2] == 'A' and rows[row][column - 1] == 'K' and rows[row - 1][column - 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
            # See if the King has been captured between three Attackers and the top side
            elif row == 1:
                if rows[row][column - 2] == 'A' and rows[row][column - 1] == 'K' and rows[row + 1][column - 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
        # Nest the if statements to avoid out of index errors
        if column - 1 == A:
            # See if the King has been captured by three Attackers and the left side of the board. Since King would have escaped
            # in a corner, there shouldn't be a need to check that the rows are within bounds when on the left side of the board.
            if rows[row][column - 1] == 'K' and rows[row + 1][column - 1] == 'A' and rows[row - 1][column - 1] == 'A':
                print_board()
                won = True
                print("The attackers captured the King!")
        # Nest the if statements to avoid out of index errors
        if column + 2 < K:
            # See if a defender piece has been captured between two Attackers
            if rows[row][column + 2] == 'A' and rows[row][column + 1] == 'D':
                rows[row][column + 1] = empty
                print("The attackers captured an defender!")
            # See if the King has been captured between four Attackers
            if row + 1 <= 11 and row - 1 >= 1:
                if rows[row][column + 2] == 'A' and rows[row][column + 1] == 'K' and rows[row - 1][column + 1] == 'A' and rows[row + 1][column + 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
            # See if the King has been captured between three Attackers and the bottom side
            elif row == 11:
                if rows[row][column + 2] == 'A' and rows[row][column + 1] == 'K' and rows[row - 1][column + 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
            # See if the King has been captured between three Attackers and the top side
            elif row == 1:
                if rows[row][column + 2] == 'A' and rows[row][column + 1] == 'K' and rows[row + 1][column + 1] == 'A':
                    print_board()
                    won = True
                    print("The attackers captured the King!")
        # Nest the if statements to avoid out of index errors
        if column + 1 == K:
            # See if the King has been captured by three Attackers and the right side of the board. Since King would have escaped
            # in a corner, there shouldn't be a need to check that the rows are within bounds when on the right side of the board.
            if rows[row][column + 1] == 'K' and rows[row + 1][column + 1] == 'A' and rows[row - 1][column + 1] == 'A':
                print_board()
                won = True
                print("The attackers captured the King!")

    # Move to the next turn
    if turn == "defender":
        turn = "attacker"
    else:
        turn = "defender"
