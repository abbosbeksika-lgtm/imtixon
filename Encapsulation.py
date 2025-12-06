"""public, private, protect 3xil methodlar bor"""
from avtopark import users

'''PUBLIC'''
"""public: Tashqi koddan erkin kirish mumkin. Hech qanday cheklov yo‘q, ya’ni class ichida ham, tashqarida ham ishlatilishi mumkin. 
Python’da default qiymat sifatida public atributlar bo‘ladi."""

'''PRIVATE'''
"""private: Faqat class ichida ishlatilishi mumkin. Tashqaridan to‘g‘ridan-to‘g‘ri kirish mumkin emas.
Python’da __ (double underscore) ishlatiladi."""

'''PROTECTED'''
"""protected: Class ichida va meros (inheritance) olgan subclasslarda ishlatiladi, lekin tashqi koddan kirish tavsiya etilmaydi.
Python’da _ (bitta underscore) ishlatiladi."""

'''ENCAPSULATION'''
"""Encapsulationning maqsadi – ob’yekt ichidagi ma’lumotlarni (atributlar) himoya qilish va ularga faqat kerakli usullar orqali kirishni ta’minlash.
Private, protected, public esa aynan shu himoyani qanday darajada amalga oshirishni belgilaydi
Private (__) → to‘liq himoyalangan, faqat class ichida ishlatiladi.
Protected (_) → qisman himoyalangan, class va subclass ichida ishlatiladi
Public → hech qanday himoya yo‘q, har joydan erkin kirish mumkin.
Shu tarzda, getter va setter metodlar yordamida private atributlarga tashqaridan xavfsiz kirish ta’minlanadi,
bu esa encapsulationning amaliy ko‘rinishi hisoblanadi."""

'''| Atribut         | Kirish darajasi | Encapsulationdagi roli                                 |
| --------------- | --------------- | ------------------------------------------------------ |
| hisob_raqami    | private         | Tashqaridan ko‘rinmasligi, xavfsizlik                  |
| balans          | private         | Faqat deposit/withdraw metodlari orqali o‘zgartiriladi |
| bank_nomi       | public          | Har kim ko‘ra oladi, xavfsizlik talab qilinmaydi       |
| maxsus_chegirma | protected       | Faqat bank va filiallar ko‘ra oladi                    |
'''

"""Private atributlar → encapsulation orqali himoyalangan
Public atribut → erkin ko‘rinadi
Getter/setter metodlari → ma’lumotlarni xavfsiz boshqarish imkonini beradi"""

'''          +---------------------------+
          |       BankAccount         |
          +---------------------------+
          | - __account_number        |  <- private
          | - __balance               |  <- private
          | + bank_name               |  <- public
          +---------------------------+
          | + deposit(amount)         |  <- method
          | + withdraw(amount)        |  <- method
          | + get_balance()           |  <- method
          +---------------------------+

Arrows:
- Private attributes (__account_number, __balance) ---> accessed ONLY via deposit, withdraw, get_balance
- Public attribute (bank_name) -----------------------> accessed directly
'''

# class Student:
#     def __init__(self, name, phone, seria_id, group_id):
#         self.name = name
#         self.phone = phone
#         self.__seria_id = seria_id
#         self.group_id = group_id
#
#     @property
#     def get_seria(self):
#         return self.__seria_id
#
#     @get_seria.setter
#     def set_seria(self, new_seria):
#         if type(new_seria)==int:
#             self.__seria_id = new_seria
#         else:
#             print("Son kiriting")
#
# g1 = Student("Abu", "9821321", 2134, 1324)
# print(g1.get_seria)
# g1.set_seria=13243
# print(g1.get_seria)

class User:
    def __init__(self, name, phone, seria, age):
        self.name = name
        self.phone = phone
        self.seria = seria
        self.age = age
        self.is_active = True


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


class Park:
    def __init__(self, title):
        self.title = title
        self.users = []
        self.cars = []
        self.orders = []

    def add_car(self):
        model = input("Mashina nomi: ")
        brand = int(input("Brendi: "))
        year = int(input("Yili: "))
        seria = int(input("Seria: "))
        car = Car(model, brand, year, seria)
        self.cars.append(car)
        print("Mashina qoshildi.\n")
    print()

    def view_cars(self):
        i = 1
        for car in self.cars:
            if car in self.orders:
                holat = "ijarada"
            else:
                holat = "Bosh"
            print(f"{i}. {car.model}, {car.brand}, {car.year}, {car.seria}, {holat}")
            i += 1
        print()

    def add_user(self):
        name = input("Ism kiriting: ")
        phone = input("Tel kiriting: ")
        age = int(input("Yoshingizni kiriting: "))
        seria = int(input("Seria kiriting: "))
        user = User(name, phone, age, seria)
        self.users.append(user)
        print("Yangi foydalanuvchi hush kelibsiz.")
    print()

    # def view_users(self):
    #     if :

def park_manager(p:Park):
    while True:
        kod = input("1. Mashina qo'shish \n 2. Mashinalarni korish \n 3. User qoshish \n : ")
        if kod == '1':
            p.add_car()
        elif kod == '2':
            p.view_cars()
        elif kod == '3':
            p.add_user()
        else:
            break

park = Park("Bro")
park_manager(park)