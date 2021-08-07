from config import db_session
from model import Student
from faker import Faker

fake = Faker()

for i in range(100):
    student = Student(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email())
    db_session.add(student)
    db_session.commit()
    print(student)
