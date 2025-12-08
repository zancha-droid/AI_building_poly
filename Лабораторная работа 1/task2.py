# TODO Найдите количество книг, которое можно разместить на дискете
volume_mb = 1.44
pages = 100
rows = 50
symb = 25
symb_volume = 4

# Перевод объема дискеты в байты:
volume_kb = 1024 * volume_mb
volume_b = 1024 * volume_kb

total_symb = symb * rows * pages # Подсчет символов
demanded_volume = total_symb * symb_volume # Объем всей книги в байтах
books = int(volume_b // demanded_volume)

print("Количество книг, помещающихся на дискету:", books)
