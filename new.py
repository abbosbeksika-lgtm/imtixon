class User:
    def __init__(self, name, phone, seria, age):
        self.username = name
        self.phone = phone
        self.seria = seria
        self.age = age
        self.password = 0000
        self.is_active = True
        self.is_admin = False
        self.rent = []

    def edit(self):
        field = input(' 1:username\n 2:phone \n 3:age: \n 4:password :')
        new_field = input('new : ')
        if field == '1':
            self.username = new_field
        elif field == '2':
            self.phone = new_field
        elif field == '3':
            self.age = new_field
        elif field == '4':
            self.password = int(new_field)

u1 = User('user',12345,12345,54)

class Car:
    def __init__(self, model, brand, year, seria):
        self.model = model
        self.brand = brand
        self.year = year
        self.seria = seria
        self.is_active = True

class Order:
    def __init__(self, user_id, car_id, date_start, date_end):
        self.user_id = user_id
        self.car_id = car_id
        self.date_start = date_start
        self.date_end = date_end
        self.is_active = True

class Park:
    def __init__(self, title):
        self.title = title
        self.users = []
        self.cars = []
        self.orders = []

    def public_cars(self):
        count = 1
        for item in self.cars:
            if item.is_active:
                print(f'{count}. model: {item.model} brand:{item.brand} year:{item.year}')
                count += 1

    def add_user(self):
        name =input('username:')
        phone =input('phone:')
        seria =input('seria:')
        age =input('age:')
        u = User(name,phone,seria,age)
        self.users.append(u)

    def add_admin(self):
        print("Admin qoshish")
        name = input("username: ")
        phone = input("phone: ")
        seria = input("seria: ")
        age = input("age: ")
        u = User(name, phone, seria, age)
        u.is_admin = True
        self.users.append(u)
        print("Yangi admin qoshildi.\n")

    def view_users(self):
        count = 0
        for item in self.users:
            count+=1
            print(f"{count}. username: {item.username} phone:{item.phone} seria:{item.seria}")

    def add_car(self):
        model = input('model:')
        brand = input('brand:')
        seria = input('seria:')
        year = input('year:')
        u = Car(model, brand, seria, year)
        self.cars.append(u)

    def view_cars(self):
        count = 0
        for item in self.cars:
            count += 1
            print(f"{count}. username: {item.model} phone:{item.brand} seria:{item.seria}")

    def login(self):
        urinish = 3
        while urinish > 0:
            name = input("username: ")
            password = int(input("password: "))
            for item in self.users:
                if item.username == name and item.password == password:
                    return item, True
            urinish -= 1
            print(f'Xato. qolgna urinishlar: {urinish}')
        print("Dastur tugatildi.")
        exit()

    def rent(self, user: User):
        self.public_cars()
        car = input("Qaysi mashinani ijaraga olasiz? (nomini yozing.): ")

        car = None
        for i in self.cars:
            if i.model == car and i.is_active:
                car = i
                break
        if not car:
            print("Bunday mashina yoq.")
            return
        days = input("Nech kunga ijaraga olasiz?: ")
        order = Order(user, car, days)
        user.rent.append(order)
        self.orders.append(order)
        car.is_active = False
        print(f'{car.model} mashinasini {days} kunga ijaraga oldindi.\n')

    def return_car(self, user: User):
        if not user.rent:
            print("Sizda ijarada mashina yoq.")
            return

        print("sizdagi mashinalar")
        for i, order in user.rent:
            print(f'{i+1}. {order.car.model} {order.car.brand}')

        index = int(input("Qaysi mashinani qaytarasiz?: ")) - 1
        order = user.rent.pop(index)
        order.car.is_active = True
        order.is_active = False
        print("Mashina qaytarildi.\n")

park = Park('park1')

park.cars.append(Car("Gentra", "Chevrolet", 2021, 12345))
park.cars.append(Car("Malibu", "Chevrolet", 2022, 123456))
park.cars.append(Car("XM", "BMW", 2023, 123457))

admin = User('admin', 123456, 1234, 12)
admin.is_admin = True
park.users.append(admin)
park.users.append(u1)

def taxi_manager(p:Park,u:User):
    while True:
        kod = input(" 1.edit \n 2. public cars \n 3. Ijaraga olish \n 4. mashinani qaytarish \n 5. break \n :")
        if kod=='1':
            u.edit()
        elif kod=='2':
            p.public_cars()
        elif kod == '3':
            p.rent(u)
        elif kod == '4':
            p.return_car(u)
        else:
            break


def admin_manager(p:Park,u:User):
    while True:
        kod = input(" 1. add user\n 2. add car \n 3. view users \n 4. views cars \n 5. break : ")
        if kod=='1':
            p.add_user()
        elif kod=='2':
            p.add_car()
        elif kod=='3':
            p.view_users()
        elif kod=='4':
            p.view_cars()
        else:
            break

def park_manager(p: Park):
    item = p.login()
    if item[1]:
        if item[0].is_admin:
            admin_manager(p,item[0])
        else:
            taxi_manager(p,item[0])
    else:
        print("xato")

park_manager(park)