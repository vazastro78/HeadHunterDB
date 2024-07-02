import json
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_from_file(json_filename):
        with open(json_filename, mode="r", encoding='utf8') as fp:
            json_text = json.load(fp)
        return json_text["items"]

employer_id = 23427
json_filename = os.path.join(BASE_DIR, "data", f"hh_{employer_id}.json")


for company in load_from_file(json_filename):
    item = company["employer"]
    employer_id = item["id"]
    name = item["name"]
    url = item["alternate_url"]
    logo_url = item["logo_urls"]["original"]
    trusted = item["trusted"]

    sql_request = f"""
INSERT INTO  employer(employer_id, name,  url, logo_url, trusted) 
SELECT 
	{employer_id}, '{name}',  '{url}', '{logo_url}', {trusted}
WHERE NOT EXISTS ( 
    SELECT 1 FROM employer WHERE employer_id = {employer_id}
);
    """
    print( sql_request )
    """
    cur.execute(
        "INSERT INTO  employer (employer_id, name,  url, logo_url, trusted) VALUES (%s, %s, %s, %s, %s) ",
        (employer_id, name,  url, logo_url, trusted)
    )
    conn.commit()
    """

