class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(f"The price of {self.model} ({self.year}) is ₹{self.price}")

car1 = Car("susuki alto", 2000, 420000)
car2 = Car("audi  r8", 2015, 1500000)

car1.cost()
car2.cost()
