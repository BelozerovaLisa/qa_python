from main import BooksCollector

import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # тест add_new_book с граничными значениями параметров (1,11,39)
    @pytest.mark.parametrize('name',['А', 'Война и мир','Справочник по разведению домашних цыплят'])
    def test_add_new_book_with_different_parameters(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1


    # тест set_book_genre - c жанром вне списка
    def test_set_book_genre_set_genre_not_in_list_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Романтика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') != 'Романтика'


    # тест get_book_genre - добавляем книгу с именем которого нет в словаре
    def test_get_book_genre_name_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Паровозик Томас') == None

    # тест get_books_with_specific_genre - когда передается жанр из словаря
    def test_get_books_with_specific_genre_with_genre_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Паровозик Томас')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Паровозик Томас', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Паровозик Томас']

    #  тест get_books_for_children - добавляет в список только книги для детей
    def test_get_books_for_children_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Паровозик Томас')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Паровозик Томас', 'Мультфильмы')
        assert 'Гордость и предубеждение и зомби' not in collector.get_books_for_children()

    # тест add_book_in_favorites c книгой которая уже есть в избранном
    def test_add_book_in_favorites_with_books_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Паровозик Томас')
        collector.add_book_in_favorites('Паровозик Томас')
        collector.add_book_in_favorites('Паровозик Томас') # добавляем еще раз
        assert len(collector.get_list_of_favorites_books()) == 1

    # тест delete_book_from_favorites - удаляем книгу которой нет в избранном
    def test_delete_book_from_favorites_with_book_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.delete_book_from_favorites('Паровозик Томас') == None

    # тест get_list_of_favorites_books - книги добавляются в избранное
    def test_get_list_of_favorites_books_add_books_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Паровозик Томас')
        collector.add_book_in_favorites('Паровозик Томас')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        for i in ['Гордость и предубеждение и зомби','Паровозик Томас']:
            assert i in collector.get_list_of_favorites_books()
