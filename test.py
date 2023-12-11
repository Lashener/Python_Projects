print("Welcome to Questions Quiz.")

Playing = input("Would you like to play? \n")

if Playing == "yes":
    print("Okay Game is initiating!")
elif Playing != "yes":
    quit()

name = input("what would you like to be called \n")

print( "Okay " + str(name) + " Your first question is")

answer_1 = input("What is the capital of Colorado? \n")
if answer_1 == "Denver":
    print("That is correct! Great job " + str(name))
elif answer_1 != "Denver":
    print("Better luck next question.... you got this " + str(name))

answer_2 = input("What does DHCP stand for? \n")
if answer_2 == "Dynamic Host configuration Protocol":
    print("That is correct! Great job " + str(name))
elif answer_2 != "Dynamic Host configuration Protocol":
    print("Better luck next question.... you got this " + str(name))

answer_3 = input("Who is the president of the united states? \n")
if answer_3 == "Joseph Biden":
    print("That is correct! Great job " + str(name))
elif answer_3 != "Joseph Biden":
    print("Better luck next question.... you got this " + str(name))

answer_4 = input("who was president before the current president? \n")
if answer_4 == "Donald Trump":
    print("That is correct! Great job " + str(name))
elif answer_4 != "Donald Trump":
    print("Better luck next question.... you got this " + str(name))

answer_5 = input("what car is called the helephant? \n")
if answer_5 == "Dodge Duragno Cidatel":
    print("That is correct! Great job " + str(name))
elif answer_5 != "Dodge Duragno Cidatel":
    print("Better luck next question.... you got this " + str(name))

