class Book:
    # Статическое поле класса для отслеживания общего количества книг
    total_books = 0

    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        # Увеличиваем общее количество книг при создании нового экземпляра
        Book.total_books += 1

    def display_info(self):
        # Метод экземпляра класса для отображения информации о книге
        print(
            f"Книга: {self.title}, Автор: {self.author}, Жанр: {self.genre}, Страниц: {self.pages}"
        )

    @staticmethod
    def convert_pages_to_words(page_count):
        # Статический метод для конвертации количества страниц в количество слов (просто для примера)
        return page_count * 250

    @classmethod
    def display_total_books(cls):
        # Метод класса для вывода общего количества книг
        print(f"Общее количество книг: {cls.total_books}")


# Создаем несколько экземпляров класса Book
book1 = Book("Преступление и наказание", "Ф.М. Достоевский", "Роман", 450)
book2 = Book("1984", "Дж. Оруэлл", "Дистопия", 320)
book3 = Book("Мастер и Маргарита", "М. Булгаков", "Фэнтези", 380)

# Вызываем методы экземпляра класса
book1.display_info()

# Вызываем статический метод
word_count = Book.convert_pages_to_words(300)
print(f"Количество слов в 300 страницах: {word_count}")

# Вызываем метод класса
Book.display_total_books()
