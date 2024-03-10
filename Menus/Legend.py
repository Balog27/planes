class Game_informations:
    def legend(self):
        print("------------------------------------ LEGEND -------------------------------------------------------------------")
        print()
        print("    ^ - the head of the plane")
        print("    0 - the body of the plane")
        print("    T - the tail of the plane")
        print("    H - a plane was hit")
        print("    M - a plane was missed")
        print("    X - a plane was destroyed(hit the head)")
        print("    ' ' - empty space (it wasn't attacked)  ")
        print()
        print("------------------------------------ GAME ----------------------------------------------------------------------")
        print()
        print()
    def rules(self):
        print("------------------------------------ RULES ----------------------------------------------------------------------")
        print()

        print("Aircraft play on paper with squares where two identical grids are drawn, usually consisting of 10x10 boxes.")
        print("Each box is identified by a number on the X-axis (from 1 to 10) and a letter on the Y-axis (from A to J).")
        print("The first grid is private, where three identical aircraft are placed without the opponent seeing their position.")
        print("The aircraft are not allowed to go outside the grid.")
        print()
        print("When both players have drawn the three planes in their own grid, the game can begin."
              "The first move can be determined by drawing lots. Each move has two parts:")
        print("   - The opponent looks at their own grid and responds with one of the following possibilities:")
        print("   - Miss: the square is outside of any plane.")
        print("   - Hit: the square is part of a plane, but the cockpit has not been found.")
        print("   - Kill/Downed: the square contains the cockpit of a plane. All squares of the downed plane become hits.")

        print()
        print("!!!IMPORTNAT!!!")
        print("A player is not necessarily required to state in which direction the opponent's downed plane is. ")
        print( "Thus, the player is not obliged to say whether a hit square is part of an already downed plane.")
        print()

        print("Draw possibility: if the first player in turn has found all three planes,")
        print("then the second player has another chance to find the opponent's plane, as the first player had an extra move.")
        print()


