# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def input_number(inputText):
    is_OK = False
    while not is_OK:
        try:
            low, hi = 0, 100000
            while True:
                try:
                    n = int(input(f"{inputText}"))
                except ValueError:
                    print('Повторите ввод')
                    pass
                else:
                    if low < n < hi:
                        break
                    print('Повторите ввод')
            is_OK = True
        except ValueError:
            print("Нужно ввести число!")
    return n

n = input_number("Введите целое число от 0 до 100 000: ")
counter = 0
for i in range(1, n + 1):
    if n % i == 0:
        counter += 1
if counter == 2:
    print ('Простое число')
else:
    print ('Составное число')
