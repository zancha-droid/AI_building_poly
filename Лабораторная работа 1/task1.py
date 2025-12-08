numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
summ1 = sum(numbers[0:4])
summ2 = sum(numbers[5:])
total = summ1 + summ2
amount = len(numbers)
missing = round(total / amount, 2)
numbers[4] = missing
print("Измененный список:", numbers)
