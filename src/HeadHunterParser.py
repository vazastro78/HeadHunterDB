import requests
import json
import os
from JobApplicationParser import JobApplicationParser
from Vacancy import Vacancy

from currency_utils import *


class HeadHunterParser(JobApplicationParser):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self, json_filename):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies_list = []
        super().__init__(json_filename)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies_list_part = response.json()['items']
            self.vacancies_list.extend(vacancies_list_part)
            self.params['page'] += 1

    def save_to_file(self):
        json_text = {"items": self.vacancies_list}
        with open(self.json_filename, mode="w", encoding='utf8') as fp:
            json.dump(json_text, fp)

    def load_from_file(self):
        with open(self.json_filename, mode="r", encoding='utf8') as fp:
            json_text = json.load(fp)
        self.vacancies_list = json_text["items"]

    def parse_and_verify(self):
        return_value = []
        for vacancy_item in self.vacancies_list:
            id = vacancy_item["id"]
            name = vacancy_item["name"]
            salary_min = 0
            salary_max = 0
            salary_currency_name = ""
            if vacancy_item["salary"]:
                salary_min = vacancy_item["salary"]["from"]
                salary_max = vacancy_item["salary"]["to"]
                salary_currency_name = vacancy_item["salary"]["currency"]
                if salary_min is None:
                    salary_min = salary_max
                if salary_max is None:
                    salary_max = salary_min
                if salary_currency_name != "RUR":
                    salary_min = my_currency_converter.convert(salary_min, salary_currency_name, 'RUB')
                    salary_max = my_currency_converter.convert(salary_max, salary_currency_name, 'RUB')
                    salary_currency_name = "RUB"
                else:
                    salary_currency_name = "RUB"
            requirements = vacancy_item['snippet']['requirement']
            if "url" in vacancy_item:
                url = vacancy_item["url"]
            else:
                url = ""
            if salary_currency_name == "RUB":
                vacancy = Vacancy(id, name, salary_min, salary_max, requirements, url)
                return_value.append(vacancy)
        return return_value


if __name__ == "__main__":
    filename = os.path.join("..", "data", "hh_python.json")

    is_online = False
    hh = HeadHunterParser(filename)
    if is_online:
        hh.load_vacancies("Python")
        hh.save_to_file()
    else:
        hh.load_from_file()

    vacancies_list = hh.parse_and_verify()
    print(vacancies_list)
