

class Vacancy:
    id: int
    min_salary: float
    max_salary: float
    name: str
    requirements: str

    def __init__(self, id, name, min_salary, max_salary, requirements, url):
        self.id = id
        self.name = name
        self.min_salary = min_salary
        self.max_salary = max_salary
        self.requirements = requirements
        self.url = url

    def __repr__(self):
        """
        Строковое представление текущей вакансии
        Важно: вся строка в нижнем регистре для удобства сравнения
        Функция используется для поиска и сравнения по ключевым словам
        :return: строку в нижнем регистре
        """
        return str.lower(f"\n{self.id}: {self.name} {self.max_salary} {self.requirements} {self.url}")
 
    def __str__(self):
        return f"""
Вакансия №{self.id}
 требуется: {self.name}
 зарплата: {self.min_salary} - {self.max_salary}
 требования: {self.requirements}
 ссылка: {self.url}

"""

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.max_salary > other.max_salary
        elif isinstance(other, float) or isinstance(other, int):
            return self.max_salary > other
        else:
            raise TypeError(f"неподдерживаемый тип сравнения для класса {self.__class__.__name__}")

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.max_salary < other.max_salary
        elif isinstance(other, float) or isinstance(other, int):
            return self.max_salary < other
        else:
            raise TypeError(f"неподдерживаемый тип сравнения для класса {self.__class__.__name__}")

    def __hash__(self):
        """
        Функция используется для сортировки вакансий
           при этом большей вакансией является та, у которой зарплата выше
        :return: максимальную зарплату
        """
        return int(self.max_salary)

    def __contains__(self, words):
        """
        Функция проверяет содержит ли строковое представление вакансии нужные слова
            используя встроенную str.find
        важно, что каждое ключевое слово перед сравнением переводится в нижний регистр
        :param words: массив или строку
        :return: boolean value
        """
        if isinstance(words, str):
            check_wordlist = [words,]
        elif isinstance(words, list):
            check_wordlist = words
        else:
            raise TypeError(f"неподдерживаемый тип содержания слов для класса {self.__class__.__name__}")

        return_value = True
        for word in check_wordlist:
            if not self.__repr__().find(word.lower()) > -1:
                return_value = False
        return return_value

    def is_salary_between(self, min_value, max_value):
        return_value = True
        if self.min_salary < min_value:
            return_value = False
        if self.max_salary > max_value:
            return_value = False
        return return_value


if __name__ == "__main__":
    vacancy1 = Vacancy(91241, "Python Developer1", 1,
                       15, "Требования: опыт работы от 1 года...", "https://api.hh.ru/vacancies/98952800?host=hh.ru")
    print(vacancy1.is_salary_between(1, 16))
