class Customer:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("customer name ", self.name)

class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
    def show(self):
        print("Shop name, ", self.shop_name)
        

shop1 = Shop("BooK WoRLD")

customer1 = Customer("Aarush")  
shop1.show()
customer1.show()
test = Shop("hello")
print(test)
        