from random import randint
import random
class INPUT:
    def airplance_placement(self):
        """
        This function will ask the user for the placement of the airplane.

        """
        while True:
            while True:
                try:
                    head_row = input("Please enter the position for the head of the airplane - row (A-J): ")
                    head_row = head_row.upper()
                    head_row = head_row.strip()
                    if head_row not in "ABCDEFGHIJ":
                        raise ValueError("The row must be between A and J")

                except ValueError as ve:
                    print(ve)
                else:
                    break

            while True:
                try:
                    head_col = input("Please enter the position for the head of the airplane - column (1-10): ")
                    head_col = head_col.strip()
                    if int(head_col) < 1 or int(head_col) > 10:
                        raise ValueError("The column must be between 1 and 10")
                except ValueError as ve:
                    print(ve)
                else:
                    break
            try:
                if head_col == "1" or head_col == "2" or head_col == "9" or head_col == "10":
                    if head_row == "A" or head_row == "B" or head_row == "I" or head_row == "J":
                        raise ValueError("The plane is outside the board for any direction of the tail")
            except ValueError as ve:
                print(ve)
            else:
                break


        while True:
            try:
                tail = input("Please specify in which direction referring to the head you want to position the tail(up, down, right, left) : ")
                print("Take into account that the plane is 4 squares long and 5 squares wide")
                tail = tail.strip()
                tail = tail.lower()
                if tail not in "up down right left":
                    raise ValueError("Unknown direction")
                if tail == "up":
                    if head_row == "A" or head_row == "B" or head_row == "C" or head_col == "1" or head_col =="2" or head_col == "9" or head_col == "10":
                        raise ValueError("The plane is outside the board")
                if tail == "down":
                    if head_row == "H" or head_row == "I" or head_row == "J" or head_col == "1" or head_col =="2" or head_col == "9" or head_col == "10":
                        raise ValueError("The plane is outside the board")
                if tail == "left":
                    if head_col == "1" or head_col == "2" or head_col == "3" or head_row == "A" or head_row == "B"  or head_row == "I" or head_row == "J":
                        raise ValueError("The plane is outside the board")
                if tail == "right":
                    if  head_col == "8" or head_col == "9" or head_col == "10" or head_row == "A" or head_row == "B"  or head_row == "I" or head_row == "J":
                        raise ValueError("The plane is outside the board")
            except ValueError as ve:
                print(ve)
            else:
                break
        return head_row, int(head_col), tail

    def attack(self):
        """
        This function will ask the user for the position to attack.

        """
        while True:
            while True:
                try:
                    row = input("Please enter the position for the attack - row (A-J): ")
                    row = row.upper()
                    row = row.strip()
                    if row not in "ABCDEFGHIJ":
                        raise ValueError("The row must be between A and J")
                except ValueError as ve:
                    print(ve)
                else:
                    break

            while True:
                try:
                    col = input("Please enter the position for the attack - column (1-10): ")
                    col = col.strip()
                    if int(col) < 1 or int(col) > 10:
                        raise ValueError("The column must be between 1 and 10")
                except ValueError as ve:
                    print(ve)
                else:
                    break
            return row, int(col)

    def who_starts_the_game(self):
        """
        This function will determine if the user or the A.I. will start the game.
        The user and the A.I. both have a 50 % change of starting the game.

        """
        random_number = random.randint(1, 100)
        print("The A.I chose a number between 1 and 100")
        print("You have to guess if the number is odd or even, if you guess right you will start the game otherwise the A.I. will start the game")
        while True:
            try:
                guess = input("Please enter your guess (odd or even): ")
                guess = guess.strip()
                guess = guess.lower()
                if guess not in "odd even":
                    raise ValueError("Unknown guess")
            except ValueError as ve:
                print(ve)
            else:
                break

        if random_number % 2 == 0:
            if guess == "even":
                print("You guessed right, you will start the game")
                print()
                return True
            else:
                print("You guessed wrong, the A.I. will start the game")
                print()
                return False
        if random_number % 2 == 1:
            if guess == "odd":
                print("You guessed right, you will start the game")
                print()
                return True
            else:
                print("You guessed wrong, the A.I. will start the game")
                print()
                return False

