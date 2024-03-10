from Menus.Legend import Game_informations
from board.draw_board_ai import Board_ai
#in board ai it prints the random thing in the beginning and you need the try where you just deleted it
from board.draw_board_player import Board_player
from UI.input_check import INPUT

def main():

    ui = INPUT()
    player_board = Board_player()
    ai_board = Board_ai()
    game_info = Game_informations()
    game_info.rules()
    game_info.legend()

#todo display the 2 baords next to each other
    player_miss_map = []
    ai_miss_map = []
    last_hit = [0,0]
    player_board.draw_a_plane_graphic()
    player_aircraft1, player_aircraft2, player_aircraft3, player_draw1, player_draw2, player_draw3 = player_board.map_of_the_board()
    ai_aircraft1, ai_aircraft2, ai_aircraft3, ai_draw1, ai_draw2, ai_draw3 = ai_board.map_of_the_board()
    who_starts = ui.who_starts_the_game()
    miss_map = []
    player_win_check = 0
    ai_win_check = 0
    #ai_board.draw_a_plane_on_board2(ai_aircraft1, ai_aircraft2, ai_aircraft3, ai_draw1, ai_draw2, ai_draw3, ai_miss_map)
    while True:

        if who_starts == False:
            player_draw1,player_draw2,player_draw3,player_miss_map,ai_win_check =ai_board.ai_move(player_aircraft1,player_aircraft2,player_aircraft3,player_draw1,player_draw2,player_draw3,player_miss_map,last_hit)
            player_board.draw_a_plane_on_board2(player_aircraft1,player_aircraft2,player_aircraft3,player_draw1,player_draw2,player_draw3,player_miss_map)
            #ai_board.map_of_the_board()

            ai_draw1,ai_draw2,ai_draw3,ai_miss_map,player_win_check = player_board.player_move(ai_aircraft1,ai_aircraft2,ai_aircraft3,ai_draw1,ai_draw2,ai_draw3,ai_miss_map)
            ai_board.draw_a_plane_on_board(ai_aircraft1, ai_aircraft2, ai_aircraft3, ai_draw1, ai_draw2, ai_draw3,ai_miss_map)
            if player_win_check == 1 and ai_win_check == 1:
                print("The game ended in a draw")
                break
            elif ai_win_check == 1:
                print("AI won")
                break
            elif player_win_check == 1:
                print("You won")
                break


        else:
            ai_draw1,ai_draw2,ai_draw3,ai_miss_map ,player_win_check= player_board.player_move(ai_aircraft1,ai_aircraft2,ai_aircraft3,ai_draw1,ai_draw2,ai_draw3,ai_miss_map)

            ai_board.draw_a_plane_on_board(ai_aircraft1,ai_aircraft2,ai_aircraft3,ai_draw1,ai_draw2,ai_draw3,ai_miss_map)

            player_draw1, player_draw2, player_draw3,player_miss_map ,ai_win_check= ai_board.ai_move(player_aircraft1, player_aircraft2,player_aircraft3, player_draw1, player_draw2,player_draw3,player_miss_map,last_hit)
            player_board.draw_a_plane_on_board2(player_aircraft1, player_aircraft2, player_aircraft3, player_draw1,player_draw2, player_draw3, player_miss_map)
            if player_win_check == 1 and ai_win_check == 1:
                print("The game ended in a draw!!!")
                break
            elif player_win_check == 1:
                print("You won!!!")
                break
            elif ai_win_check == 1:
                print("The AI won!!!")
                break



if __name__ == "__main__":
    main()