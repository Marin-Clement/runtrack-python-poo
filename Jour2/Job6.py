class Order:
    def __init__(self, number, product_list):
        self.__TVA = 20
        self.__order_number = number
        self.__product_list = product_list
        self.__order_status = product_list["status"]
        self.__show_recap()

    def add_product(self, product):
        self.__product_list.append(product)

    def cancel_order(self):
        self.__order_status = "cancel"

    def __calc_total(self):
        total = 0
        for product in self.__product_list["product"]:
            total += self.__product_list["product"][product]
        return total

    def __calculate_ttc(self):
        return round(self.__calc_total() * (1 + self.__TVA / 100), 2)

    def __show_recap(self):
        for product in self.__product_list["product"] : print(product)
        print(f"HT: {self.__calc_total()}")
        print(f"TTC: {self.__calculate_ttc()}")
        print(self.__order_status)


order1 = Order(1, {"product":
                       {"steak": 20,
                        "apple": 1},
                   "status":
                       "in progress"}
               )