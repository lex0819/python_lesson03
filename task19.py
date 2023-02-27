# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

#slice full is Lst[ Initial : End : IndexJump ]
#slicing is list[start:end]

input_list = input("Enter some elements separated by spaces: ").split()
shift = int(input("Enter shift: "))

k = shift % len(input_list)

output_list = input_list[k :]+input_list[: k]

print(input_list)
print(output_list)