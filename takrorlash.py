"""1-savol"""
from idlelib.debugobj import myrepr

# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def drive(self):
#         print(f'{self.brand} car is driving')
#
# drive = Car("car")
# drive.drive()

"""2-savol"""
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         '''__init__ bu konstruktor'''

"""3-savol"""
# class Car:
#         wheels = 4
#
#         @classmethod
#         def number_of_wheels(cls):
#             return cls.wheels

"""4-savol"""
# class Vehiles:
#     def __init__(self, brand):
#         self.brand = brand
#     def move(self):
#         print("Moving")
# class Car(Vehiles):
#     pass
#
# my_car = Car("Car")
# my_car.move()

"""5-savol"""
# class Dog:
#     def sound(self):
#         print("Woof")
# class Cat:
#     def sound(self):
#         print("Meow")
# def make_sound(animal):
#     animal.sound()
#
# make_sound(Dog())  # Woof
# make_sound(Cat())  # Meow

"""6-savol"""
# class Car:
#     def __init__(self, brand):
#         self.__brand = brand  # private atribut
#     def get_brand(self):
#         return self.__brand

"""7-savol"""
# class Car:
#     def __init__(self, brand):
#         self.brand = brand  # public atribut
# my_car = Car("Toyota")
# print(my_car.brand)  # Toyota
# my_car.brand = "Honda"  # o‘zgartirish mumkin
#
#
# class Car:
#     def __init__(self, brand):
#         self._brand = brand  # protected atribut
# my_car = Car("Toyota")
# print(my_car._brand)  # ishlaydi, lekin tavsiya qilinmaydi
#
#
# class Car:
#     def __init__(self, brand):
#         self.__brand = brand  # private atribut
#
# my_car = Car("Toyota")
# # print(my_car.__brand)  # Xato: AttributeError
# print(my_car._Car__brand)  # Toyota (name mangling orqali ishlaydi)


"""8-savol"""
# class Car:
#     def __init__(self, brand):
#         self.__brand = brand
#     def get_brand(self):
#         return self.__brand
#     def set_brand(self, brand):
#         self.__brand = brand

"""9-savol"""
# class Car:
#     def __init__(self, brand):
#         self.__brand = brand
#     @property
#     def brand(self):
#         return self.__brand
#     @brand.setter
#     def brand(self, value):
#         self.__brand = value
#
# my_car = Car("Toyota")
# my_car.brand = "Honda"  # setter ishladi
# print(my_car.brand)     # getter ishladi

"""10-savol"""
# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         pass

"""11-savol"""
# class Vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         pass
# class Car(Vehicle):
#     def move(self):
#         print("Car is moving")
#
# my_car = Car()
# my_car.move()



'''1-savol: classni chuntirib bering'''
'''2-savol: konstruktorlarni chuntirib bering'''
'''3-savol: class methodlarini chuntirib bering'''
'''4-savol: vorislikni chuntirib bering'''
'''5-savol: polimofrizmni chuntirib bering'''
'''6-savol: incapsulation nima'''
'''7-savol: acsist fayllarni chunirib bering'''
'''8-savol: getter setterni chuntirb bering'''
'''9-savol: propertini chuntirib bering'''
'''10-savol: abstruck classni chuntirib bering'''
'''11-savol: abctruck methodini chuntirib bering'''
