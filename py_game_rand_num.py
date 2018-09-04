import random


def begin():
    r_num = random.randint(1, 10)
    p_num = int(input('Enter your number: '))
    ch = (r_num, p_num)
    if ch[0] == ch[1]:
        print(ch[0])
        print("You've won! Excellent!")
        play_again = input("Do you want to play again? y/n")
        if play_again == 'y' or play_again == 'Y':
            begin()
        elif play_again == 'n' or play_again == 'N':
            print('Goodbye!')
    elif ch[1] < ch[0]:
        print(ch[0])
        print("Your number is lower than it must be!")
        begin()
    elif ch[1] > ch[0]:
        print(ch[0])
        print("Your number is higher than it must be!")
        begin()


def start():
    gen = input('Print generate to begin playing! \n')
    if gen == 'generate':
        print('Success!')
        begin()
    else:
        print('Fail!')
        start()


print('Welcome to my first Python game! Guess random generated number from 1 to 10!')
start()
