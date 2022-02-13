import random

while(1):
    choice=input("\t\tAre you ready to guess the number (yes/y or no/n): ")

    if(choice.lower() not in ["yes","y","no","n"]):
        print("\n\n\t\tStop wasting my time with illogical inputs!!")
    
    elif(choice.lower() in ["yes","y"]):
        generate_number=random.randint(1,100)
        user_number=int(input("\t\tso what did you guess: "))
        
        if(user_number==generate_number):
            print("\n\n\t\tWow!! you are one hell of a lucky guesser!!\n")

        elif(user_number>generate_number):
            print("\n\n\t\tOops!! You went a little higher than the number!!")
            print("\t\tBetter luck next time!!\n")
       
        else:
            print("\n\n\t\tOops!! You went a little lower than the number!!")
            print("\t\tBetter luck next time!!\n")

    else:
        print("\n\n\t\tyou are going too soon!! well bye-bye\n")
        break