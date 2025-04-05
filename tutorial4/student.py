class student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def dataprint(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}")

student1 = student("ronaldo", 7)
student2 = student("neymar", 10)

student1.dataprint()
student2.dataprint()
