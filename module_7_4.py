import os  # импорт модуля (библиотеки) os для работы с файлами и директориями ОС
import time  # импорт модуля (библиотеки) time для работы с данными времени

directory = os.getcwd()  # присвоение переменной directory путь до текущего каталога
# присвоение переменной directory путь до текущего каталога в папке проекта
# directory = '.'
# обзор всего каталога directory организован через несколько циклов в цикле# for i in os.walk(testdir)
for root, dirs, files in os.walk(directory):
    for file in files:  # цикл вывода расположения файлов в directory
        # присвоение переменной filepath полного пути к итерируемому файлу действием функции join
        filepath = os.path.join(root, file)
        # присвоение переменной filetime
        filetime = os.path.getmtime(filepath)
        # форматирование filetime в удобоваримое значение времени
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # присвоение filesize значения размера файла
        filesize = os.path.getsize(filepath)
        # присвоение parent_dir пути родительской директории
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
