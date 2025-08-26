from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///many2one_test.db")
Base = declarative_base()

class Person (Base):
    __tablename__ = "Person"
    id = Column(Integer, primary_key=True)
    name = Column("Ben", String)
    surname = Column("Wilson", String)
    person_id = Column("42500214888", Float)
    mobile = Column("+44077411990", Float)

    def __str__(self):
        return f"{self.name} {self.surname} {self.person_id} {self.mobile}"

class Bank (Base):
    __tablename__ = "Bank"
    id = Column(Integer, primary_key=True)
    name = "Revolut"
    address = "78 Stone Street, Ipswich, Suffolk, GB852 222"
    code = "SWIFT 2247800554"
    account = "GB2004877715"








