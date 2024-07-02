import json
import os.path
import psycopg2

kwargs = {
  'host':'localhost',
  'database':'hh_db',
  'user':'hh_database_user',
  'password':'D2a2e82DB7142E15'
  }

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_from_file(json_filename):
        with open(json_filename, mode="r", encoding='utf8') as fp:
            json_text = json.load(fp)
        return json_text["items"]

Companies = [
        [3388, "Газпромбанк"],
        [4934, "ПАО ВЫМПЕЛКОМ Билайн"],
        [3529, "Сбербанк"],
        [2242, "РЕСО-Гарантия"],
        [78638, "Т-Банк"],
        [1057, "Лаборатория Касперского"],
        [869045, "Московский метрополитен"],
        [2748, "ПАО Ростелеком"],
        [58320, "Россельхозбанк"],
        [23427, "РЖД"],
        [2245, "Росгосстрах"],
]
vacancies_list = []

for employer_id, name in Companies:
    json_filename = os.path.join(BASE_DIR, "data", f"hh_{employer_id}.json")
    vacancies_list += load_from_file(json_filename)


conn = psycopg2.connect(**kwargs)
try:
    with conn:
        with conn.cursor() as cur:
            for company in vacancies_list:
                item = company["employer"]
                employer_id = item["id"]
                name = item["name"]
                url = item["alternate_url"]
                logo_url = item["logo_urls"]["original"]
                trusted = item["trusted"]
                cur.execute("""
INSERT INTO  employer(employer_id, name,  url, logo_url, trusted) 
SELECT 
	%s, %s, %s, %s, %s
WHERE NOT EXISTS ( 
    SELECT 1 FROM employer WHERE employer_id = %s
);
                """,(employer_id, name,  url, logo_url, trusted, employer_id))
                conn.commit()
finally:
    conn.close()

