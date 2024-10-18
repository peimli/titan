class Person:
    def __init__(self, name, age, momage):
        self.name = name
        self.age = age
        self.momage = momage

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. My mom give birh to me when she was {self.momage - self.age}"

person1 = Person("Alice", 25, 48)
print(person1.greet()) 