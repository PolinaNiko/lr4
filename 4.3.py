class Animal:
    def __init__(self, breed, price):
        self.breed = breed
        self.price = price

    def move(self):
        pass


class Fish(Animal):
    def move(self):
        return "Плавает"


class Bird(Animal):
    def move(self):
        return "Летает"


class PetShop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def most_expensive_breed(self):
        if not self.animals:
            return None
        most_expensive = max(self.animals, key=lambda x: x.price)
        return most_expensive.breed

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for animal in self.animals:
                file.write(f"{animal.breed}, {animal.price}\n")


pet_shop = PetShop()

while True:
    breed = input("Введите породу животного (или '0' для выхода): ")
    if breed.lower() == '0':
        break

    price = float(input("Введите стоимость животного: "))

    animal_type = input("Введите тип животного ('рыба' или 'птица'): ").lower()
    if animal_type == 'рыба':
        animal = Fish(breed, price)
    elif animal_type == 'птица':
        animal = Bird(breed, price)
    else:
        print("Неверный тип животного. Повторите ввод!")
        continue

    pet_shop.add_animal(animal)

most_expensive_breed = pet_shop.most_expensive_breed()
print(f"Самая дорогая порода: {most_expensive_breed}")

filename = input("Введите имя файла для сохранения данных: ")
pet_shop.save_to_file(filename)
