class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int, species: str):
        """
        Конструктор базового класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного.
        :param species: Вид животного.
        """
        self.name = name
        self.age = age
        self.species = species

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"{self.name} ({self.species}), возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        """
        return f"Animal(name={self.name}, age={self.age}, species={self.species})"

    def make_sound(self) -> str:
        """
        Метод, возвращающий звук, издаваемый животным.
        """
        return "Беззвучно"

    def stroke(self):
        return f'{self.name} очень доволен'

class Dog(Animal):
    """
    Дочерний класс для собак.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age, species="Собака")
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"{self.name} ({self.breed}), возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def make_sound(self) -> str:
        """
        Перегрузка метода make_sound для собаки. Нужна для индивидуализации звука, издаваемого конкретным животным.
        """
        return "Гав-гав!"

    def returner(self, item: str) -> str:
        """
        Метод, который описывает, как собака приносит предмет.

        :param item: Предмет, который нужно принести.
        :return: Строка с описанием действия.
        """
        return f"{self.name} приносит {item}."


class Cat(Animal):
    """
    Дочерний класс для кошек.
    """

    def __init__(self, name: str, age: int, color: str):
        """
        Конструктор класса Cat.

        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age, species="Кошка")
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"{self.name} ({self.color} кошка), возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        """
        return f"Cat(name={self.name}, age={self.age}, color={self.color})"

    def make_sound(self) -> str:
        """
        Перегрузка метода make_sound для кошки. Нужна для индивидуализации звука, издаваемого конкретным животным.
        """
        return "Мяу!"

    def purr(self) -> str:
        """
        Метод, который описывает, как кошка мурлычет.

        :return: Строка с описанием действия.
        """
        return f"{self.name} мурлычет."


if __name__ == "__main__":
    # Write your solution here
    pass
