# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

def non_repeat_numbers(array):
    s_array = set(array)   # создаем множество из исходной последовательности
    array_vih = []         # создаем пустой массив
    for num_s in s_array:  # перебором множества и исходного массива, 
        count = 0          # подсчитываем количество повторений чисел
        for num in array:
            if num == num_s:
                count += 1
        if count == 1:
            array_vih.append(num_s)
    return array_vih


list = [2, 1, 1, 29, 34, 4, 5, 29]
print(non_repeat_numbers(list))
