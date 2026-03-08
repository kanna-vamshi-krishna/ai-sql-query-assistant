
CREATE DATABASE studentdb;
GO

USE studentdb;
GO

CREATE TABLE STUDENT (
    NAME VARCHAR(50),
    CLASS VARCHAR(50),
    SECTION VARCHAR(5),
    MARKS INT
);

INSERT INTO STUDENT VALUES
('Krish','Data Science','A',90),
('John','Data Science','B',100),
('Mukesh','Data Science','A',86),
('Jacob','DevOps','A',50),
('Dipesh','DevOps','A',35);
