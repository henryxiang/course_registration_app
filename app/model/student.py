from config import Base
from sqlalchemy import Column, Integer, String
from pprint import pformat


class Student(Base):
    __tablename__ = 'students'

    id: int = Column(Integer, primary_key=True)
    first_name: str = Column(String(50), nullable=False)
    last_name: str = Column(String(50), nullable=False)
    email: str = Column(String(100), nullable=False)
    password: str = Column(String(50), nullable=False, default='')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return pformat(self.to_dict(), indent=2, width=50)
