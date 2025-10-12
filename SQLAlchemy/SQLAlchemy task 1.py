from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///employees.db')
Base = declarative_base()

class Employee(Base):
    __tablename__: str = "Employee"
    id = Column(Integer, primary_key=True)
    name = Column ("Tom", String)
    surname = Column ("Ritter", String)
    birthday = Column ("1991/01/22", DateTime)
    position = Column ("Python developer", String)
    salary = Column ("2000", Float)
    started_working = Column ("2025/06/20", Float)

    def __init__(self):
       self.name = "Tom"
       self.surname = "Ritter"
       self.birthday = "1991/01/22"
       self.position = "Python developer"
       self.salary = "2000"
       self.started_working = "2025/06/20"

    def __repr__(self):
       return f"{self.id} {self.name} - {self.surname} - {self.birthday} - {self.position} - {self.salary} - {self.started_working}"

    Base.metadata.create_all(engine)
