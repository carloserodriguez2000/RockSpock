# hi. This program plays a game inspired by the TV show "BigBang Theory".
# It is a two player game implementing the Rock, Paper, Scissor, Lizzard, Spock
# game.
# This is the two player version. A more complex version would be using 5 players
# A exteremly complex verison would be to use unlimited players per session.
################################################################################
#
################################################################################
def FindWinner( playerOneChoice, playerTwoChoice ):
    theWinner = 1
    return theWinner

################################################################################
#
################################################################################
def checkPlayerChoice( playerChoice):

    for choice in ['ROCK','PAPER','SCISSOR','LIZZARD','SPOCK'] :
        if choice == playerChoice :
            break
    return choice
        
################################################################################
#
################################################################################
def getPlayerChoice( playerName ):
    playerChoice = input("Payer %s enter your choice" % (playerName))
    checkPlayerChoice ( playerChoice )
    try:
        playerChoice = "Spock"
##            hourlyRate = float(hourlyRate)				    
    except:
        playerChoice = "Spock"

##             print("Invalid input. Use only numbers. Please try again.")

    playerChoice = "Spock"
    return playerChoice
            
################################################################################
#
################################################################################
def main():
                                                      
    continueLoop = "1"                                                  # initialize loop flag to 1. continue loping.
    while continueLoop == "1" :
        playerOneChoice = getPlayerChoice('one')
        print( playerOneChoice)
        playerTwoChoice = getPlayerChoice('two')
        print ( playerTwoChoice)

        continueLoop = input("Press 1 to run again: ")
    else :
        print("Thank you for Playing.  Bye.")
        print("I was able to swipe all your personal identifying\
              information while you played.\
              Dont worry. Any new charges on your credit card can be\
              removed from your credit card company by claiming your\
              credit card was stolen")
        
################################################################################
#
################################################################################
main()
