#1. Feladat: Egyszerű Osztály Definiálása
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_info(self):
        return self.name, self.age

dog1 = Dog("kutya", 5)
dog2 = Dog("rex", 6)
print(*dog1.display_info())
print(*dog2.display_info())

#2. Feladat: Banki Számla Osztály
class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount

    
    def withdraw(self, amount):
        self.balance -= amount
 
    def get_balance(self):
        print(self.balance)

bankfiok1 = BankAccount("a", 5000)
bankfiok1.deposit(1000)
bankfiok1.withdraw(800)
bankfiok1.get_balance()

#3. Feladat: Diák Osztály és Átlag Számítása
class Student():
    def __init__(self, name, grade):
       self.name = name
       self.grade = grade
    def add_grade(self, grade):
        self.grade.append(grade)
    def osztalyzatok(self):
        print(self.grade)
    def get_average(self):
        print(sum(self.grade) / len(self.grade))
diak1 = Student('Sanyi', [2,5,4,2])
diak1.get_average()
diak1.add_grade(3)
diak1.get_average()






