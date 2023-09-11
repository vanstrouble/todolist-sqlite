from datetime import datetime, timedelta
from models.task import Task, create_session


class Main:
    def __init__(self) -> None:
        self.today = datetime.today().date()
        self.session = create_session()
        self.rows = self.session.query(Task).all()
        self.today_rows = self.session.query(Task).filter(Task.limit_date == self.today).all()

    def option_1(self,):
        print('')
        print(f'Today {self.today}'.center(50, '-'))
        if len(self.today_rows) > 0:
            [print(f'{count + 1}. {task}\n') for count, task in enumerate(self.rows)]
        else:
            print("\nYou're free for today. Nothing to do!\n")

    def option_2(self,):
        monday = self.today - timedelta(days=self.today.weekday())
        sunday = monday + timedelta(days=6)
        print('')
        print(f'Week {monday} to {sunday}'.center(50, '-'))
        print('')

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

            except Exception as e:
                print(f'\nError: {e}\n')
        else:
            print(f'\nExiting… Good bye!')



if __name__ == "__main__":
    Main().menu()
