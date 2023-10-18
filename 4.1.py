class String:
    def __init__(self, value):
        self.value = value
    @classmethod
    def from_input(cls):
        user_input = input("Введите строку: ")
        return cls(user_input)

    def length(self):
        return len(self.value)

    def is_empty(self):
        return not bool(self.value)

    def count_words(self):
        words = self.value.split()
        return len(words)

    def reverse(self):
        return self.value[::-1]

    def uppercase(self):
        return self.value.upper()


my_string = String.from_input()
print(f"Длина строки: {my_string.length()}")
print(f"Пустая ли строка: {my_string.is_empty()}")
print(f"Количество слов в строке: {my_string.count_words()}")
print(f"Обратная строка: {my_string.reverse()}")
print(f"Строка в верхнем регистре: {my_string.uppercase()}")
