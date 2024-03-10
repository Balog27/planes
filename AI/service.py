from random import randint
import random
class AI:
    def generate_coordinates(self):
        """
        Function that generates random coordinates for the attack
        :return: the coordinates for the attack
        """

        while True:
            head_row = random.randint(2, 7)
            head_row =   (chr(ord("A") + head_row))
            head_col = random.randint(3, 8)
            head_col = str(head_col)
            if (head_col == "1" or head_col == "2" or head_col == "9" or head_col == "10") or  (head_row == "A" or head_row == "B" or head_row == "I" or head_row == "J"):
                continue
            else:
                break

        ok = True
        while ok == True:
            tail = random.randint(1, 4)
            if tail == 1:
                tail = "up"
            elif tail == 2:
                tail = "down"
            elif tail == 3:
                tail = "left"
            elif tail == 4:
                tail = "right"
            if tail == "up":
                if head_row == "A" or head_row == "B" or head_row == "C" or head_col == "1" or head_col == "2" or head_col == "9" or head_col == "10":
                    ok = True
                else:
                    ok = False
            elif tail == "down":
                if head_row == "H" or head_row == "I" or head_row == "J" or head_col == "1" or head_col == "2" or head_col == "9" or head_col == "10":
                    ok = True
                else:
                    ok = False
            elif tail == "left":
                if head_col == "1" or head_col == "2" or head_col == "3" or head_row == "A" or head_row == "B" or head_row == "I" or head_row == "J":
                    ok = True
                else:
                    ok = False
            elif tail == "right":
                if  head_col == "8" or head_col == "9" or head_col == "10" or head_row == "A" or head_row == "B" or head_row == "I" or head_row == "J":
                    ok = True
                else:

                    ok = False



        return head_row, int(head_col), tail

    def attack(self):
        """
        Function that generates random coordinates for the attack
        :return: the coordinates for the attack
        """
        while True:
            col = random.randint(1, 10)
            row = random.randint(0, 9)
            if col <3 or col >8:
                if row <2 or row > 7:
                    continue
                else:
                    break
            else:
                break

        row =   (chr(ord("A") + row))
        print("The AI attacked the position: ", row, col)
        return row, col

    def is_valid_move(self, row, col):
        if 0 <= row <= 9 and 1 <= col <= 10:
            if col <3 or col >8:
                if row <2 or row > 7:
                    return False
            return True
        return False

    def __init__(self):
        super().__init__(10)
        self._last_hit = [0,0]

    @property
    def last_hit(self):
        return AI._last_hit

    def get_last_hit(self):
        return AI._last_hit

    def smart_attack(self,last_hit):
        if last_hit!= [0,0]:
            hit_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
            # If last move was a hit, continue in the same direction
            for direction in hit_directions:
                next_x = last_hit[0] + direction[0]
                next_y = last_hit[1] + direction[1]
                if AI.is_valid_move(self,next_x, next_y):
                    next_x = (chr(ord("A") + next_x))
                    return next_x, next_y
            return self.attack()
        return self.attack()

    def targeted_positions(self):
        hit_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for direction in hit_directions:


            next_x = self.last_hit[0] + direction[0]
            next_y = self.last_hit[1] + direction[1]
            if self.is_valid_move(next_x, next_y) and (next_x, next_y) not in AI.targeted_positions:
                return next_x, next_y
        return None
    def make_move(self):
        last_hit = AI.get_last_hit(self)
        if last_hit != [0,0]:
            hit_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
            # If last move was a hit, continue in the same direction
            for direction in hit_directions:
                next_x = last_hit[0] + direction[0]
                next_y = last_hit[1] + direction[1]
                if self.is_valid_move(next_x, next_y) and (next_x, next_y) not in AI.targeted_positions:
                    next_x =  (chr(ord("A") + next_x))
                    print("miau")
                    return next_x, next_y
            return self.attack()
        # If no hit direction or no valid move in that direction, revert to random move
        return self.attack()

    def update_after_hit(self, hit_position):
        AI.last_hit = hit_position
        AI.targeted_positions.add(hit_position)


