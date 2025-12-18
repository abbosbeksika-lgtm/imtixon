# CREATE TABLE teacher (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     salary NUMERIC(12,2),
#     phone VARCHAR(20),
#     email VARCHAR(100)
# );
# CREATE TABLE admin (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     phone VARCHAR(20),
#     role VARCHAR(50)
# );
#
# CREATE TABLE groups (
#     id SERIAL PRIMARY KEY,
#     group_name VARCHAR(100),
#     teacher_id INT REFERENCES teacher(id),
#     room VARCHAR(50)
# );
#
# CREATE TABLE student1 (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     phone VARCHAR(20),
#     birth_date DATE,
#     group_id INT REFERENCES groups(id)
# );
#
# CREATE TABLE dars (
#     id SERIAL PRIMARY KEY,
#     group_id INT REFERENCES groups(id),
#     topic VARCHAR(200)
# );
#
# CREATE TABLE uyga_vazifa (
#     id SERIAL PRIMARY KEY,
#     lesson_id INT REFERENCES dars(id),
#     description TEXT
# );
#
# CREATE TABLE yoqlama (
#     id SERIAL PRIMARY KEY,
#     student_id INT REFERENCES student(id),
#     lesson_id INT REFERENCES dars(id),
#     status VARCHAR(20),
#     note TEXT
# );
#
# CREATE TABLE tolov (
#     id SERIAL PRIMARY KEY,
#     student_id INT REFERENCES student(id),
#     amount NUMERIC(12,2),
#     payment_date DATE,
#     method VARCHAR(50)
# );
