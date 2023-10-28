import random
print("0 => For Rock\n1 => For Scissors\n2 => For Papers")


rock = '''
    _______
---'   ____)
      (_____)
      (____)
---   (____)
   '__(___)
'''

paper = '''
    ______
   '   ___)___
---      _____)
         ______)
----     ______)
    '________)

'''

Scissors = '''
    ________
---'   _____)___
         _______)
       __________)
____   (____)
    '__(__)  
 
'''
for i in range (1,100):
    
    users_choice = int(input("Enter your choice = "))
    computer_choice = random.randint(0,2)
    
    if computer_choice == users_choice or users_choice == computer_choice:
        if computer_choice == 0 and users_choice == 0:
            print(f"Users Choice = (Rock){rock}")
            print(f"Computers choice = (Rock){rock}")
            print("The Mactch is draw.")
        elif computer_choice == 1 and users_choice == 1:
            print(f"Users Choice = (Scissors){Scissors}")
            print(f"Computers choice = (Scissors){Scissors}")
            print("The Mactch is draw.")
        elif computer_choice == 2 and users_choice == 2:
            print(f"Users Choice = (paper){paper}")
            print(f"Computers choice = (paper){paper}")
            print("The Mactch is draw.")  
    elif(users_choice==0 and computer_choice==1):
        print(f"Users Choice = (Rock){rock}")
        print(f"Computers choice = (Scissors){Scissors}")
        print("You won.") 
    elif(users_choice==0 and computer_choice==2):
        print(f"Users Choice = (Rock){rock}")
        print(f"Computers choice = (paper){paper}")
        print("You lose.")
    elif(users_choice==1 and computer_choice==0):
        print(f"Users Choice = (Scissors){Scissors}")
        print(f"Computers choice = (Rock){rock}")
        print("You lose.") 
    elif(users_choice==1 and computer_choice==2):
        print(f"Users Choice = (Scissors){Scissors}")
        print(f"Computers choice = (paper){paper}")
        print("You won.")
    elif(users_choice==2 and computer_choice==0):
        print(f"Users Choice = (paper){paper}")
        print(f"Computers choice = (Rock){rock}")
        print("You lose.")
    elif(users_choice==2 and computer_choice==1):
        print(f"Users Choice = (paper){paper}")
        print(f"Computers choice = (Scissors){Scissors}")
        print("You lose.")
    else:
        print("Please Enter Correct Choice.")
