# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
def find_common_participants(group1, group2, delimiter=","):
    """
    Находит общих участников двух групп.

    :param group1: Строка с фамилиями участников первой группы.
    :param group2: Строка с фамилиями участников второй группы.
    :param delimiter: Разделитель между фамилиями в строках (по умолчанию запятая).
    :return: Отсортированный список общих участников.
    """
    # Разделяем строки на списки фамилий
    group1_list = set(group1.split(delimiter))
    group2_list = set(group2.split(delimiter))

    # Находим пересечение множеств
    common_participants = sorted(group1_list & group2_list)

    return common_participants

# Проверяем работу функции с разделителем "|"
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print("Общие участники:", common)
