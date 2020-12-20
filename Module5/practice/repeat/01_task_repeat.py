# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random
def gen_list(size, at, to):
    numbers = []
    for _ in range(size):
        numbers.append(random.randint(at, to))
    return numbers
list1 = gen_list(5, -100, 200)
print(list1)
