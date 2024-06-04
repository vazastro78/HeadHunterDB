from src.Vacancy import Vacancy


def test_vacancy_contains_right_list():
    vacancy1 = Vacancy(1, "Vacancy Name", 1, 15, "Требования: опыт работы от 1 года Python, GIT", "https://api.hh.ru/")
    assert ["pythoN", "giT"] in vacancy1

def test_vacancy_contains_right_str():
    vacancy1 = Vacancy(1, "Vacancy Name", 1, 15, "Требования: опыт работы от 1 года Python, GIT", "https://api.hh.ru/")
    assert "giT" in vacancy1

def test_vacancy_contains_wrong():
    vacancy1 = Vacancy(1, "Vacancy Name", 1, 15, "Требования: опыт работы от 1 года Python, GIT", "https://api.hh.ru/")
    assert not ["pythoN", "Django"] in vacancy1







