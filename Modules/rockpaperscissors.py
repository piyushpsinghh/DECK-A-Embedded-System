import random
def rockPaperScissors():
    num=int(input("How Many Times You Want To Play: "))

    for i in range(1,num+1):
        user=input("Enter r for rock p for paper s for scissors: ").lower()
        computer=random.choice(['r','p','s'])
        if(user==computer):
            print("Its a Tie")
        elif((user=="r" and computer=="s") or (user=="p" and computer=="r") or (user=="s" and computer=="p")):
            print("You Won")
        else:
            print("You Lost")

# rockPaperScissors()
#piyush