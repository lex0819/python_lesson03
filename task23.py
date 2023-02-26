# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

inp_array = input("enter numbers divided by space: ").split()
count = 0
for i in range(1, len(inp_array)):
    count += 1 if int(inp_array[i-1]) < int(inp_array[i]) else 0

print(count)