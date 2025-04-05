class person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: ₹{self.salary}")

person1 = person("mia", 50, 5000)
person2 = person("kia", 62, 8000)

person1.display()
person2.display()
