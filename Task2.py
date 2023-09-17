# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

HEX: int = 16
NUM: int = int(input('Введите число: '))

hex_digits = "0123456789abcdef"
hex_str = ""
num = NUM

while num > 0:
    hex_str = hex_digits[num % HEX] + hex_str
    num = num // HEX

print(f"Шестнадцатеричное представление числа {NUM} = {hex_str}")
print('Проверка:')
print(f'{hex(NUM) = :>10}')
