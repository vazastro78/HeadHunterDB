from src.Vacancy import Vacancy


def test_vacancy_sort():
    vacancy1 = Vacancy(1, "Vacancy Name", 5, 7, "Требования: опыт работы от 10 лет", "https://api.hh.ru/")
    vacancy2 = Vacancy(2, "Vacancy Name", 1, 8, "Требования: опыт работы от 20 лет", "https://api.hh.ru/")
    vacancy3 = Vacancy(3, "Vacancy Name", 2, 9, "Требования: опыт работы от 30 лет", "https://api.hh.ru/")
    vacancies_list = [vacancy2, vacancy1, vacancy3]
    vacancies_list.sort(reverse=True)
    compare_value = [vacancy_item.id for vacancy_item in vacancies_list]
    assert compare_value == [3, 2, 1]






