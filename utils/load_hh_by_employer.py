import time
import os.path
from src.HeadHunterParser import HeadHunterParser


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
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
        [23427, "РЖД"]
    ]
    Companies = [
     [2245,"Росгосстрах"],
    ]
    
    for employer_id, name in Companies:

        filename = os.path.join(BASE_DIR, "data", f"hh_{employer_id}.json")

        is_online = True
        hh = HeadHunterParser(filename)
        if is_online:
            hh.load_vacancies_by_employer(employer_id)
            hh.save_to_file()
            time.sleep(100)
        else:
            hh.load_from_file()

