import random

f = open('numbers.csv', 'w') # Создания файла для записи

for i in range(99):

    f.write(str(random.randint(1, 100)) + ',') # Запись случайных чисел в файл

f.write(str(random.randint(1, 100)))

f.close() # Закрытие файла