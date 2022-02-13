import random

while(1==1):
    choice = input("do you want to roll the dice (yes/y or no/n): ")
    
    if(choice.lower() not in ["yes","y","no","n"]):
        print("enter a valid choice!!")

    elif(choice.lower() in ["yes","y"]):
        generate_number=random.randint(1,6)
        print("the no. is: ",generate_number)

    else:
        break

print("thanks for playing the game!!")
