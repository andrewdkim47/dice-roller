#DICE ROLLER# 
#5/7/2018
import random

print("\n")
user_input = 'h'

#repeats the rolling process
while user_input != 'q':
	#catch user input
	user_input = raw_input("Press \"r\" to roll a six sided die! (Press q to quit) \n")
	#doesnt roll if user enters q, breaks out of loop
	if (user_input == 'q'):
		break

    #catches anything other than q and r
	if(user_input != 'q' and user_input != 'r'):
		print("Sorry, that is an invalid input. Please try again!")
	else:
		#x is set to a random int between 1 and 6 inclusive
		x = random.randint(1,6)
		print "You rolled a", x, "\n"
    

print("Thanks for rollin")

