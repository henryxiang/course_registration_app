from config import api

from .student import StudentController

api.add_resource(StudentController, '/api/student/<int:id>', '/api/students')
