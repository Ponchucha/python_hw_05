# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def get_degree(number, deg):
    if deg == 0:
        return 1
    elif deg == 1:
        return number
    elif deg < 0:
        return 1/(number * get_degree(number, abs(deg) - 1))
    else:
        return number * get_degree(number, deg-1)

print(get_degree(10, -3))
