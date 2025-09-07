-- 1 Table creation: Person & seed data
CREATE TABLE person (id INTEGER PRIMARY KEY, lname VARCHAR UNIQUE, fname VARCHAR, timestamp DATETIME);
INSERT INTO person VALUES (1, 'Fairy', 'Tooth', '2022-10-08 09:15:10');
INSERT INTO person VALUES (2, 'Ruprecht', 'Knecht', '2022-10-08 09:15:13');
INSERT INTO person VALUES (3, 'Bunny', 'Easter', '2022-10-08 09:15:27');

-- 2 Table creation: Note
CREATE TABLE note (id INTEGER PRIMARY KEY, person_id INTEGER, content VARCHAR, timestamp DATETIME, CONSTRAINT FK_PersonID FOREIGN KEY (person_id) REFERENCES person(id));