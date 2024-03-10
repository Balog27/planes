
from AI.service import AI


#todo USE the aircraft class and the aircraft repository class
class Board_ai:
    def __init__(self):
            pass

    def draw_a_plane_on_board(self,aircraft1,aircraft2,aircraft3,draw1,draw2,draw3,miss):
        print("AI board's:")
        print()
        for i in range(1, 11):
            if i == 1:
                print("  ", end=" ")
            print(i, end=" ")
        print()

        letter = "A"
        board_size = 10
        for i in range(board_size):
            for j in range(board_size):
                if j == 0:
                    print("  ", end="")
                print("+-", end="")
            print("+")

            for j in range(1,board_size + 2):
                if j == 1:
                    print(letter, end=" ")

                position = str(letter + str(j))

                if position in aircraft1:
                    k = aircraft1.index(position)
                    if draw1[k] == "X" or draw1[k] == "H":
                        print("|"+draw1[k], end="")
                    else:
                        print("| ", end="")
                elif position in aircraft2:
                    k = aircraft2.index(position)

                    if draw2[k] == "X" or draw2[k] == "H":
                        print("|"+draw2[k], end="")
                    else:
                        print("| ", end="")
                elif position in aircraft3:
                    k = aircraft3.index(position)
                    if draw3[k] == "X" or draw3[k] == "H":
                        print("|"+draw3[k], end="")
                    else:
                        print("| ", end="")
                elif position in miss:
                    print("|M", end="")

                else:
                    print("| ", end="")
            letter = chr(ord(letter) + 1)

            print()

        # Print the last row of horizontal lines
        for j in range(board_size):
            if j == 0:
                print("  ", end="")
            print("+-", end="")
        print("+")

        print()
        print()
    def draw_a_plane_on_board2(self,aircraft1,aircraft2,aircraft3,draw1,draw2,draw3,miss):

        for i in range(1, 11):
            if i == 1:
                print("  ", end=" ")
            print(i, end=" ")
        print()

        letter = "A"
        board_size = 10
        for i in range(board_size):
            for j in range(board_size):
                if j == 0:
                    print("  ", end="")
                print("+-", end="")
            print("+")

            for j in range(1,board_size + 2):
                if j == 1:
                    print(letter, end=" ")

                position = str(letter + str(j))

                if position in aircraft1:
                    k = aircraft1.index(position)
                    print("|"+draw1[k], end="")
                elif position in aircraft2:
                    k = aircraft2.index(position)
                    if position == aircraft2[k]:
                        print("|"+draw2[k], end="")
                elif position in aircraft3:
                    k = aircraft3.index(position)
                    print("|"+draw3[k], end="")
                elif position in miss:
                    print("|M", end="")

                else:
                    print("| ", end="")
            letter = chr(ord(letter) + 1)

            print()

        # Print the last row of horizontal lines
        for j in range(board_size):
            if j == 0:
                print("  ", end="")
            print("+-", end="")
        print("+")

        print()
        print()



    def create_map(self,aircraft1,draw):

        head_row, head_col, tail =AI.generate_coordinates(self)

        head = head_row + str(head_col)
        aircraft1.append(head)
        if tail == "up":
            draw = ["v", "0", "0", "T", "0", "0", "<",">","<" , ">"]
            for i in range(1, 4):
                aircraft1.append(chr(ord(head_row) - i) + str(head_col))
            for i in range(1, 3):
                aircraft1.append(chr(ord(head_row) - 1) + str(head_col - i))
                aircraft1.append(chr(ord(head_row) - 1) + str(head_col + i))
            aircraft1.append(chr(ord(head_row) - 3) + str(head_col - 1))
            aircraft1.append(chr(ord(head_row) - 3) + str(head_col + 1))
        elif tail == "down":
            draw = ["^", "0", "0", "T", "0", "0", "<", ">", "<", ">"]
            for i in range(1, 4):
                aircraft1.append(chr(ord(head_row) + i) + str(head_col))
            for i in range(1, 3):
                aircraft1.append(chr(ord(head_row) + 1) + str(head_col - i))
                aircraft1.append(chr(ord(head_row) + 1) + str(head_col + i))
            aircraft1.append(chr(ord(head_row) + 3) + str(head_col - 1))
            aircraft1.append(chr(ord(head_row) + 3) + str(head_col + 1))
        elif tail == "left":
            draw = [">", "0", "0", "T", "0", "0", "^", "v", "^", "v"]
            for i in range(1, 4):
                aircraft1.append(head_row + str(head_col - i))
            for i in range(1, 3):
                aircraft1.append(chr(ord(head_row) - i) + str(head_col - 1))
                aircraft1.append(chr(ord(head_row) + i) + str(head_col - 1))
            aircraft1.append(chr(ord(head_row) - 1) + str(head_col - 3))
            aircraft1.append(chr(ord(head_row) + 1) + str(head_col - 3))
        elif tail == "right":
            draw = ["<", "0", "0", "T", "0", "0", "^", "v", "^", "v"]
            for i in range(1, 4):
                aircraft1.append(head_row + str(head_col + i))
            for i in range(1, 3):
                aircraft1.append(chr(ord(head_row) - i) + str(head_col + 1))
                aircraft1.append(chr(ord(head_row) + i) + str(head_col + 1))
            aircraft1.append(chr(ord(head_row) - 1) + str(head_col + 3))
            aircraft1.append(chr(ord(head_row) + 1) + str(head_col + 3))

        return aircraft1,head_row,head_col,tail,draw
    def map_of_the_board(self):
        """
        This function will create a map of the board
        :return:
        """
        cont = 1
        aircraft1 = []
        aircraft2 = []
        aircraft3 = []
        draw1 = []
        draw2 = []
        draw3 = []
        while cont<=3:

            if cont == 1:

                aircraft1, head_row,head_col, tail,draw1 = self.create_map(aircraft1,draw1)

                #Board_ai.draw_a_plane_on_board2(self,aircraft1,aircraft2,aircraft3,draw1,draw2, draw3,[])
                cont += 1
            elif cont == 2:
                while True:
                    try:
                        aircraft2, head_row, head_col, tail,draw2 = self.create_map(aircraft2,draw2)
                        for i in range(len(aircraft2)):
                            if aircraft2[i] in aircraft1:
                                aircraft2.clear()
                                raise ValueError("The plane overlaps with another plane")
                    except ValueError as ve:
                        pass
                    else:
                        break
                #Board_ai.draw_a_plane_on_board2(self,aircraft1,aircraft2,aircraft3,draw1,draw2, draw3,[])
                cont += 1
            elif cont == 3:
                while True:
                    try:
                        aircraft3, head_row, head_col, tail,draw3 = self.create_map(aircraft3,draw3)
                        for i in range(len(aircraft3)):
                            if aircraft3[i] in aircraft1 or aircraft3[i] in aircraft2:
                                aircraft3.clear()
                                raise ValueError("The plane overlaps with another plane")
                    except ValueError as ve:
                        pass
                    else:
                        break
                #Board_ai.draw_a_plane_on_board2(self,aircraft1,aircraft2,aircraft3,draw1,draw2,draw3,[])
                cont += 1
        return aircraft1,aircraft2,aircraft3,draw1,draw2,draw3

    def ai_move(self,aircraft1,aircraft2,aircraft3,draw1,draw2,draw3,miss,last_hit):


        row,col = AI.attack(self)



        place = row + str(col)

        if place in aircraft1:
            index = aircraft1.index(place)
            if place == aircraft1[0] and draw1[0] != "X":
                print("AI destroyed a plane!")

                draw1[0] = "X"
                last_hit = [0,0]

            elif place == aircraft1[0] and draw1[0] == "X":
                print("AI already destroyed this plane!")
            elif place != aircraft1[0] and draw1[index] != "H":

                draw1[index] = "H"
                last_hit[0] = ord(place[0]) - ord("A")
                last_hit[1] = int(place[1])
                print("AI hit a plane!")
            elif place != aircraft1[0] and draw1[index] == "H":
                print("AI already hit this plane in the same place!")
        elif place in aircraft2:
            index = aircraft2.index(place)
            if place == aircraft2[0] and draw2[0] != "X":
                print("AI destroyed a plane!")
                draw2[0] = "X"
                last_hit = [0,0]

            elif place == aircraft2[0] and draw2[0] == "X":
                print("AI already destroyed this plane!")
            elif place != aircraft2[0] and draw2[index] != "H":
                draw2[index] = "H"
                last_hit[0] = ord(place[0])-ord("A")
                last_hit[1] = int(place[1])
                print("AI hit a plane!")
            elif place != aircraft2[0] and draw2[index] == "H":
                print("AI already hit this plane in the same place!")
        elif place in aircraft3:
            index = aircraft3.index(place)
            if place == aircraft3[0] and draw3[0] != "X":
                print("AI destroyed a plane!")
                draw3[0] = "X"
                last_hit = [0,0]
            elif place == aircraft3[0] and draw3[0] == "X":
                print("AI already destroyed this plane!")
            elif place != aircraft3[0] and draw3[index] != "H":
                draw3[index] = "H"
                last_hit[0] = ord(place[0])-ord("A")
                last_hit[1] = int(place[1])
                print("AI hit a plane!")
            elif place != aircraft3[0] and draw3[index] == "H":
                print("AI already hit this plane in the same place!")

        else:
            print("AI missed!")
            miss.append(place)

        if draw3[0] == "X" and draw2[0] == "X" and draw1[0] == "X":
            return draw1,draw2,draw3,miss,1

        return draw1,draw2,draw3,miss,0





#TODO make the ai board invisile for the player(only the player board will be visible)
#
#
# board = Board_ai()
#
# board.map_of_the_board()
