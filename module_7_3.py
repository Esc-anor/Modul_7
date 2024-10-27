class WordsFinder:  # создание класса WordsFinder
    def __init__(self, *file_txt):  # метод __init__ принимающий множество названий текстовых файлов
        self.file_names = file_txt  # создание атрибута класса file_names

    def get_all_words(self):  # подготовительный метод get_all_word, который возвращает словарь all_words
        all_words = {}  # создание пустого словаря all_words
        for i in self.file_names:  # цикл перебора строк файла с открытием оператором with для чтения
            with open(i, 'r', encoding='utf-8') as file:  # в кодировке utf-8
                file = file.read().lower()  # перевод в нижний регистр стоки переменной file
                # цикл перебора и поиска в тексте указанных в [] знаков
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file = file.replace(j, '')  # замена знаков пунктуации на пустое значение в строке
                words = file.split()  # разбор строки на элементы списка методом split()
                all_words[i] = words  # присвоение словарю all_words ключу (i) значения списка слов (words)
        return all_words  # возврат словаря метода get_all_words()

    """ find(self, word) - метод, где word - искомое слово. 
    Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла."""

    def find(self, word):
        result = {}  # создание пустого словаря result
        # цикл перебора в файле (i) слов (word_) из словаря all_words из метода get_all_words
        for i, word_ in self.get_all_words().items():
            # цикл перебора (поиска) номера (j) слова (wd) из списка word_ начиная с 1
            for j, wd in enumerate(word_, 1):
                # условие сравнения слова (wd) и приведенного к нижнему регистру принятого
                # (искомого) слова (word)
                if wd == word.lower():
                    result[i] = j  # присвоение переменной result[i] найденного номера
                    break  # выход из условия при нахождении первого тождества
        return result  # возврат метода find()

    """count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, 
    значение - количество слова word в списке слов этого файла."""

    def count(self, word):
        result_ = {}  # объявление пустого словаря result_
        # цикл перебора в файле (i) слов (word_) из словаря all_words из метода get_all_words
        for i, word_ in self.get_all_words().items():
            # присвоение словарю result_[i] количества совпадений word_ в приведенном к
            # нижнему регистру искомого (принятого) слова word
            result_[i] = word_.count(word.lower())
        return result_  # возврат метода count()


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))
