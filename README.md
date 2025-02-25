# qa_python

    # По большей части избегал негативных тестов, т.к. не уверен, как в таком случае лучше поступить:
    # Сделать условие для ассертов или написать отдельные тесты под негативные сценарии

В файле test.py реализованы следующие юнит-тесты:
1. test_add_new_book_add_one_new_book_true. Тест на добавление 1 книги с длиной названия = макс. кол-ву символов (40)
2. test_add_new_book_add_book_that_already_exists_book_added_once. Тест на невозможность добавить одну и ту же книгу
дважды.
3. test_set_book_genre_book_and_genre_exists_true. Параметризованный тест на добавление жанра для книги, которая есть
в словаре. Так же включена проверка негативного сценария: добавление жанра, которого нет в исходном списке.
4. test_get_book_genre_book_and_genre_exist_true. Тест на получение ранее установленного жанра книги по названию книги.
5. test_get_books_with_specific_genre_add_two_books_diff_genres_returned_one. Тест на получение книг только конкретного
жанра.
6. test_get_books_genre_add_two_books_returned_dict_not_empty. Тест на получение всех книг, ранее добавленных в словарь.
7. test_get_books_for_children_no_books_with_age_rating. Тест на получение только книг без возрастных ограничений.
8. test_add_book_in_favorites_book_added_once. Тест на невозможность добавить в "Избранное" одну и ту же книгу несколько
раз подряд.
9. test_delete_book_from_favorites_favorite_book_deleted. Тест на успешное удаление указанной книги.
10. test_get_list_of_favorites_books_returned_list_is_not_empty. Тест на успешное получение книги из списка "Избранных".