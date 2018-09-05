import random


def begin():
    life = 5
    r_num = random.randint(1, 10)
    while life >= 1:
        p_num = int(input("Enter a number: "))
        if r_num > p_num:
            #print(r_num)
            print("Your number is less. Try again!")
            life = life - 1
            print("You've lost one life. Only {} left!".format(life))
        elif r_num < p_num:
            #print(r_num)
            print("Your number is bigger. Try again!")
            life = life - 1
            print("You've lost one life. Only {} left!".format(life))
        elif r_num == p_num:
            #print(r_num)
            print("You're right! Thanks for playing!")
            break


begin()



