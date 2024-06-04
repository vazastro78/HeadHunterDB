from src.Vacancy import Vacancy


def test_vacancy_repr():
    vacancy = Vacancy(1, "Vacancy Name", 1, 15, "Требования: опыт работы от 1 года", "https://api.hh.ru/")
    assert vacancy.__repr__() == """
1: vacancy name 15 требования: опыт работы от 1 года https://api.hh.ru/"""
