from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

engine = create_engine('sqlite:///todo.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_task = Column(String, default='empty task')
    details = Column(String, default='empty task details')
    created_at = Column(Date, default=datetime.today().date())
    limit_date = Column(Date, default=datetime.today().date())
    status = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, name_task={self.name_task!r}, details={self.details!r}, created={self.created_at!r}, limit_date={self.limit_date!r}, status={self.status!r})"

Base.metadata.create_all(engine)

new_task = Task(name_task='Add new task to todo', details='IDK, just making a DB', limit_date=datetime(2020, 8, 20).date())
session.add(new_task)
session.commit()
