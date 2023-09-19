from datetime import datetime, timedelta
from models.task import Task, create_session


class Main:
    def __init__(self) -> None:
        self.today = datetime.today().date()
        self.session = create_session()
        self.rows = self.session.query(Task).all()
        self.today_rows = self.session.query(Task).filter(Task.limit_date == self.today).all()

    def option_1(self):
        """Show a list of tasks for today"""
        print('')
        print(f' Today {self.today} '.center(50, '-'))

        if len(self.today_rows) > 0:
            [print(f'{count + 1}. {task}\n') for count, task in enumerate(self.rows)]
        else:
            print("\nYou're free for today. Nothing to do!\n")

    def option_2(self):
        """Show a list of tasks for the week"""
        monday = self.today - timedelta(days=self.today.weekday())
        sunday = monday + timedelta(days=6)
        print('')
        print(f' Week {monday} to {sunday} '.center(50, '-'))

        tasks_in_week = self.session.query(Task).filter(
            Task.limit_date >= monday,
            Task.limit_date <= sunday,
            Task.status == False
        ).all()

        if tasks_in_week:
            print('\nPending tasks or tasks with a deadline during the week:')
            for count, task in enumerate(tasks_in_week):
                print(f'{count+1}: Task: {task.name_task}, Limit date: {task.limit_date}')
            print('')
        else:
            print("\nYou're free for the week. Nothing to do!\n")

    def option_5(self):
        print('')
        print(" Add a new task ".center(50, '-'))

        name_task = input('Task name: ')
        details = input('Task details: ')
        limit_date = input('Task deadline (YYYY-MM-DD): ')

        try:
            limit_date = datetime.strptime(limit_date, '%Y-%m-%d').date()
        except ValueError:
            print('Invalid date format. Please use Year-month-day format.')

        new_task = Task(name_task=name_task, details=details, limit_date=limit_date)
        self.session.add(new_task)
        self.session.commit()
        print(f"\nTask added successfully\n")

    def menu(self):
        option = None
        while option != 8:
            try:
                print('.::Menu de opciones:.'.center(50, '-'))
                print('1. Tasks for today.')
                print('2. Tasks for the week.')
                print('3. All tasks.')
                print('4. Pending tasks.')
                print('5. Add new task.')
                print('6. Modify task.')
                print('7. Delete a task.')
                print('8. Exit.')
                option = int(input('Opción (1-8): '))
                print('')

                if option == 1:
                    self.option_1()
                if option == 2:
                    self.option_2()
                if option == 3:
                    self.option_3()
                if option == 4:
                    self.option_4()
                if option == 5:
                    self.option_5()

            except Exception as e:
                print(f'\nError: {e}\n')
        else:
            print(f'\nExiting… Good bye!')



if __name__ == "__main__":
    Main().menu()
