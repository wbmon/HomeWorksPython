# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

def calculating_fractions(frac1_str, frac2_str):
    num1, denom1 = map(int, frac1_str.split("/"))
    num2, denom2 = map(int, frac2_str.split("/"))

    sum_frac_num = num1 * denom2 + num2 * denom1
    sum_frac_denom = denom1 * denom2
    sum_frac = (sum_frac_num, sum_frac_denom)

    prod_frac_num = num1 * num2
    prod_frac_denom = denom1 * denom2
    prod_frac = (prod_frac_num, prod_frac_denom)
    return sum_frac, prod_frac

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


frac1_str = str(input('Введите первую дробь в формате a/b: '))
frac2_str = str(input('Введите вторую дробь в формате c/d: '))

sum_frac, prod_frac = calculating_fractions(frac1_str, frac2_str)
t1 = gcd(sum_frac[0],sum_frac[1])
print(f"Сумма дробей {frac1_str} и {frac2_str} равна {sum_frac[0] // t1}/{sum_frac[1] // t1}")
t2 = gcd(prod_frac[0],prod_frac[1])
print(f"Произведение дробей {frac1_str} и {frac2_str} равно {prod_frac[0] // t2}/{prod_frac[1] // t2}")

print('Проверка c помощью модуля fractions:')
num1, denom1 = map(int, frac1_str.split("/"))
num2, denom2 = map(int, frac2_str.split("/"))
f1 = fractions.Fraction(num1, denom1)
f2 = fractions.Fraction(num2, denom2)
print(f"Сумма дробей {frac1_str} и {frac2_str} равна {f1 + f2}")
print(f"Произведение дробей {frac1_str} и {frac2_str} равно {f1 * f2}")