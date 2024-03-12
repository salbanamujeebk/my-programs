class Shop:
    def __init__(self, id, quantityitem, priceitem):
        self.id = id
        self.quantityitem = quantityitem
        self.priceitem = priceitem

    def gold(self):
        total = self.priceitem * self.quantityitem
        discount = total * 0.2
        finalprice = total - discount

        print(f"Price of an item: {total}")
        print(f"Discount for gold customer: {discount}")
        print(f"After discount: {finalprice}")

    def silver(self):
        total = self.priceitem * self.quantityitem
        discount = total * 0.1
        finalprice = total - discount

        print(f"Price of an item: {total}")
        print(f"Discount for silver customer: {discount}")
        print(f"After discount: {finalprice}")

    def exit(self):
        print("Thank you for using the Billing System. Goodbye!")
        exit()

while True:
    id = input("Enter your ID: ")
    quantityitem = int(input("Enter quantity item: "))
    priceitem = float(input("Enter price item: "))

    print("Welcome to the Billing System")
    print("1: Gold\n"
          "2: Silver\n"
          "3: Exit\n")
    choice = input("Choose your customer type: ")

    if choice == '3':
        print("Thank you for using the Billing System. Goodbye!")
        break
    elif choice == '1':
        shop = Shop(id, quantityitem, priceitem)
        shop.gold()
        while True:
            print("1: Yes\n"
                  "2: No\n")
            cont = input("Do you want to continue? : ")
            if cont == '2':
                shop.exit()
            elif cont == '1':
                break
    elif choice == '2':
        shop = Shop(id, quantityitem, priceitem)
        shop.silver()
        while True:
            print("1: Yes\n"
                  "2: No\n")
            cont = input("Do you want to continue? : ")
            if cont == '2':
                shop.exit()
            elif cont == '1':
                break
    else:
        print("Invalid choice. Please enter a valid option.")
