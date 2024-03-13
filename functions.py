import classes
def guess_the_number():
    game = classes.PlayGame()
    while game.go_again:
        game.keep_going = True
        
        game.ask_for_length()
        
        if game.end:
            game.end_game()
            return None
        
        game.build_a_key()
        
        while game.keep_going:
            game.ask_for_inputs()
            
            if game.end:
                game.end_game
                return None
            
            game.check_against_list()
            game.print_output()
            game.check_if_won()