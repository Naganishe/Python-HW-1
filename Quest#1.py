# 1. Напишите программу, которая принимает на вход цифру, 
#    обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите номер дня недели: ')
n = int(input())
n1 = range(1, 6)
if n == 6 or n == 7:
    print('yes')
elif n in n1:
    print('no')
else:
    print('input number 1 - 7')