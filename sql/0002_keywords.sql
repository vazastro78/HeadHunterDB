DROP TABLE IF EXISTS keywords;


CREATE TABLE keywords (
	kword_id INT PRIMARY KEY,
	kword VARCHAR(100) NOT NULL
);



INSERT INTO keywords
VALUES
(1, 'python'),
(2, 'sql'),
(3, 'html')
;



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
*/
