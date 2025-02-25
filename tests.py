import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_new_book_true(self):
        collector = BooksCollector()
        book = 'mxe5kz457iq8gio5jl7N3zF6SBB7opXSjf1C891x'
        collector.add_new_book(book)

        assert book in collector.get_books_genre()

    def test_add_new_book_add_book_that_already_exists_book_added_once(self):
        collector = BooksCollector()
        book = 'Книга, которая уже есть'
        collector.add_new_book(book)
        collector.add_new_book(book)

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book, genre', [['Непобедимый', 'Фантастика'], ['Голубое сало', 'Комедии']])
    def test_set_book_genre_book_and_genre_exists_true(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert genre in collector.get_books_genre()[book]

    @pytest.mark.parametrize('book, genre', [['Властелин колец', 'Фэнтези'], ['Нейромант', 'None']])
    def test_set_book_genre_genre_doesnt_exist_only_book_name(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert genre not in collector.get_books_genre()[book]

    def test_get_book_genre_book_and_genre_exist_true(self):
        collector = BooksCollector()
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')

        assert collector.get_book_genre('Дракула') == 'Ужасы'

    def test_get_books_with_specific_genre_add_two_books_diff_genres_returned_one(self):
        collector = BooksCollector()
        detective_book = 'Собака Баскервилей'
        detective_genre = 'Детективы'
        other_book = 'Мастер и Маргарита'
        other_genre = 'Фантастика'

        collector.add_new_book(detective_book)
        collector.set_book_genre(detective_book, detective_genre)
        collector.add_new_book(other_book)
        collector.set_book_genre(other_book, other_genre)

        assert len(collector.get_books_with_specific_genre(detective_genre)) == 1

    def test_get_books_genre_add_two_books_returned_dict_not_empty(self):
        collector = BooksCollector()
        book_one = 'Плоский мир'
        genre_one = 'Комедии'
        collector.add_new_book(book_one)
        collector.set_book_genre(book_one, genre_one)

        book_two = 'Незнайка на Луне'
        genre_two = 'Мультфильмы'
        collector.add_new_book(book_two)
        collector.set_book_genre(book_two, genre_two)

        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_no_books_with_age_rating(self):
        collector = BooksCollector()
        books = {'Детская книга 1': 'Фантастика',
                 'Детская книга 2': 'Комедии',
                 'Книга с возрастным рейтингом': 'Ужасы'}

        for key, value in books.items():
            collector.add_new_book(key)
            collector.set_book_genre(key, value)

        assert 'Книга с возрастным рейтингом' not in collector.get_books_for_children()

    def test_add_book_in_favorites_book_added_once(self):
        collector = BooksCollector()
        book = 'Тестовая книга'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_favorite_book_deleted(self):
        collector = BooksCollector()
        books = ['Избранная книга', 'Избранная книга Два']

        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        collector.delete_book_from_favorites('Избранная книга')

        assert (len(collector.get_list_of_favorites_books()) == 1
                and 'Избранная книга Два' in collector.get_list_of_favorites_books())

    def test_get_list_of_favorites_books_returned_list_is_not_empty(self):
        collector = BooksCollector()
        book = 'Тестовая избранная книга'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert len(collector.get_list_of_favorites_books()) == 1
