"""
statik method

class methodini yozib bering

polimorfizmni chuntirib kod yozib bering

class yozing classni public private protected

class yozing class ichida 4ta abctrak methodi bolsin abctrakdan voris olgan barcha abctrack methodlar aniqlansin
"""

"statik method"
# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
# print(Math.add(5, 3))  # 8
# m = Math()
# print(m.add(10, 2))    # 12


# class Car:
#     moshina = 4
#     @classmethod
#     def number_of_wheels(cls):
#         return cls.moshina
#
# print(Car.number_of_wheels())


"""getter va setter"""
# class Car:
#     def __init__(self, brand):
#         self.__brand = brand
#     def get_brand(self):
#         return self.__brand
#     def set_brand(self, brand):
#         self.__brand = brand
#
# my_car = Car("Daewoo")
# print(my_car.get_brand())  # Toyota
# my_car.set_brand("Chevrolet")
# print(my_car.get_brand())  # Honda


"""ABC"""
# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
#     @abstractmethod
#     def fuel(self):
#         pass
#     @abstractmethod
#     def move(self):
#         pass
#
# class Car(Vehicle):
#     def start(self):
#         print("Car started")
#     def stop(self):
#         print("Car stopped")
#     def fuel(self):
#         print("Car is fueled")
#     def move(self):
#         print("Car is moving")
#
# my_car = Car()
# my_car.start()
# my_car.move()

