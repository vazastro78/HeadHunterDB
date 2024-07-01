DROP TABLE IF EXISTS employer;

CREATE TABLE employer (
    employer_id INT UNIQUE NOT NULL,
    name VARCHAR(150) NOT NULL,
    url VARCHAR(50) NOT NULL,
    logo_url VARCHAR(80) NOT NULL,
    trusted BOOLEAN NOT NULL DEFAULT FALSE
);



INSERT INTO employer
VALUES
(10420429, 'INTELLIGENCE SYSTEMS LTD.', 'https://hh.ru/employer/10420429', 'https://img.hhcdn.ru/employer-logo-original/1178712.jpeg', TRUE);


SELECT * FROM employer;
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

employer
 employer_id
 name
 url
 logo_url
 trusted
*/
