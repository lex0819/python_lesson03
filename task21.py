# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII
# ":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]

# ordinary
val_set = set()

for dic in dict_list:
    for key, val in dic.items():
        val_set.add(val)

print(val_set)

# unpack dictionary values
val_set1 = set()

for dic in dict_list:
    val_set1.add( *dic.values()) #unpack dict values()

print(val_set1)