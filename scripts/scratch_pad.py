from config import db_session
from model import Student

# Query

student = db_session.query(Student).filter(Student.id == 1).one()

print(student)
