import random,time

def rollDice():
    user_input = 'Y'
    while user_input != 'YES' or user_input != 'Y':

        if user_input == 'Y':
            outcome = random.randint(1, 6)
            print("Dice Is Rolling")
            for i in range(10):
                time.sleep(0.20)
                print("*",end="")
            print(f'\noutcome is {outcome}')

            user_input = (input('Want to Roll (Y,N): ')).upper()
            continue
        else:
            print('Thanks For Playing')
            break

#piyush