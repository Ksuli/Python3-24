class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int, weight: float):
        """
        Конструктор базового класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного.
        :param weight: Вес животного.
        """
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"Animal(name={self.name}, age={self.age}, weight={self.weight})"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        """
        return f"Animal(name={self.name}, age={self.age}, weight={self.weight})"

    def make_sound(self) -> str:
        """
        Возвращает звук, который издает животное.
        """
        return "Some generic animal sound"

    def eat(self, food: str) -> str:
        """
        Метод, описывающий процесс питания животного.

        :param food: Название еды.
        :return: Строка с описанием процесса питания.
        """
        return f"{self.name} is eating {food}."


class Dog(Animal):
    """
    Дочерний класс Dog, наследуемый от Animal.
    """

    def __init__(self, name: str, age: int, weight: float, breed: str):
        """
        Конструктор класса Dog.

        :param breed: Порода собаки.
        """
        super().__init__(name, age, weight)
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Dog.
        """
        return f"Dog(name={self.name}, age={self.age}, weight={self.weight}, breed={self.breed})"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта Dog.
        """
        return f"Dog(name={self.name}, age={self.age}, weight={self.weight}, breed={self.breed})"

    def make_sound(self) -> str:
        """
        Перегрузка метода make_sound для собаки.
        """
        return "Woof!"

    def fetch(self, item: str) -> str:
        """
        Метод, описывающий процесс принесения предмета собакой.

        :param item: Название предмета.
        :return: Строка с описанием процесса.
        """
        return f"{self.name} is fetching the {item}."


class Cat(Animal):
    """
    Дочерний класс Cat, наследуемый от Animal.
    """

    def __init__(self, name: str, age: int, weight: float, color: str):
        """
        Конструктор класса Cat.

        :param color: Цвет кошки.
        """
        super().__init__(name, age, weight)
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Cat.
        """
        return f"Cat(name={self.name}, age={self.age}, weight={self.weight}, color={self.color})"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта Cat.
        """
        return f"Cat(name={self.name}, age={self.age}, weight={self.weight}, color={self.color})"

    def make_sound(self) -> str:
        """
        Перегрузка метода make_sound для кошки.
        """
        return "Meow!"

    def purr(self) -> str:
        """
        Метод, описывающий процесс мурлыканья кошки.

        :return: Строка с описанием процесса.
        """
        return f"{self.name} is purring."


if __name__ == "__main__":
    # Пример использования классов
    dog = Dog("Buddy", 3, 15.5, "Golden Retriever")
    cat = Cat("Whiskers", 5, 4.2, "Black")

    print(dog)  # Dog(name=Buddy, age=3, weight=15.5, breed=Golden Retriever)
    print(cat)  # Cat(name=Whiskers, age=5, weight=4.2, color=Black)

    print(dog.make_sound())  # Woof!
    print(cat.make_sound())  # Meow!

    print(dog.fetch("ball"))  # Buddy is fetching the ball.
    print(cat.purr())  # Whiskers is purring.