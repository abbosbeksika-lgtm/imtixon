from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def send_sms(self):
        pass


class IPhone(Phone):
    def call(self):
        print("iPhone qo‘ng‘iroq qilmoqda")

    def send_sms(self):
        print("iPhone SMS yuboryapti")

phone = IPhone()
phone.call()
phone.send_sms()

