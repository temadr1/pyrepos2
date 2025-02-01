class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, pages: int, name=None, author=None):
        super().__init__(name, author)
        self.pages = None
        self.pages_initial(pages)

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    def pages_initial(self, pages):
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError
        self.pages = pages


class AudioBook(Book):
    def __init__(self, duration: float, name=None, author=None):
        super().__init__(name, author)
        self.duration = None
        self.duration_initial(duration)

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    def duration_initial(self, duration):
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 0:
            raise ValueError
        self.duration = duration
