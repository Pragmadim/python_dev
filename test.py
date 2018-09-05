# Это программа «Угадай число»
import random
guessesTaken = 0
print('Желаешь разбогатеть, друг? Как тебя зовут?')
myName = input()
number = random.randint(1,20)
print('Ну тогда приступим? '+myName+', я загадал число от одного до 20')
while guessesTaken < 6:
    print('Как ты думаешь, какое?')
    print(number)
    #Перед функцией print() должно быть 4 пробела
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken+1
    if guess < number:
        print('Мое число больше твоего') #Перед функцией print() должно быть 8 пробелов
    if guess > number:
        print('Мое число меньше твоего')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Превосходно '+myName+'! Ты угадал число с '+guessesTaken+'попытки. Твой выигрыш 10 очков.')
if guess != number:
    number = str(number)
    print('Жаль, но у тебя не осталось попыток. Я загадал число '+number+'. Ты проиграл… Эй! Вы! Двое! Живо! Снимите ка с него шкуру!')
