#Rock Paper Scissors game
import random

#Here we define our first function and create a list that will be where the user and the computer will draw their answer from
def Play_Game():
    list = ["rock" , "paper" , "scissors"]
    
#player chooses an option
    player_choice = input(" please choose one of the following: rock, paper, or scissors! \n\n")
    plyr_choice = player_choice.lower()
    
#computer chooses an option
#use internet research
    comp_choice = random.choice(list)
    print(comp_choice)
    
#comparison: This step involves creating the if statments that the game runs off of
#each if statment is based off of what the user inputs as their answer choice
#then the computer iwll randomly generate an answer from the list we gave it to pick from.
#for each answer (rock, paper, or scissors) the main if statement contains the players choice
#then the indented if statement following the main if statement contains the computers choice and prints different text
#based on the randomized choice of the computer.
#there are three main if statements for each choice that the user can make. 

    if plyr_choice == "rock":
        if comp_choice == "paper":
           print("you lose... best 2 out of 3? \n\n the computer wins")
        elif comp_choice == "scissors" :
           print("good one! I'll get you next time. \n\n the computer loses")
        else:
           print("great minds think alike... may the greatest mind win! \n\n this is a tie")
    
    if plyr_choice == "scissors":
        if comp_choice == "rock":
           print("to bad you didnt draw a jack hammer... \n\n the computer wins!")
        elif comp_choice == "paper":
           print("man paper is so weak! \n\n the computer loses!")
        else:
           print("what a coincidnece, you could be edward scissor hands! \n\n this is a tie!")
    
    if plyr_choice == "paper":
        if comp_choice == "scissors":
           print("i told you paper was weak! \n\n the computer wins!")
        elif comp_choice == "rock":
           print("Geez what a gamble... \n\n the computer loses!")
        else:
           print("paper paper, whose got the paper? oh wait its us. \n\n this is a tie")

#Once the if staements for each user choice are made, then we can write the code for the game to continue on to the next round 
#or if we wanted to end the game.
#first we create a main function and call the first Play_Game function. then we ask for input if we want to play again.
# there is an if statement to differentiate between saying yes and playing again and saying no. then to finish off the game 
#we call the main function. this will allow us to play over and over again if we so choose.
def main():
    Play_Game()
    ask = input("would you like to play again yes/no? \n")
    
    if ask.lower() == "yes":
        main()
    else:
      print("thanks for playing that was fun have a good day!!")
main()
