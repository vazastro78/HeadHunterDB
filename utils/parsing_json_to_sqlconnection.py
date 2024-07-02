import json
import glob
import os.path
import psycopg2

kwargs = {
  'host':'localhost',
  'database':'hh_db',
  'user':'hh_database_user',
  'password':'D2a2e82DB7142E15'
  }

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_from_files(template="hh_*.json"):
    vacancies_list = []
    file_names = sorted( glob.glob( os.path.join(BASE_DIR, "data", template) ) )
    for json_filename in file_names:
        with open(json_filename, mode="r", encoding='utf8') as fp:
            json_text = json.load(fp)
        vacancies_list += json_text["items"]
    return vacancies_list



conn = psycopg2.connect(**kwargs)
try:
    with (conn):
        with conn.cursor() as cur:

            for vacancy_item in load_from_files():
                '''
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
                '''

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

