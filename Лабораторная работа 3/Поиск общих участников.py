def find_common_participants(group1, group2, delimiter=','):
    set1 = set(group1.split(delimiter))
    set2 = set(group2.split(delimiter))
    common_participants = sorted(list(set1 & set2))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(f"Общие участники: {common}")

# Проверка работы функции с разделителем отличным от запятой
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common}")