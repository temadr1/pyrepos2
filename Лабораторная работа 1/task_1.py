import doctest


class Refrigerator:
    def __init__(self, name: str, height: (int, float), free_capacity: int):
        """
                Создание и подготовка к работе объекта "Холодильник"

                :param name: Название марки производителя холодильника
                :param height: Высота холодильника
                :param free_capacity: Количество свободного места в холодильнике

                Примеры:
                >>> fridge = Refrigerator("samsung", 100, 200)  # инициализация экземпляра класса
                """
        self.name = name
        if not isinstance(height, (int, float)):
            raise TypeError("Некорректное значение для высоты")
        if height <= 0:
            raise ValueError("Высота холодильника должна быть больше 0")
        self.height = height
        if not isinstance(free_capacity, int):
            raise TypeError("Некорректное значение свободного места")
        if free_capacity < 0:
            raise ValueError("Количество свободного места не должно быть меньше 0")
        self.free_capacity = free_capacity

    def add_item(self, item_size: int) -> None:
        """
        Функция, добавляющая предмет в холодильник

        :param item_size: Количество места, занимаемое добавляемым предметом

        :raise ValueError: Возвращается ошибка при попытке добавления предмета, занимающего больше места, чем есть в хол
        одильнике

         Примеры:
        >>> fridge = Refrigerator("samsung", 100, 200)
        >>> fridge.add_item(50)
        """
        if not isinstance(item_size, int):
            raise TypeError("Некорректное значение места, занимаемого предметом")
        if item_size < 0:
            raise ValueError("Количество места, занимаемого предметом, не должно быть меньше 0")
        ...

    def is_fridge_empty(self) -> bool:
        """Функция, проверяющая является ли холодильник пустым

        :return: Является ли холодильник пустым

        Примеры:
        >>> fridge = Refrigerator("samsung", 100, 200)
        >>> fridge.is_fridge_empty()
        """
        ...


class Door:
    def __init__(self, is_electric: bool, material: str, is_open: bool):
        """
                Создание и подготовка к работе объекта "Дверь"

                :param is_electric: Является ли дверь электрической
                :param material: Материал из которого изготовлена дверь
                :param is_open: Открыта ли дверь

                Примеры:
                >>> door_1 = Door(True, 'wood', True)  # инициализация экземпляра класса
                """
        if not isinstance(is_electric, bool):
            raise TypeError("Дверь может быть либо электрической либо нет")
        self.is_electric = is_electric
        if not isinstance(material, str):
            raise TypeError("Некорректное значение материала двери")
        self.material = material
        if not isinstance(is_open, bool):
            raise TypeError("Дверь может быть либо открытой либо закрытой")
        self.is_open = is_open

    def open_door(self) -> None:
        """
        Функция, открывающая дверь

        :raise AlreadyOpenedError: Возвращается ошибка, если дверь уже открыта.

         Примеры:
        >>> door_1 = Door(True, 'steel', False)
        >>> door_1.open_door()
        """
        ...

    def close_door(self) -> None:
        """
        Функция, закрывающая дверь

        :raise AlreadyClosedError: Возвращается ошибка, если дверь уже закрыта.

         Примеры:
        >>> door_1 = Door(True, 'steel', False)
        >>> door_1.close_door()
        """
        ...

    def is_door_closed(self) -> bool:
        """Функция, возвращающая текущее состояние двери

        :return: Закрыта ли дверь

        Примеры:
        >>> door_1 = Door(True, 'steel', False)
        >>> door_1.close_door()
        """
        ...


class Car:
    def __init__(self, model: str, is_started: bool, gas_value: int):
        """
                Создание и подготовка к работе объекта "Машина"

                :param model: Модель машины
                :param is_started: Заведена ли машина
                :param gas_value: Показатель количества бензина в машине (в процентах)

                Примеры:
                >>> car_1 = Car('Mercedes', False, 24)  # инициализация экземпляра класса
                """
        if not isinstance(model, str):
            raise TypeError("Неверный тип данных для параметра модель машины")
        self.model = model
        if not isinstance(is_started, bool):
            raise TypeError("Неверный тип данных для параметра is_started")
        self.is_started = is_started
        if not isinstance(gas_value, int):
            raise TypeError("Количество бензина должно быть целым числом(измеряется в процентах)")
        if gas_value < 0:
            raise ValueError("Количество бензина не может быть меньше 0 процентов")
        self.gas_value = gas_value

    def get_started(self) -> None:
        """
        Функция, включающая либо выключающая двигатель машины, в зависимости от ее текущего состояния

         Примеры:
        >>> car_1 = Car("Mercedes", True, 25)
        >>> car_1.get_started()
        """
        ...

    def refuel(self) -> None:
        """
        Функция, заправляющая машину до полного бака

        :raise FullTankError: Возвращается ошибка, если машина уже полностью заправлена.

         Примеры:
        >>> car_1 = Car("Mercedes", True, 25)
        >>> car_1.refuel()
        """
        ...

    def get_gas_data(self) -> int:
        """Функция, возвращающая текущее количество бензина

        :return: Количество бензина в машине

        Примеры:
        >>> car_1 = Car("Mercedes", True, 25)
        >>> car_1.get_gas_data()
        """
        ...


fridge_1 = Refrigerator("samsung", 100, 200)
door = Door(True, 'wood', False)
car = Car('Mercedes', True, 48)
if __name__ == "__main__":
    doctest.testmod()
