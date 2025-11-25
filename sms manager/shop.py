class Product:
    def __init__(self, title, price, year):
        self.title = title
        self.price = price
        self.year = year
        self.type = ''


class Shop:
    def __init__(self, title, phone):
        self.title = title
        self.phone = phone
        self.baza = []

    def add_water(self):
        title = input("Title: ")
        price = input("Price: ")
        year = input("Year: ")
        p1 = Product(title, price, year)
        p1.type = 'water'
        self.baza.append(p1)

    def add_food(self):
        title = input("Title: ")
        price = input("Price: ")
        year = input("Year: ")
        p1 = Product(title, price, year)
        p1.type = 'food'
        self.baza.append(p1)

    def view_all(self):
        i = 1
        for item in self.baza:
            print(f'{i}. title: {item.title}, price: {item.price}, year: {item.year} type: {item.type}')
            i += 1

    def view_water(self):
        for item in self.baza:
            if item.type == "water":
                print(f'title: {item.title}, price: {item.price}, year: {item.year}')

    def view_food(self):
        for item in self.baza:
            if item.type == "food":
                print(f'title: {item.title}, price: {item.price}, year: {item.year}')

    def delete_product(self):
        self.view_all()
        index = int(input("Qaysi mahsulotni ochirmoqchisiz? index: "))
        if 0 > index or index >= len(self.baza):
            print("Notogri index.")
            return

        self.baza.pop(index)
        print("Mahsulot ochirildi.")

    def edit_product(self):
        self.view_all()
        index = int(input("Qaysi mahsulotni tahrirlamoqchisiz? index: "))

        if 0 > index or index >= len(self.baza):
            print("Notogri index.")
            return
        item = self.baza[index]
        print("Nimasini o‘zgartirasiz?")
        print("1. title\n2. price\n3. year\n4. type\n : ")
        n = input("Tanlang: ")
        if n == "1":
            item.title = input("Yangi title: ")
        elif n == "2":
            item.price = input("Yangi price: ")
        elif n == "3":
            item.year = input("Yangi year: ")
        elif n == "4":
            item.type = input("Yangi type (water/food): ")
        else:
            print("Noto‘g‘ri tanlov.")

shop1 = Shop('shop1', 1234567)

def shop_manager(shop:Shop):
    while True:
        kod = input(
            " 1. add water \n 2. add food \n 3. view all \n 4. view water \n 5. view food \n 6. delete product \n 7. edit product \n 8. break \n : "
        )

        if kod == "1":
            shop.add_water()
        elif kod == "2":
            shop.add_food()
        elif kod == "3":
            shop.view_all()
        elif kod == "4":
            shop.view_water()
        elif kod == "5":
            shop.view_food()
        elif kod == "6":
            shop.delete_product()
        elif kod == "7":
            shop.edit_product()
        else:
            print("Dastur tugatildi.")
            break

shop_manager(shop1)
