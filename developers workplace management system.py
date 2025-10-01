from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime, timedelta
import sys

Base = declarative_base()
engine = create_engine('sqlite:///developers.db', echo=False)
Session = sessionmaker(bind=engine)

class Python_Developer(Base):
    __tablename__ = "Python"
    id = Column(Integer, primary_key=True)
    name = Column("Garry", String)
    surname = Column("Peterson", String)
    birthday = Column("1990", Integer)
    role = Column("Python Developer", String)
    started_working = Column("2015/06/30", Integer)
    salary = Column("5000", Integer)
    experience = Column("7years", Integer)

    def __init__(self):
        self.name = "Garry"
        self.surname ="Peterson"
        self.birthday = "1990"
        self.role = "Python Developer"
        self.started_working = "2015/06/30"
        self.salary = "5000"
        self.experience = "7 years"

    def __repr__(self):
        return f"{self.name} {self.surname} {self.birthday} {self.role} {self.started_working} {self.salary} {self.experience}"

name = "Garry"
print("Garry")
print(type("Garry"))

surname = "Peterson"
print("Peterson")
print(type("Peterson"))

birthday = "1990"
print("1990")
print(type("1990"))

role = "Python Developer"
print("Python Developer")
print(type("Python Developer"))

started_working = "2015/06/30"
print("2015/06/30")
print(type("2015/06/30"))

salary = "5000"
print("5000")
print(type("5000"))

experience = "10 years"
print("10 years")
print(type("10 years"))

class Software_Developer(Base):
    __tablename__ = "Software"
    id = Column(Integer, primary_key=True)
    name = Column("Josh", String)
    surname = Column("Keller", String)
    birthday = Column("1996", Integer)
    role = Column("Software Developer", String)
    started_working = Column("2019/09/25", Integer)
    salary = Column("4000", Integer)
    experience = Column("6 years", Integer)

def __init__(self):
    self.name = "Josh"
    self.surname = "Keller"
    self.birthday = "1996"
    self.role = "Software Developer"
    self.started_working = "2019/09/25"
    self.salary = "4000"
    self.experience = "6 years"

def __repr__(self):
    return f"{self.name} {self.surname} {self.birthday} {self.role} {self.started_working} {self.salary} {self.experience}"

name = "Josh"
print("Josh")
print(type("Josh"))

surname = "Keller"
print("Keller")
print(type("Keller"))

birthday = "1996"
print("1996")
print(type("1996"))

role = "Software Developer"
print("Software Developer")
print(type("Software Engineer"))

started_working = "2019/09/25"
print("2019/09/25")
print(type("2019/09/25"))

salary = "4000"
print("4000")
print(type("4000"))

experience = "6 years"
print("6 years")
print(type("6 years"))

class Data_Analyst(Base):
    __tablename__ = "Data"
    id = Column(Integer, primary_key=True)
    name = Column("Jack", String)
    surname = Column("Mills", String)
    birthday = Column("1990", Integer)
    role = Column("Data Analyst", String)
    started_working = Column("2021/09/25", Integer)
    salary = Column("3000", Integer)
    experience = Column("4 years", Integer)

def __init__(self):
    self.name = "Jack"
    self.surname = "Mills"
    self.birthday = "1990"
    self.role = "Data analyst"
    self.started_working = "2021/09/25"
    self.salary = "3000"
    self.experience = "4 years"

def __str__(self):
    return f"{self.name} {self.surname} {self.birthday} {self.role} {self.started_working} {self.salary} {self.experience}"

name = "Jack"
print("Jack")
print(type("Jack"))

surname = "Mills"
print("Mills")
print(type("Mills"))

birthday ="1990"
print("1990")
print(type("1990"))

position = "Data Analyst"
print("Data Analyst")
print(type("Data Analyst"))

started_working = "2021/09/25"
print("2021/09/25")
print(type("2021/09/25"))

salary = "3000"
print("3000")
print(type("3000"))

experience = "4 years"
print("4 years")
print(type("4 years"))

class SQL_Programmer(Base):
    __tablename__ = "SQL"
    id = Column(Integer, primary_key=True)
    name = Column("Mark", String)
    surname = Column("Wheeler", String)
    birthday = Column("1993", Integer)
    role = Column("Database Administrator")
    started_working = Column("2023/09/25", Integer)
    salary = Column("2500", Integer)
    experience = Column("2 years", Integer)

def __init__(self):
    self.name = "Mark"
    self.surname = "Wheeler"
    self.birthday = "1993"
    self.role = "Database Administrator"
    self.started_working = "2023/09/25"
    self.salary = "2500"
    self.sxperience = "2 years"

def __str__(self):
    return f"{self.name} {self.surname} {self.birthday} {self.role} {self.started_working} {self.salary} {self.experience}"

name = "Mark"
print("Mark")
print(type("Mark"))

surname = "Wheeler"
print("Wheeler")
print(type("Wheeler"))

birthday = "1993"
print("1993")
print(type("1993"))

role = "Database Administrator"
print("Database Administrator")
print(type("Database Administrator"))

started_working = "2023/09/25"
print("2023/09/25")
print(type("2023/09/25"))

salary = "2500"
print("2500")
print(type("2500"))

experience = "2 years"
print("2 years")
print(type("2 years"))





























































