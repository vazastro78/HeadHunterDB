from src.HeadHunterParser import HeadHunterParser
from src.DBManager import DBManager,print_rows
from utils.db_connection import load_hh_companies, parse_into_db
import os.path


BASE_DIR = os.path.dirname((os.path.abspath(__file__)))



if __name__ == "__main__":
    load_hh_companies(False)
    parse_into_db()
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

