DROP TABLE IF EXISTS vacancy_keyword;


CREATE TABLE vacancy_keyword (
	vacancy  INT REFERENCES vacancy(vacancy_id) NOT NULL,
	kword_id INT REFERENCES keywords(kword_id)  NOT NULL
);

INSERT INTO vacancy_keyword
VALUES
(101261194, 1),
(101261194, 3)
;
