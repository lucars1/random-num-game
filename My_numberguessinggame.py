import sys
import random
global trys
trys = 6
global randomnum
randomnum = random.randrange(0, 100)
print(randomnum)
def to100game():
    
    guess = int(input('What is you\'re guess?: '))
    
    if randomnum == guess:
        print("Correct!")
        sys.exit()
        
    if randomnum != guess:
        print('Incorrect!')
        global trys
        trys -= 1
        print('you have',trys, 'to get it right')
to100game()
to100game()
to100game()
to100game()
to100game()
to100game()