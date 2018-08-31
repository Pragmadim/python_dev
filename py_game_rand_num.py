import random

print('Welcome to my first Python game! Guess random generated number from 1 to 10!')

gen = input('Print generate to begin playing! \n')


def begin():
    l = 3  ## Кол-во жизней
    r_num = random.randint(1, 10)
    p_num = int(input('Enter your number: '))
    while l > 0:
        if p_num == r_num:
            print("You've won! Excellent!")
            play_again = input("Do you want to play again? y/n")
            if play_again == 'y' or play_again == 'Y':
                begin()
            else:
                print('Goodbye!')
        elif p_num < r_num:
            print("Your number is lower than it must be!")
            l -= 1
            print('You lost your life! Now you have only {}'.format(l))
            begin()
        elif p_num > r_num:
            print("Your number is higher than it must be!")
            l -= 1
            print('You lost your life! Now you have only {}'.format(l))
            begin()
        elif l == 0:
            print("Game Over! Your HP ended.")

if gen == 'generate':
    print('Success!')
    begin()
else:
    print('Fail!')
    print("Type 'Generate' to begin playing!")
