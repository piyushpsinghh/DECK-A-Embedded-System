import random
def game(n):
    chances=5
    random_num = random.randint(1,n)
    guess = int(input("Enter the Number: "))
    chances=chances-1
    print(f"You have {chances} left")
    while(random_num != guess and chances!=0):
        if(guess<random_num):
            print("Number is low")
            guess = int(input("Enter the Number: "))
            chances=chances-1
            print(f"You have {chances} left")
        elif(guess>random_num) :
            print("Number is High")
            guess = int(input("Enter the Number: "))
            chances=chances-1
            print(f"You have {chances} chances left")
    if(chances==0):
        print(f"The Correct Answer Was {random_num}")
    else:
        print(f"Nice!! {random_num} is the correct answers.You had {chances} chances left")
    input("Press Enter to Continue")

def guessGame():
    print("1 For Easy   1-20")
    print("2 For Medium 1-50")
    print("3 For Hard   1-100")
    try:
        level=int(input())
    except ValueError as val:
        print("Invalid Input")
        level=int(input())
    if(level==1):
        game(20)
    elif(level==2):
        game(50)
    elif(level==3):
        game(100)
    elif(level>3 or level<=0):
        print("invalid Input")
