print(" WELCOME TO TREASURE ISLAND")
print("YOUR MISSION IS TO FIND THE TREASUE")
choice=input(" left'L' or right'R'")
print(choice)
if choice=='R':
    print("game over")
if choice=='L':
    choice2=input("swim'S' or wait'W'")
    if choice2=='S':
        print("game over")
    if choice2=='W':
        choice3=input(" which door 'red=R','blue=B','yellow=Y'")
        if choice3=='R':
            print(" game over")
        elif choice=='B':
            print(" GAME OVER")
        elif choice=='Y':
            print("YOU WIN")
        else:
            print(" game over")
    else:
        print("game over")
else:
    print("GAME OVER")
            
        
    
