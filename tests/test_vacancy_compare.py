from src.Vacancy import Vacancy


def test_vacancy_compare_lt_number():
    vacancy1 = Vacancy(1, "Vacancy Name", 1, 15, "Требования: опыт работы от 1 года", "https://api.hh.ru/")
    assert vacancy1 < 20


def test_vacancies_compare_lt():
    vacancy1 = Vacancy(1, "Vacancy Name", 1, 15, "Требования: опыт работы от 1 года", "https://api.hh.ru/")
    vacancy2 = Vacancy(2, "Vacancy Name", 10, 20, "Требования: опыт работы от 10 лет", "https://api.hh.ru/")
    assert vacancy1 < vacancy2
