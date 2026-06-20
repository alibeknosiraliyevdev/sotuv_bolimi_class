from product import Product
from openpyxl import load_workbook
import getpass

print("Do'kon bo'limi".center(135))
while True:
    print("\n===== MENU =====")
    print("1. Add Product")
    print("2. Sell Product")
    print("3. Report")
    print("0. Exit")

    menu = input("Tanlang: ")

    if menu == "1":
        family = input("Mahsulot oilasi: ")
        name = input("Mahsulot nomi: ")
        quantity = int(input("Miqdori: "))
        buy_price = int(input("Sotib olish narxi: "))
        sell_price = int(input("Sotish narxi: "))
        unit = input("Birligi: ")

        product = Product(family,name,quantity,buy_price,sell_price,0,unit)
        product.add_product()

    elif menu == "2":
        family = input("Mahsulot oilasi: ")
        name = input("Mahsulot nomi: ")
        quantity = int(input("Nechta sotildi: "))

        product = Product(family,name,quantity,0,0,0,"")
        product.sell_product()
    elif menu == "3":
        login=input("Login: ")
        parol=getpass.getpass("Parol: ")
        if login == '1' and parol == '1':    
            while True:
                print("\n===== REPORT =====")
                print("1. Add Product Report")
                print("2. Sell Product Report")
                print("3. Database")
                print("0. Chiqish")
                menu_add=input("Tanlang: ")
                if menu_add == '3':
                    print(Product.get_all_products())
                elif menu_add == '0':
                    break
    elif menu == "0":
        break

    else:
        print("Noto'g'ri tanlov!")


