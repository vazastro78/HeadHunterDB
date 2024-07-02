import os.path
import json
import codecs
import time
import psycopg2
import glob


from src.HeadHunterParser import HeadHunterParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename = os.path.join(BASE_DIR, "data", "db_settings.json")

with open(filename, mode="r", encoding='utf8') as fp:
    kwargs = json.load(fp)


filename = os.path.join(BASE_DIR, "data", "companies_settings.json")
with open(filename, mode="r", encoding='utf8') as fp:
    companies = json.load(fp)

def load_hh_companies(is_online=True):
    for employer in companies["companies"]:
        employer_id = employer["company_id"]
        print(f"load for company with id {employer_id}")

        filename = os.path.join(BASE_DIR, "data", f"hh_{employer_id}.json")
        hh = HeadHunterParser(filename)
        if is_online:
            hh.load_vacancies_by_employer(employer_id)
            hh.save_to_file()
            time.sleep(100)
        else:
            hh.load_from_file()

def load_from_files(template="hh_*.json"):
    vacancies_list = []
    file_names = sorted( glob.glob( os.path.join(BASE_DIR, "data", template) ) )
    for json_filename in file_names:
        with open(json_filename, mode="r", encoding='utf8') as fp:
            json_text = json.load(fp)
        vacancies_list += json_text["items"]
    return vacancies_list

def parse_into_db():
    conn = psycopg2.connect(**kwargs)
    try:
        with (conn):
            with conn.cursor() as cur:
                for vacancy_item in load_from_files():
                    company = vacancy_item["employer"]
                    employer_id = company["id"]
                    name = company["name"]
                    url = company["alternate_url"]
                    logo_url = company["logo_urls"]["original"]
                    trusted = company["trusted"]
                    cur.execute("""
INSERT INTO  employer(employer_id, name,  url, logo_url, trusted) 
SELECT 
	%s, %s, %s, %s, %s
WHERE NOT EXISTS ( 
    SELECT 1 FROM employer WHERE employer_id = %s
);
                """,(employer_id, name,  url, logo_url, trusted, employer_id))
                    conn.commit()

                    vacancy_id = vacancy_item["id"]
                    name = vacancy_item["name"]
                    salary = 0
                    requirement = vacancy_item["snippet"]["requirement"]
                    if not requirement:
                        requirement = ""
                    responsibility = vacancy_item["snippet"]["responsibility"]
                    if not responsibility:
                        responsibility = ""
                    if vacancy_item["salary"]:
                        if vacancy_item["salary"]["currency"] == "RUR":
                            if vacancy_item["salary"]["to"]:
                                salary = vacancy_item["salary"]["to"]
                            elif vacancy_item["salary"]["from"]:
                                salary = vacancy_item["salary"]["from"]
                            else:
                                salary = 0
                    url = vacancy_item["alternate_url"]
                    published_at = vacancy_item["published_at"]
                    employer_id = vacancy_item["employer"]["id"]

                    cur.execute("""
INSERT INTO  vacancy(vacancy_id, name, requirement, responsibility, salary, url, employer_id, published_at) 
SELECT 
	%s, %s, %s, %s, %s, %s, %s, %s
WHERE NOT EXISTS ( 
    SELECT 1 FROM vacancy WHERE vacancy_id = %s
);
                """,(vacancy_id, name, requirement, responsibility, salary, url, employer_id, published_at, vacancy_id))
                    conn.commit()
    finally:
        conn.close()

