# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT) 

from random import randint

guesses_made = 0
number = randint(0, 1000)
print ('Я загадал число между от 0 до 1000. Сможешь угадать его за 10 попыток?')

while guesses_made < 10:
    guesses_made += 1
    print ('Попытка', guesses_made,'. Введи число: ', end = ' ')
    guess = int(input())
    if guess < number:
        print ('Твое число меньше того, что я загадал.')
    if guess > number:
        print ('Твое число больше загаданного мной.')
    if guess == number:
        break
if guess == number:
    x = {2, 3, 4}
    y = {1}
    if guesses_made in x:
        print ('Ты угадал мое число, использовав %s попытки!' % guesses_made)
    elif guesses_made in y:
        print ('Ты угадал мое число, использовав %s попытку!' % guesses_made)
    else:
        print ('Ты угадал мое число, использовав %s попыток!' % guesses_made)
else:
    print ('Не угадал! Я загадал число %s' % number)