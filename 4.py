# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           }

def degree(deg):
    degrees = ""
    temp = str(deg)
    for char in temp:
        degrees += indexes[char]
    return degrees

def polonomial(k):
    polinom = ""
    if k == 0:     
        return str(random.randint(0,100)) + "=0"
    return str(random.randint(0,100)) + 'x' + degree(k) + '+' + polonomial(k-1)
k = int(input("Введите степеть многочлена "))
print(polonomial(k))