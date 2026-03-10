from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

# Create database engine and session
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', password='{self.password}')>"

try:
    # Adding users to the database
    user1 = User(name='Alice', password='password123')
    user2 = User(name='Bob', password='securepassword')
    session.add(user1)
    session.add(user2)
    session.commit()

    # SQLAlchemy ORM example to prevent SQL injection
    secure_user_input = input("Enter user ID: ")

    # Validate input to ensure it's an integer
    try:
        user_id = int(secure_user_input)
        user = session.query(User).filter(User.id == user_id).first()

        if user:
            print(f"User found: {user.name}")
        else:
            print("User not found.")
    except ValueError:
        print("Please enter a valid integer for user ID.")

except Exception as e:
    print(f"An error occurred: {e}")