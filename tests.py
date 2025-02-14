from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollectorи
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# проверка на добавление книги с названием, превышающим 40 символов
    def test_add_new_book_title_length_over_40_simbols(self):
        collector = BooksCollector()
        long_title = 'Гордость и предубеждение и зомби: исторический роман, который изменит ваш взгляд на классическую литературу'
        collector.add_new_book(long_title)
        assert long_title not in collector.books_genre
        # добавили книгу с длинным названием и проверяем, что книга не была добавлена

# проверка на добавление одной книги два раза
    def test_add_new_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1
        # добавили две одинаковые книги и проверили, что книга не добавилась


# проверка на установку жанра для книги
    def test_set_book_genre_valid_book_and_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')

        assert collector.books_genre['Гордость и предубеждение'] == 'Роман'
        # добавляем книгу, устанавливаем жанр,проверяем, что жанр был установлен правильно

# проверка на установку жанра для несуществующей книги
    def test_set_book_genre_invalid_book_valid_genre(self):
        collector = BooksCollector()
        collector.set_book_genre('Тучи-облока', 'Роман')

        assert 'Тучи-облока' not in collector.books_genre
        # установка жанра для книги несуществующей книги

# проверка на получение жанра по книге
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')

        assert  collector.get_book_genre('Гордость и предубеждение') == 'Роман'
        #п добавили книгу, жанр, проверили, что жанр получен правильно

# проверка получения книг с определенным жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедия')

        books = collector.get_books_with_specific_genre('Роман')
        assert 'Гордость и предубеждение' in books
        assert 'Что делать, если ваш кот хочет вас убить' not in books
        # добавили 2 книги с жанром, проверили, что возврощается книга с нужным жанром

# проверка на получение книг для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедия')

        collector.genre_age_rating.append('Комедия')

        books_for_children = collector.get_books_for_children()
        assert 'Гордость и предубеждение' in books_for_children
        assert 'Что делать, если ваш кот хочет вас убить' not in books_for_children
        # добавили книги и жанр, добавили возрастной рейтинг для книги, проверяем, что она не попадает в список детских книг

# проверка на добавление книг в избранные
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')

        collector.add_book_in_favorites('Гордость и предубеждение')
        assert 'Гордость и предубеждение' in collector.favorites
        # добавили книгу и жанр, добавили в избранное, проверили, что добавилась

# проверка на удаление книги из избранных
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')

        collector.add_book_in_favorites('Гордость и предубеждение')

        collector.delete_book_from_favorites('Гордость и предубеждение')
        assert 'Гордость и предубеждение' not in collector.favorites
        # добавили книгу и жанр, добавили в избранное, проверили, что удалилась.
        #gitignore

# проверка на получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Роман')

        collector.add_book_in_favorites('Гордость и предубеждение')
        favorites = collector.get_list_of_favorites_books()
        assert 'Гордость и предубеждение' in favorites

