DROP TABLE IF EXISTS vacancy;

CREATE TABLE vacancy (
    vacancy_id INT UNIQUE NOT NULL,
    name VARCHAR(150) NOT NULL,
    requirement TEXT NOT NULL,
    responsibility TEXT NOT NULL,
    salary real,
    url VARCHAR(150) NOT NULL,
    employer_id INT REFERENCES employer(employer_id) NOT NULL,
    published_at TIMESTAMP WITH TIME ZONE
);

INSERT INTO vacancy
VALUES
(101261194, 'Менеджер проектов', 'Умения вакансии', 'Должен уметь вести проекты', 35000, 'https://hh.ru/vacancy/101261194', 10420429, '2024-06-04T13:41:32+0300');

SELECT * FROM vacancy;

/*
"employer":
{
    "id": "10420429",
    "name": "\u0427\u041a INTELLIGENCE SYSTEMS LTD.",
    "url": "https://api.hh.ru/employers/10420429",
    "alternate_url": "https://hh.ru/employer/10420429",
    "logo_urls": {"90": "https://img.hhcdn.ru/employer-logo/6335274.jpeg",
          "original": "https://img.hhcdn.ru/employer-logo-original/1178712.jpeg", "240": "https://img.hhcdn.ru/employer-logo/6335275.jpeg"},
    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10420429",
    "accredited_it_employer": false,
    "trusted": true
}

vacancies
 vacancy_id
 name
 description
 salary
 keyword
 company_id
 url


CREATE TABLE vacancy (
    vacancy_id INT UNIQUE NOT NULL,
    name VARCHAR(150) NOT NULL,
    requirement TEXT NOT NULL,
    responsibility TEXT NOT NULL,
    salary real,
    url VARCHAR(150) NOT NULL,
    employer_id INT REFERENCES employer(employer_id) NOT NULL
);



INSERT INTO vacancy
VALUES
(101261194, 'Менеджер проектов', 'Умения вакансии', 'Должен уметь вести проекты', 35000, 'https://hh.ru/vacancy/101261194', 10420429);

*/
