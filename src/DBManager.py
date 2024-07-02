import os.path
import json
import psycopg2


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




class DBManager:
    def __init__(self):
        self.get_db_settings()

    def get_db_settings(self, filename="db_settings.json"):
        filename = os.path.join(BASE_DIR, "data", filename)
        with open(filename, mode="r", encoding='utf8') as fp:
            self.db_settings = json.load(fp)

    def get_companies_and_vacancies_count(self):
        """
        получает список всех компаний и количество вакансий у каждой компании
        """
        print("""
        SQL запрос с расчетом, сколько вакансий у каждой компании
        """)
        conn = psycopg2.connect( **self.db_settings )
        try:
            with (conn):
                with conn.cursor() as cur:
                    cur.execute("""
SELECT E.name, COUNT(V.name) FROM vacancy AS V
JOIN  employer AS E USING(employer_id) GROUP BY E.name
	ORDER BY COUNT(V.name) DESC;
                """)
                    rows = cur.fetchall()
                    return rows
        finally:
            conn.close()

    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        """
        print("""
        SQL запрос с выдачей всех вакансий и их url-ссылок
        """)
        conn = psycopg2.connect( **self.db_settings )
        try:
            with (conn):
                with conn.cursor() as cur:
                    cur.execute("""
SELECT E.name, V.name, V.url FROM vacancy AS V
	JOIN employer AS E USING(employer_id);
                """)
                    rows = cur.fetchall()
                    return rows
        finally:
            conn.close()

    def get_avg_salary(self, vacancy_name):
        """
        получает среднюю зарплату по вакансиям, совпадающих по шаблону.
        """
        print(f"""
        SQL запрос с выдачей средней ЗП по вакансиям: {vacancy_name}
        """)
        conn = psycopg2.connect( **self.db_settings )
        try:
            with (conn):
                with conn.cursor() as cur:
                    cur.execute("""
SELECT AVG(V.salary)  FROM vacancy AS V WHERE LOWER(V.name) like LOWER( %s ) and V.salary>0;""",  (vacancy_name,) )
                    rows = cur.fetchall()
                    return rows
        finally:
            conn.close()

    def get_vacancies_with_higher_salary(self):
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        print("""
        SQL запрос получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """)
        conn = psycopg2.connect( **self.db_settings )
        try:
            with (conn):
                with conn.cursor() as cur:
                    cur.execute("""
SELECT DISTINCT name  FROM vacancy AS V
	WHERE salary > (SELECT AVG(V.salary) FROM vacancy AS V WHERE salary>0);
	                """)
                    rows = cur.fetchall()
                    return rows
        finally:
            conn.close()




    def get_vacancies_with_keyword(self, keyword):
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python
        """
        print(f"""
        SQL запрос получает список всех вакансий, в названии которых содержатся переданные в метод слова
        {keyword}
        """)
        conn = psycopg2.connect( **self.db_settings )
        try:
            with (conn):
                with conn.cursor() as cur:
                    cur.execute("""
SELECT DISTINCT V.name FROM vacancy AS V
	WHERE LOWER(V.name) like LOWER( CONCAT('%%',%s,'%%') );
	                """, (keyword,))
                    rows = cur.fetchall()
                    return rows
        finally:
            conn.close()

def print_rows( rows ):
    for row in rows:
        print(row)

if __name__ == "__main__":
    dbmanager = DBManager()
    rows = dbmanager.get_companies_and_vacancies_count()
    print_rows( rows )
    rows = dbmanager.get_all_vacancies()
    print_rows( rows )
    rows = dbmanager.get_avg_salary("%администратор%")
    print_rows( rows )
    rows = dbmanager.get_avg_salary("%python%")
    print_rows( rows )
    rows = dbmanager.get_vacancies_with_higher_salary()
    print_rows(rows)
    rows = dbmanager.get_vacancies_with_keyword("python")
    print_rows(rows)


