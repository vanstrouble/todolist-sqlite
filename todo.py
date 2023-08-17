from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime

# Create database
engine = create_engine('sqlite:///:todo.db:')
Base = declarative_base()
