# TODO Найдите количество книг, которое можно разместить на дискете


# Данные задачи
disk_size_mb = 1.44  # Объём дискеты в Мб
pages = 100  # Количество страниц в книге
lines_per_page = 50  # Число строк на странице
characters_per_line = 25  # Количество символов в строке
bytes_per_character = 4  # Количество байт на один символ

# Константа: 1 Мб = 1024 * 1024 байт
MB_TO_BYTES = 1024 * 1024

# Переводим объём дискеты в байты
disk_size_bytes = disk_size_mb * MB_TO_BYTES

# Рассчитываем общий объём данных одной книги в байтах
book_size_bytes = pages * lines_per_page * characters_per_line * bytes_per_character

# Вычисляем, сколько книг поместится на дискету
number_of_books = int(disk_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", number_of_books)