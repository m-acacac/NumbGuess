class PlayGame:
    
    def __init__(self):
        self.tries = 0
        self.keep_going = True
        self.key_list = []
        self.output = ''
        self.end = False
        self.input_list = []
        self.ref_list = []
        self.check_list = []
        self.go_again = True
        output = ''
        print("\033[37m","\033[40m","""This is a game similar to the famous WORDLE, but instead of guessing a 6-letter word, you get to guess a PIN of
 any length you choose. Digits not in the PIN will show up as red, digits in the wrong place will be yellow,
 and digits guessed correctly will be green. Keep in mind,numbers can repeat. Type 'stop' while the game is 
 running to end the game.""")
        print ('')
        
    def ask_for_length(self):
        length = input('How many digits? ')
        if length.lower() == 'stop':
            self.end = True
        else:
            self.length = int(length)
            
    def build_a_key(self):
        import random
        x = 0
        while x < self.length:
            self.key_list.append(random.randint(0,9))
            x = x +1
    
    def ask_for_inputs(self):
        self.ref_list = []
        self.input_list = []
        self.check_list = []
        right_length = False
        while right_length == False:
            print('')
            print('')
            guess = input('GUESS #' + str(self.tries + 1) + ': ')
            if guess.lower() == 'stop':
                self.end = True
                break
            elif len(guess) == self.length:
                right_length = True
            else:
                print('')
                print("\033[37m", 'Wrong number of digits. Try again!')
        
        if not self.end:
            for digit in guess:
                self.input_list.append(int(digit))
                self.ref_list.append(int(digit))
        self.tries +=1
                
    def check_against_list(self):
        for x,y in zip(self.input_list, self.key_list):
            if x == y:
                self.check_list.append('green')
            elif x in self.key_list:
                if self.input_list.count(x)<= self.key_list.count(x):
                    self.check_list.append('yellow')
                else:
                    self.input_list[self.input_list.index(x)]= 10
                    self.check_list.append('red')
            else:
                self.check_list.append('red')
    
    def print_output(self):
        for x,y in zip(self.check_list, self.ref_list):
            if x == 'green':
                print ("\033[32m", str(y),"\033[37m",end = '')
            elif x == 'red':
                print ("\033[31m", str(y),"\033[37m",end = '')
            else:
                print ("\033[33m", str(y),"\033[37m",end = '')
                
    def check_if_won(self):
        if 'red' not in self.check_list and 'yellow' not in self.check_list:
            self.key_list = []
            print('')
            print ("\033[37m",'You solved the puzzle in ' + str(self.tries) + ' tries! ')
            self.tries = 0
            go_again = input('Do you want to go again? ')
            if go_again.lower() == 'yes':
                self.go_again = True
                self.keep_going = False
            else:
                self.end = True
                self.end_game()
                
    def end_game(self):
        if self.key_list != []:
            for item in self.key_list:
                self.output += str(item)
            print('Game stopped. Pin was: ' + self.output)
        else:
            print('Game stopped.')
        self.keep_going = False
        self.go_again = False
        
