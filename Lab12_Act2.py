# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Carlos Velazquez   
#               Chet Beasely
#               Christopher Winsett
#               Oluwaseyi Johnson           
# Section:      522
# Assignment:   Lab11a_Act2
# Date:         21 November 2021
#

      

endscore = open('Endscore.txt','w+') #Opens file to write
endscore.write('Winner'+8*' '+'Loser'+8*' '+'Score\n') #Writes string
import random
import turtle

def pig():
    '''This is the standard version of the dice game 'PIG'. To view the rules of the game, enter one of the acceptable inputs for RULES'''
    ####STANDARD PIG GAME#####
    # dice roll simulator using randint function
    exit2menu = 0

    def rolldice(): # Rolls dice
        '''Rolls dice'''
        return random.randint(1,6)
    # here first index is for 1st player and 2nd for 2nd player
    player_score = [0,0]
    roundscore = [0,0]
    # it will tell the turn of player (turn+1)
    turn = 0
    # until anyone reaches the 100 mark
    player1 = input("Enter a name for Player 1: ")
    player2 = input("Enter a name for Player 2: ")
    currentplayer = player1    
    while player_score[0] < 100 and player_score[1] < 100 and exit2menu == 0:
    # print whose turn it is:
        
        print("\n-  -  -  -  -  -  -  -  -  -  -\n\n",currentplayer,"'s turn", sep = '')
    # Displaying their score and giving them option to hold or roll
        while True:
            print(currentplayer,"'s current round score is: ",roundscore[turn], sep = '') #Prints round score
            print(currentplayer,"'s current total score is: ",player_score[turn], sep = '') #Prints current score
            try: #Handles error if wrong input
               choice = input("Enter an 'R' to roll or an 'H' to hold or enter 'MENU': ") #Enter R, H, or MENU
            except:
                print("Invalid entry, please try again.") 
            if choice == 'R': #If R, roll dice
                dice_roll = rolldice()
        # printing what roll came
                print("You rolled a",dice_roll)
                if dice_roll != 1:
                    roundscore[turn] += dice_roll
                        
                else:
                    roundscore[turn]=0
                    break
            if choice == 'H': #If H, player doesn't get any points and next player's turn 
                player_score[turn] += roundscore[turn]
                roundscore[turn]=0
                break
            if choice == 'MENU': #Goes back to menu
                 exit2menu = 1
                 break

    # giving the turn to other player
        turn = (turn+1)%2
        if turn == 1:
            currentplayer = player2
        if turn == 0:
            currentplayer = player1
    if player_score[0] >= 100: #Displays the winner
        style=('Arial',30)
        print("\nGame Over! Please view the turtle graphic!\nClose the graphic window to return to the main menu.")
        turtle.write(player1+'\nWins!',font=style,align='center')
        turtle.hideturtle()
        turtle.done()
        turtle.bye()
        exit2menu = 1
        endscore(player_score,player2,player1)
        
    if player_score[1] >= 100: #Displays the winner
        print("\nGame Over! Please view the turtle graphic!\nClose the graphic window to return to the main menu.")
        style=('Arial',30)
        turtle.write(player2+'\nWins!',font=style,align='center')
        turtle.hideturtle()
        turtle.done()
        turtle.bye()
        exit2menu = 1
        endscore(player_score,player2,player1)
    if exit2menu == 1:
        MENU()


def twopig():
    '''This is Two-Dice Pig game. To view the rules of the game, enter one of the acceptable inputs for RULES'''
    ####Two-dice PIG GAME#####
    # dice roll simulator using randint function
    def rolldice1():
        '''Rolls dice 1'''
        return random.randint(1,6)
    def rolldice2():
        '''Rolls dice 2'''
        return random.randint(1,6)
    exit2menu = 0
    # here first index is for 1st player and 2nd for 2nd player
    player_score = [0,0]
    roundscore = [0,0]
    # it will tell the turn of player (turn+1)
    turn = 0
    # until anyone reaches the 100 mark
    player1 = input("Enter a name for Player 1: ")
    player2 = input("Enter a name for Player 2: ")
    currentplayer = player1
    double = 0
    while player_score[0] < 100 and player_score[1] < 100 and exit2menu == 0:
    # print whose turn it is:
        print("\n-  -  -  -  -  -  -  -  -  -  -\n\n",currentplayer,"'s turn", sep = '')
    # Displaying their score and giving them option to hold or roll
        while True:
            print(currentplayer,"'s current round score is: ",roundscore[turn], sep = '') #Prints round score
            print(currentplayer,"'s current total score is: ",player_score[turn], sep = '') #Prints current score
            if double == 1:
                choice = 'R'
            else:
                try:
                   choice = input("Enter an 'R' to roll or an 'H' to hold or enter 'MENU': ") #Enter R, H, or MENU
                except:
                    print("Invalid entry, please try again.")
            if choice == 'R': #If R, roll dice
                dice_roll1 = rolldice1()
                dice_roll2 = rolldice2()
    # printing what rolls came
                print("You rolled a",dice_roll1,"and a", dice_roll2)
              #  if they roll one 1
                if dice_roll1 == 1: 
                     if dice_roll2 != 1: #If dice1 and dice2 doesn't land on 1, round score goes back to 0
                         roundscore[turn] = 0
                         double = 0
                         break  
                     if dice_roll2 == 1: #If dice1 and dice2 land on 1, curent score goes back to 0
                         player_score[turn]=0
                         roundscore[turn]=0
                         double = 0
                         break                
                if dice_roll2 == 1:
                     if dice_roll1 != 1: #If dice2 and dice1 doesn't land on 1, round score goes back to 0
                         roundscore[turn] = 0
                         double = 0
                         break 
                     if dice_roll1 == 1: #If dice2 and dice1 land on 1, curent score goes back to 0
                         player_score[turn]=0
                         roundscore[turn]=0
                         double = 0
                         break
                     
                        
                #if they are both 1s          
                if dice_roll1 + dice_roll2 == 2:
                     player_score[turn]=0
                     roundscore[turn]=0
                     #not a double
                     double = 0
                     break
                #if they roll no 1s
              #if dice rolls without 1s
                else:
                    #if they are equal and not 1
                     if dice_roll1 == dice_roll2:
                         print("You rolled a double! Rolling again...")
                         roundscore[turn] += (dice_roll1 + dice_roll2)
                         #is a double, begins second roll
                         double = 1
                     #if they are not equal and not 1
                     else:
                         roundscore[turn] += (dice_roll1 + dice_roll2)
                         double = 0
           # choose to hold
            if choice == 'H':
                player_score[turn] += roundscore[turn]
                roundscore[turn]=0
                break
            #ends turn above
            #if they choose to go to menu
            if choice == 'MENU':
                exit2menu = 1
                break
                
    # giving the turn to other player
        turn = (turn+1)%2
        if turn == 1:
            currentplayer = player2
            #designates who the current player is for the text to show up correctly
        if turn == 0:
            currentplayer = player1
            #if player 1 wins
    if player_score[0] >= 100:
#turtle showing winner and name after text
        print("\nGame Over! Please view the turtle graphic!\nClose the graphic window to return to the main menu.")
        style=('Arial',30)
        turtle.write(player1+'\nWins!',font=style,align='center')
        turtle.hideturtle()
        turtle.done()
        turtle.bye()
        #exits to menu
        exit2menu = 1
        #sets endscore for txt file
        endscore(player_score,player2,player1)
#if player 2 wins
    if player_score[1] >= 100:
        #turtle and text again
        print("\nGame Over! Please view the turtle graphic!\nClose the graphic window to return to the main menu.")
        style=('Arial',30)
        turtle.write(player2+'\nWins!',font=style,align='center')
        turtle.hideturtle()
        turtle.done()
        turtle.bye()
        #menu
        exit2menu = 1
#        for text file
        endscore(player_score,player2,player1)
 #If player wanted to exit 
    if exit2menu == 1:
        #calls menu
        MENU()

#rules of pig function
def pigrules():
#called when player goes to rules or standard pig from menu
    '''Rules for Pig game'''
    print("\n-  -  STANDARD PIG RULES:  -  -")
    print("""\n-Each turn, the specified player rolls a die until they either choose to "hold" or they roll a 1.""")
    print("-If the player rolls a number other than 1, that number is added to their turn total, and turn continues.")
    print("-If the player rolls a 1, they lose all points for the round, and it becomes the next player's turn.")
    print("""-If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.""")
    print("-The first player to score 100 or more points wins.")
    print("\n-  -  -  -  -  -  -  -  -  -  -")

def twodierules():
#called when player goes to rules or 2-die pig from menu
    '''Rules for Two-Dice Pig game'''
    print("\n-  -  TWO-DICE PIG RULES:  -  -")
    print("\n-Two standard dice are rolled. If neither shows a 1, their sum is added to the turn total.")
    print("-If the player rolls a single 1, they lose all points for the round, and it becomes the next player's turn.")
    print("-If both die land on 1, though, the player’s entire score is reset to 0, and it becomes the next player's turn.")
    print("-If a double is rolled, the point total is added as usual, but the player is forced to roll again ")
    print("\n-  -  -  -  -  -  -  -  -  -  -")


def rulebook():
    #called from rules section of menu, displays all rules
    '''Calls rules for Pig game and Two-Dice Pig game'''
    print("\n-  -  -  PIG RULEBOOK:  -  -  -")
    pigrules()
    twodierules()
    #if player chooses to exit rulebook entering MENU calls the menu()
    exit2menu = input("To return to the main menu, enter 'MENU': ")
    if exit2menu == 'MENU':
        MENU()


def instructions():
    #called from instructions section of menu, displays instructions
    '''Instructions of what to do to play the game'''
    print("\n-  -  -  INSTRUCTIONS:  -  -  -")
    print("\n-Enter the names when prompted for Players 1 and 2")
    print("""-When asked if you want to continue a turn, enter "YES" to continue, and enter "NO" or "HOLD" to hold""")
    print("""-To see the current score of the game at any time, enter "SCORE" """)
    print("""-To return to the menu and quit the game at any time, enter "MENU" """)
    print("\n-  -  -  -  -  -  -  -  -  -  -")
    #if player chooses to exit rulebook entering MENU calls the menu()
    exit2menu = input("To return to the main menu, enter 'MENU': ")
    if exit2menu == 'MENU':
        MENU()

#main menu of game, shows up when program is run, is base spot for user to get to different games or to see rules and instructions
def MENU():
    '''This is the menu so player can choose what game to play, look at instructions, or look at rules'''
    print("\n-  -  -  Pig Game Menu  -  -  -")
    print("\n1: Pig (standard)\n-  Enter 'PIG' or 'pig' or '1'.\n\n2: Two-Dice Pig\n-  Enter 'TWO' or 'two' or '2'.\n\n3: Rules\n-  Enter 'RULES' or 'rules' or '3'.\n\n4: Instructions\n-  Enter 'INS' or 'ins' or '4'.\n\n5: Exit\n-  Enter 'EXIT' or 'exit' or '5'.\n\nOpen 'Endscore.txt' to see the history of games played during this run.")
    print("\n-  -  -  -  -  -  -  -  -  -  -")
#designates what is run based on input from user
    menuchoice = input("Enter your preferred destination as listed above: ")
    if menuchoice == 'PIG' or menuchoice == 'pig' or menuchoice == '1':
        pigrules()
        pig()
    if menuchoice == 'TWO' or menuchoice == 'two' or menuchoice == '2':    
        twodierules() 
        twopig()
    if menuchoice == 'RULES'or menuchoice == 'rules' or menuchoice == '3':
        rulebook()
    if menuchoice == 'INS' or menuchoice == 'ins' or menuchoice == '4':
        instructions()
  #if user enters exit, the function will end in case they want to stop playing or view docstrings
    if menuchoice == 'EXIT' or menuchoice == 'exit' or menuchoice == '5':
        print("Thanks for playing!")
    else: 
#if they enter something other than the above entries
        print("\nInvalid entry, please try again.")
        #sends them back to menu
        MENU()
    return menuchoice
#sets endscore for txtfile to be appended
def endscore(player_score,player2,player1):
    '''Writes the winner, loser, and score of each game to a file'''
#opens file
    endscore = open('Endscore.txt','a')
#if player 2 won
    if player_score[1]>player_score[0]:
        #if player 2 name is shorter than 6 characters
       if len(player2) < 6:
 #space after name is subtracted from 6
           space = (6 -len(player2)) * ' '
           endscore.write(player2+space + ' '*8)
           #for formatting
       else:#if not shorter than 6 characters
           space = (14 - len(player2)) * ' '
           endscore.write(player2+space)
          # formatting
          #if length of player 1 name is less than 5
       if len(player1) < 5:
           space = (5 -len(player1)) * ' '
           #formatting final appearance of txt file
           endscore.write(player2+space + ' '*8 + str(player_score[1])+'-'+str(player_score[0])+'\n')
       else:
           space = (13 - len(player1)) * ' '
           #formatting final appearance of txt file

           endscore.write(player1+space+ str(player_score[1])+'-'+str(player_score[0])+'\n')
   
    #if player 1 won, same stuff
    if player_score[0]>player_score[1]:
       if len(player1) < 6:
           space = (6 -len(player1)) * ' '
           endscore.write(player1+space + ' '*8)
       else:
           space = (14 - len(player1)) * ' '
           endscore.write(player1+space)
       if len(player2) < 5:
           space = (5 -len(player2)) * ' '
           endscore.write(player2+space + ' '*8 + str(player_score[0])+'-'+str(player_score[1])+'\n')
       else:
           space = (13 - len(player2)) * ' '
           endscore.write(player2+space+ str(player_score[0])+'-'+str(player_score[1])+'\n')
        
#calls main menu, this is the first thing that appears to user
MENU()
     




