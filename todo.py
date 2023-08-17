from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime

# Create database
engine = create_engine('sqlite:///:todo.db:')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name_task = Column(String, default='empty task')
    details = Column(String, default='empty task details')
    limit_date = Column(Date, default=datetime.today())

    def __repr__(self) -> str:
        return f"Table(id={self.id!r}, name={self.name_task!r}, details={self.details!r})"
