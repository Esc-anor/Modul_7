""" Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name -
    название файла для записи, strings - список строк для записи."""


def custom_write(file_name, strings):
    strings_positions = {}  # объявление словаря strings_positions
    # открытие файла file_name для записи с использованием кодировки UTF-8
    file = open(file_name, 'w', encoding='utf-8')
    # цикл определения номера строки в индексированном списке strings (enumerate(strings))
    for i, string in enumerate(strings, 1):
        # присвоение значений индексу строки (i), номеру байта (file.tell()) начала строки
        # (для номера байта конца строки эта строка кода прописывается после записи в файл
        # (закоментировано)) ключа строки в словаре strings_positions
        strings_positions[i, file.tell()] = string

        file.write(string + '\n')  # запись строки (string) в файл
    file.close()  # закрытие file
    return strings_positions  # Возвращение словаря strings_positions,
    # где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка.
    # Для получения номера байта начала строки используйте метод tell() перед записью.


# исходные данные
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
# вывод на консоль
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
