import random

while True:
    player=input("Enter[rock,paper,scissor]:")
    choose=["rock","paper","scissor"]
    computer=random.choice(choose)
    
    print(f"You choose{player},computer choose{computer}")
    
    if player==computer:
        print("Tie...")
        
    elif player=="rock":
        if computer=="scissor":
            print("You win")
            
        else:
            print("You lose")
    elif player=="paper":
        if computer=="rock":
            print("You win")
        else:
            print("You lose")
    elif player=="scissor":
        if computer=="paper":
            print("You win")
        else:
            print("You lose")
            continue
            
            
            
    