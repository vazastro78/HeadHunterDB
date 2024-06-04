from src.Vacancy import Vacancy


def test_vacancy_contains_right_list():
    """
    создается вакансия
    :return: проверяется правильность работы функции Vacancy.__contains__
     на наличие каждого ключевого слова из списка в этой вакансии
    """
    vacancy1 = Vacancy(1, "Vacancy Name", 1, 15, "Требования: опыт работы от 1 года Python, GIT", "https://api.hh.ru/")
    assert ["pythoN", "giT"] in vacancy1


def test_vacancy_contains_right_str():
    """
    создается вакансия
    :return: проверяется правильность работы функции Vacancy.__contains__
     на наличие одного слова  в этой вакансии, написанного в другом регистре
    """
    vacancy1 = Vacancy(1, "Vacancy Name", 1, 15, "Требования: опыт работы от 1 года Python, GIT", "https://api.hh.ru/")
    assert "giT" in vacancy1


def test_vacancy_contains_wrong():
    """
    создается вакансия
    :return: проверяется правильность работы функции Vacancy.__contains__
     на отсутствие одного из ключевых  слов  в этой вакансии "Django" точно нет
    """
    vacancy1 = Vacancy(1, "Vacancy Name", 1, 15, "Требования: опыт работы от 1 года Python, GIT", "https://api.hh.ru/")
    assert not ["pythoN", "Django"] in vacancy1
