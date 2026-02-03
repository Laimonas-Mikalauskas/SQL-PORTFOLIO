from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String)

# Create database engine and session
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# SQLAlchemy ORM example to prevent SQL injection
# User input is considered only as data, bun not a code 
user_input_id = input("Enter user ID: ")
user = session.query(User).filter(User.id == int(user_input_id)).first()
