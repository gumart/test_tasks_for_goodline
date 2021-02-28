import sys

try:
    path = sys.argv[1] # Получение пути до директории в которой лежит файл

except IndexError:
    path = '' # По умолчанию файл ищется в текущей директории

try:
    f = open(path+'numbers.csv', 'r') # Открытие файла на чтение
    
    for numbers in f:
        
        string_numbers = numbers # Получение строки из файла

    string_numbers = string_numbers.split(',') # Разбиение строки на список строк

    numbers = list() 

    for number in string_numbers:
        
        numbers.append(int(number)) # Конвертация строк в целые числа

    numbers.sort() # Сортировка

    print(numbers)

except FileNotFoundError:
    
    print("Файл отсутствует в данной директории")

except ValueError:

    print("Файл должен содержать только числа")

finally:
    f.close() # Закрытие файла