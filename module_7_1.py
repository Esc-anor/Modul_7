class Product:  # Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables')
    def __init__(self, name: str, weight: float, category: str):
        self.name = name  # Атрибут name - название продукта (строка).
        self.weight = weight  # Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.category = category  # Атрибут category - категория товара (строка).

    def __str__(self):
        """ Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
            Все данные в строке разделены запятой с пробелами."""
        prods_str = str(f"{self.name}, {self.weight}, {self.category}")
        return prods_str


class Shop:  # Объекты класса Shop будут создаваться следующим образом - Shop()
    def __init__(self):
        self.__file_name = open('products.txt', 'a')  # Инкапсулированный атрибут __file_name = 'products.txt'.
        self.__file_name.close()

    def get_products(self):
        """ Метод get_products(self), который считывает всю информацию из файла __file_name,
            закрывает его и возвращает единую строку со всеми товарами из файла __file_name."""
        get_file = open('products.txt', 'r')  # обращение к чтению файла products.txt (self.__file_name)
        name_prod = get_file.read()
        get_file.close()
        return name_prod  # возвращение работы метода self.get_products()

    def add(self, *products):
        """ Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
            Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
            Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'."""
        for product in products:  # цикл перебора наименований product в products
            # условие проверки когда строки product нет в списке products.txt
            if str(product) not in self.get_products():
                file = open('products.txt', 'a+')
                file.write(f'{str(product)}\n')  # добавление отсутствующего product в файл products.txt
                file.close()
            # когда запись product есть в файле products.txt
            else:
                print(f'Продукт {product} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
