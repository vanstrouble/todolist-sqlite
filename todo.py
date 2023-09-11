from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Create databse
engine = create_engine("sqlite:///todo.db")
Base = declarative_base()

Session = sessionmaker(bind=engine)


# Create task table
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_task = Column(String, default="empty task")
    details = Column(String, default="empty task details")
    created_at = Column(Date, default=datetime.today().date())
    limit_date = Column(Date, default=datetime.today().date())
    status = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"""\
        Task ID: {self.id}
        Task Name: {self.name_task}
        Task Details: {self.details}
        Created Date: {self.created_at}
        Limit Date: {self.limit_date}
        Status: {'Completed' if self.status else 'Incomplete'}\
        """


# Create all
Base.metadata.create_all(engine)

if __name__ == "__main__":
    try:
        with Session() as session:
            # Add new row
            # new_task = Task(
            #     name_task="Add new task to todo",
            #     details="IDK, just making a DB",
            #     limit_date=datetime(2020, 8, 20).date(),
            # )
            # session.add(new_task)
            # session.commit()  # Consolidate everything

            rows = session.query(Task).all()
            [print(task) for task in rows]
    except SQLAlchemyError as e:
        # Handle database errors here
        print(f"An error occurred: {e}")
