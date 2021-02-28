import sys

class NumberError(Exception):
    pass

class ExtentError(Exception):
    pass

def elevate(number, extent): # Рекурсивная функция возведения в степень
    if extent == 0:
        return 1
    else:
        return number * elevate(number, extent-1)

try:
    number = int(sys.argv[1]) # Получение числа из коммандной строки
    extent = int(sys.argv[2]) # Получение степени из коммандной строки

    if number < 1 or number > 10:
        
        raise NumberError("Переданно невалидное число")
    
    if extent < 0 or number > 9:
        
        raise ExtentError("Переданна невалидная степень")

    print(elevate(number, extent)) 


except IndexError:
    print("Переданны не все аргументы. Программа принимает на вход 2 аргумента.")

except ValueError:
    print("Указанны не валидные аргументы. Программа принимает на вход только целые числа")

except NumberError:
    print("Переданное число должно быть в диапазоне от 1 до 10")

except ExtentError:
    print("Переданная степень должна быть в дипазоне от 0 до 9")
