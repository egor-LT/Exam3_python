class Product:
    _product_count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product._product_count += 1

    @staticmethod
    def get_product_count():
        return Product._product_count

    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.price}, Total Products: {Product.get_product_count()}"


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def get_info(self):
        return (f"Electronic Product Name: {self.name}, Price: {self.price}, "
                f"Warranty Period: {self.warranty_period} months, Total Products: {Product.get_product_count()}")


class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_info(self):
        return (f"Clothing Product Name: {self.name}, Price: {self.price}, "
                f"Size: {self.size}, Total Products: {Product.get_product_count()}")


# Приклад використання:
# Створення електронних продуктів
electronic1 = ElectronicProduct("Laptop", 1500, 24)
electronic2 = ElectronicProduct("Smartphone", 800, 12)

# Створення продуктів одягу
clothing1 = ClothingProduct("T-Shirt", 20, "M")
clothing2 = ClothingProduct("Jeans", 50, "L")

# Виведення інформації про продукти
print(electronic1.get_info())
print(electronic2.get_info())
print(clothing1.get_info())
print(clothing2.get_info())

# Виведення загальної кількості продуктів
print(f"Total number of products created: {Product.get_product_count()}")
