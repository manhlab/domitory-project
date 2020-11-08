import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///student.db')
Base.metadata.create_all(engine)

class Student(Base):
   __tablename__ = 'student'
   id = Column(Integer, primary_key=True)
   title = Column(String(250), nullable=False)
   author = Column(String(250), nullable=False)
   genre = Column(String(250), nullable=False)

   def __init__(self, id, title, author,genre):
      self.id = id
      self.title = title
      self.author = author
      self.genre = genre
   def __repr__(self):
        return '<User %r>' % self.title



