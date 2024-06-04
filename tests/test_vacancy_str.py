from src.Vacancy import Vacancy


def test_vacancy_repr():
    """
    создается вакансия
    :return: проверяется правильность работы функции Vacancy.__str__
    """
    vacancy = Vacancy(1, "Vacancy Name", 1, 15, "Требования: опыт работы от 1 года", "https://api.hh.ru/")
    assert vacancy.__str__() == """
Вакансия №1
 требуется: Vacancy Name
 зарплата: 1 - 15
 требования: Требования: опыт работы от 1 года
 ссылка: https://api.hh.ru/

"""
