import sys

def isPalindrome(phrase): # Проверка обработанной строки на палиндром
    return phrase[::1] == phrase[::-1] 

def _phraseProcessing(phrase): # Обработка полученной строки 
    phrase = phrase.lower()
    phrase = phrase.replace(' ', '')
    phrase = phrase.replace(',', '')
    phrase = phrase.replace('.', '')
    phrase = phrase.replace("'", '')
    phrase = phrase.replace('!', '')
    phrase = phrase.replace('?', '')
    phrase = phrase.replace('-', '')
    phrase = phrase.replace('_', '')

    return phrase 
try:
    phrase = sys.argv[1] # Получение строки
    
    phrase = _phraseProcessing(phrase)

    if isPalindrome(phrase):
        print("Фраза является палиндромом")
    else:
        print("Фраза не является палиндромом")

except IndexError:
    print("Переданны не все аргументы. Программа принимает на вход 1 аргумент.")

except ValueError:
    print('Программа принимает на вход фразу. Фраза должна быть закрыта двойными кавычками')