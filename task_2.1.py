# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

def minimum(arr):
    pass

def maximum(arr):
    pass

def minimum(arr):
    min_val = arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
    return min_val

def maximum(arr):
    max_val = arr[0]
    for i in arr:
        if i > max_val:
            max_val = i
    return max_val

# Пример вызова функций:
arr = [4,6,2,1,9,63,-134,566]
print(minimum(arr)) # -134
print(maximum(arr)) # 566
