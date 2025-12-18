import datetime
import random

class Product:
    def __init__(self, name, price, amount, expiry):
        self.name = name
        self.price = price
        self.amount = amount  # kg/dona
        self.expiry = expiry

    def __str__(self):
        return f"{self.name} | {self.price} som | {self.amount} kg/dona | Exp: {self.expiry}"


class User:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.basket = {}
        self.history = []

    def add_money(self, amount):
        self.balance += amount


class Supermarket:
    def __init__(self):
        self.products = []
        self.balance = 0

    def add_product(self):
        try:
            name = input("Mahsulot nomi: ")
            existing_product = self.find_product(name)

            if existing_product:
                print(f"{name} mahsuloti allaqachon mavjud.")
                try:
                    add_amount = float(input("Qancha kg/dona qo‘shmoqchisiz? "))
                    if add_amount <= 0:
                        print("Miqdor 0 dan katta bo‘lishi kerak.")
                        return
                    existing_product.amount += add_amount

                    new_price = input("Narxni o‘zgartirmoqchimisiz? (y/n): ").lower()
                    if new_price == "y":
                        price = int(input("Yangi narx: "))
                        existing_product.price = price

                    expiry = input("Yaroqlilik muddatini yangilamoqchimisiz? (y/n): ").lower()
                    if expiry == "y":
                        existing_product.expiry = input("Yangi yaroqlilik muddati: ")

                    print(f"{name} mahsuloti yangilandi.\n")
                except:
                    print("Xatolik.")
            else:
                price = int(input("Narxi: "))
                amount = float(input("Miqdori (kg/dona): "))
                expiry = input("Yaroqlilik muddati: ")
                product = Product(name, price, amount, expiry)
                self.products.append(product)
                print("Yangi mahsulot qo‘shildi.\n")
        except:
            print("Xatolik.")

    def view_products(self):
        print("\n===== MAHSULOTLAR =====")
        if not self.products:
            print("Mahsulotlar yoq.\n")
            return

        i = 1
        for p in self.products:
            print(f"{i}. {p}")
            i += 1
        print("================================\n")

    def find_product(self, name):
        for i in self.products:
            if i.name.lower() == name.lower():
                return i
        return None


def generate_qr(text):
    random.seed(sum(ord(c) for c in text))
    qr = ""
    for i in range(12):
        line = ""
        for j in range(12):
            line += random.choice(["⬜️", " "])
        qr += line + "\n"
    return qr


def print_receipt(user, items, total):
    now = datetime.datetime.now()
    vaqt = now.strftime("%Y-%m-%d %H:%M:%S")

    print("\n========== CHEK ==========")
    print(f"Xaridor: {user.username}")
    print(f"Xarid vaqti: {vaqt}")
    print("--------------------------")

    index = 1
    for name, kg in items.items():
        print(f"{index}.{name} - {kg} kg/dona")
        index += 1
    print("--------------------------")
    print(f"Umumiy summa: {total} som")
    print("Tolangan:", total, "som")
    print("--------------------------")
    qr_text = f"{user.username}-{vaqt}-{total}"
    print(generate_qr(qr_text))

def add_to_basket(user, market):
    market.view_products()
    name = input("Qaysi mahsulot qo‘shilsin? ")
    product = market.find_product(name)
    if not product:
        print("Mahsulot topilmadi.\n")
        return
    if product.amount <= 0:
        print("Bu mahsulot tugagan.\n")
        return
    try:
        amount = float(input("Miqdor (kg/dona): "))
        if amount <= 0:
            print("Miqdor notogri.")
            return
        if amount > product.amount:
            print("Supermarketda yetarli mahsulot yoq.\n")
            return
        user.basket[name] = user.basket.get(name, 0) + amount
        print("Mahsulot savatga qoshildi.")
    except:
        print("Notogri.")

def view_basket(user):
    print("\n===== SAVATCHA =====")
    if not user.basket:
        print("Savatcha bo‘sh.\n")
        return
    i = 1
    for name, amount in user.basket.items():
        print(f"{i}. {name} - {amount} kg/dona")
        i += 1
    print("====================\n")

def edit_basket(user):
    if not user.basket:
        print("Savatcha bosh.")
        return

    view_basket(user)
    name = input("Qaysi mahsulotni tahrirlanadi? ")
    if name not in user.basket:
        print("Mahsulot nomini togri kiriting. \n")
        return
    try:
        new_amount = float(input("Yangi miqdor (kg/dona): "))
        if new_amount <= 0:
            print("0 kirita olmaysiz.")
            return
        user.basket[name] = new_amount
        print("Savatcha yangilandi.")
    except:
        print("Xato miqdor kiritildi")

def remove_basket(user):
    if not user.basket:
        print("Savatcha bosh.\n")
        return
    view_basket(user)
    name = input("Mahsulot nomi: ")
    if name not in user.basket:
        print("Bu mahsulot savatchada yoq.\n")
        return
    del user.basket[name]
    print("Mahsulot savatdan ochirildi.\n")


def checkout(user, market):
    if not user.basket:
        print("Savatcha bosh.\n")
        return

    total = 0
    for name, amount in user.basket.items():
        product = market.find_product(name)
        total += product.price * amount
    print(f"Umumiy summa: {total} som")
    if user.balance < total:
        print("Mablag yetarli emas.\n")
        return
    user.balance -= total
    market.balance += total
    for name, amount in user.basket.items():
        product = market.find_product(name)
        product.amount -= amount
    print("Xarid amalga oshirildi!\n")
    user.history.append({
        "items": user.basket.copy(),
        "total": total,
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    print_receipt(user, user.basket, total)
    user.basket.clear()

def view_history(user):
    if not user.history:
        print("\n Tarix bosh.\n")
        return

    print("=== Tarixlar ===")
    i = 1
    for record in user.history:
        print(f"{i}. Vaqt: {record["time"]} Umumiy summa: {record["total"]} som.")
        for name, kg in record["items"].items():
            print(f" {name}: {kg} kg/dona")
        i += 1
        print("==========================\n")

def view_all_history(users):
    print("=== Xaridlar tarixi ===")
    for user in users:
        if not user.history:
            continue
        print(f"\nXaridor: {user.username}")
        i = 1
        for record in user.history:
            print(f"{i}. Vaqt: {record['time']} | Umumiy summa: {record['total']} som")
            for name, kg in record["items"].items():
                print(f" {name}: {kg} kg/dona")
            print("----------------")
            i += 1

def admin_panel(market, users):
    while True:
        print("\n==== ADMIN PANEL ====")
        print("1. Mahsulot qo‘shish")
        print("2. Mahsulotlar ro‘yxati")
        print("3. Balansni ko‘rish")
        print("4. Tarixni korish")
        print("5. Chiqish")

        cmd = input("Tanlang: ")
        if cmd == "1":
            market.add_product()
        elif cmd == "2":
            market.view_products()
        elif cmd == "3":
            print(f"Supermarket balansi: {market.balance} so'm\n")
        elif cmd == "4":
            view_all_history(users)
        elif cmd == "5":
            return
        else:
            print("Notogri.\n")


def user_panel(user, market):
    while True:
        print(f"\n==== {user.username} ====")
        print("1. Mahsulotlarni ko‘rish")
        print("2. Savatchaga qo‘shish")
        print("3. Savatchani ko‘rish")
        print("4. Xarid qilish")
        print("5. Savatchani tahrirlash")
        print("6. Savatchadan ochirish")
        print("7. Balansni ko‘rish")
        print("8. Balansga pul qo‘shish")
        print("9. Chiqish")

        cmd = input("Tanlang: ")
        if cmd == "1":
            market.view_products()
        elif cmd == "2":
            add_to_basket(user, market)
        elif cmd == "3":
            view_basket(user)
        elif cmd == "4":
            checkout(user, market)
        elif cmd == "5":
            edit_basket(user)
        elif cmd == "6":
            remove_basket(user)
        elif cmd == "7":
            print(f"Sizni balansingiz: {user.balance} som. \n")
        elif cmd == "8":
            try:
                pul = float(input("Qancha pul qoshasiz? "))
                user.add_money(pul)
                print("Balans qoshildi.\n")
            except:
                print("Notogri.\n")
        elif cmd == "9":
            return
        else:
            print("Noto‘g‘ri tanlov!\n")

def run():
    market = Supermarket()

    market.products.append(Product("Olma", 10000, 50, "2025-01-20"))
    market.products.append(Product("Non", 4000, 100, "2024-12-12"))
    market.products.append(Product("Cola", 14000, 40, "2024-12-01"))

    users = [
        User("user1", "1111", 100000),
        User("user2", "2222", 50000)
    ]

    Admin_login = "admin"
    Admin_parol = "1234"

    while True:
        print("\n===== LOGIN =====")
        print("1. Admin")
        print("2. User login")
        print("3. New user")
        print("4. Exit")

        choice = input("Tanlang: ")
        if choice == "1":
            login = input("Admin login: ")
            parol = input("Admin parol: ")
            if login == Admin_login and parol == Admin_parol:
                admin_panel(market, users)
            else:
                print("Admin paroli noto‘g‘ri!\n")
        elif choice == "2":
            login = input("Login: ")
            parol = input("Parol: ")
            user = None
            for i in users:
                if i.username == login and i.password == parol:
                    user = i
                    break
            if user:
                user_panel(user, market)
            else:
                print("User topilmadi!\n")
        elif choice == "3":
            username = input("Yangi login: ")
            password = input("Parol: ")
            users.append(User(username, password))
            print("Yangi user yaratildi!\n")
        elif choice == "4":
            print("LOGIN menyusiga qaytildi.\n")
            continue
        else:
            print("Noto‘g‘ri tanlov!\n")

run()

