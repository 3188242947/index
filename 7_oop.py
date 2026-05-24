class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "动物叫声"

    def info(self):
        return f"{self.name}, {self.age}岁"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "汪汪汪!"

    def fetch(self):
        return f"{self.name}正在捡球"


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "喵喵喵!"

    def climb(self):
        return f"{self.name}正在爬树"


class PetShop:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        return f"{animal.name}已添加到{self.name}"

    def show_all_animals(self):
        print(f"\n{self.name}的所有动物:")
        for animal in self.animals:
            print(f"  - {animal.info()}, 叫声: {animal.speak()}")


dog = Dog("旺财", 3, "金毛")
cat = Cat("咪咪", 2, "白色")

print(dog.info())
print(dog.speak())
print(dog.fetch())

print()

print(cat.info())
print(cat.speak())
print(cat.climb())

shop = PetShop("爱心宠物店")
shop.add_animal(dog)
shop.add_animal(cat)
shop.show_all_animals()