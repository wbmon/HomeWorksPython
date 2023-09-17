# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

def withdraw(money):
    global balance, count
    count +=1
    perc_withdraw = money * 0.015
    if perc_withdraw < 30: perc_withdraw = 30
    if perc_withdraw > 600: perc_withdraw = 600
    print(f'За снятие средств взимается 1,5% от суммы снятия, но не менее 30 и не более 600: {perc_withdraw}')
    money += perc_withdraw

    if money > balance:
        print('У вас недостаточно средств')
        print(f'Баланс счета составляет {balance} ')
    else:
        print(f'Выдано {money}')
        balance -= money
        print(f'Баланс счета составляет {balance} ')
 
def supplement(money):
    global balance, count
    count += 1
    balance += money
    print(f'Баланс пополнен на {money} ')
    print(f'Баланс счета составляет {balance} ')

def set_amount():
    while True:
        try:
            n = int(input())
            if n % 50 != 0:
                raise  Exception
            return n
            break
        except ValueError:
           print('Неверный формат.')
        except Exception:
            print('Введите число кратное 50.')
        
balance = 0
count = 0 
while True:
    if count == 3:
        percentages = balance * 0.03
        print(f'После трёх операций мы снимаем 3% с Вашего счёта: {percentages}')
        balance -= percentages
        print(f'Баланс счета составляет {balance} ')
        count = 0
    if balance > 5_000_000:
        wealth_tax = balance * 0.1
        print(f'На Вашем счете сумма, превышающая 5 млн. Снимаем налог на богатство 10% с Вашего счёта: {wealth_tax}')
        balance -= wealth_tax
        print(f'Баланс счета составляет {balance} ')

    print('Выбор операции. 1 - пополнить, 2 - снять, 0 - выход')
    n = input()
    if n == '1':
        print('Введите сумму пополнения (кратную 50) >>: ')
        supplement(set_amount())
    elif n == '2':
        print('Введите сумму снятия (кратную 50) >>: ')
        withdraw(set_amount())
    elif n == '0':
        print('Работа завершена. До свидания!')
        break
    else:
        print('Неверная команда. Попробуйте еще раз.')