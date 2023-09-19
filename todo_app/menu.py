from datetime import datetime, timedelta
from controller.connection import Task, create_session


class Menu:
    def __init__(self) -> None:
        self.today = datetime.today().date()
        self.session = create_session()
        self.rows = self.session.query(Task).all()

    def option_1(self):
        """Show a list of tasks for today"""
        print(f' Today {self.today} '.center(50, '-'))

        today_rows = self.session.query(Task).filter(Task.limit_date == self.today).all()
        if len(today_rows) > 0:
            [print(f'{count + 1}. \n{task}\n') for count, task in enumerate(today_rows)]
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
            [print(f'{count + 1}. \n{task}\n') for count, task in enumerate(tasks_in_week)]
        else:
            print("\nYou're free for the week. Nothing to do!\n")

    def option_3(self):
        """Show all tasks"""
        print(f" All tasks: {self.session.query(Task).count()} ".center(50, '-'))

        all_tasks = self.session.query(Task).all()
        [print(f"\n{task}") for task in all_tasks]
        print('')

    def option_4(self):
        """Show a list of pending tasks"""
        print(f" Incomplete tasks: {self.session.query(Task).filter(Task.status == False).count()} ".center(50, '-'))
        pending_task = self.session.query(Task).filter(Task.status == False).all()
        [print(f"\n{task}") for task in pending_task]
        print('')

    def option_5(self):
        """Add a new task"""
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

    def option_6(self):
        """Modify a task"""
        print(" Modify a task ".center(50, '-'))
        id_task = int(input('Task id to modify: '))

        task_to_modify = self.session.query(Task).filter(Task.id == id_task).first()

        if task_to_modify:
            print(f"Modifying task with ID {id_task}: {task_to_modify.name_task}")
            new_name = input('Enter the new task name (press Enter to keep it unchanged): ')
            new_details = input('Enter the new task details (press Enter to keep it unchanged): ')
            new_limit_date = input('Enter the new limit date (YYYY-MM-DD) (press Enter to keep it unchanged): ')
            update_status = input('Do you want to update the task status? (y/n): ')

            if new_name:
                task_to_modify.name_task = new_name
            if new_details:
                task_to_modify.details = new_details
            if new_limit_date:
                try:
                    task_to_modify.limit_date = datetime.strptime(new_limit_date, '%Y-%m-%d').date()
                except ValueError:
                    print('Invalid date format. Task limit date not updated.')

            if update_status.lower() == 'y':
                new_status = input('Enter the new task status (Complete/Incomplete): ').capitalize()
                if new_status in ['Complete', 'Incomplete']:
                    task_to_modify.status = (new_status == 'Complete')
                else:
                    print('Invalid status. Task status not updated.')

            self.session.commit()
            print('\nTask modified successfully.\n')
        else:
            print(f'\nTask with ID {id_task} not found.\n')

    def option_7(self):
        """Delete a task"""
        print(" Delete a task ".center(50, '-'))
        id_task = int(input('Task id to modify: '))

        task_to_delete = self.session.query(Task).filter(Task.id == id_task).first()
        if task_to_delete:
            self.session.query(Task).filter(Task.id == id_task).delete()
            print('\nTask deleted successfully.\n')
        else:
            print(f'\nTask with ID {id_task} not found.\n')

    def menu(self):
        option = None
        while option != 8:
            try:
                print('.::Menu de opciones::.'.center(50, '-'))
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
                if option == 6:
                    self.option_6()
                if option == 7:
                    self.option_7()

            except Exception as e:
                print(f'\nError: {e}\n')
        else:
            print(f'\nExiting… Good bye!')



if __name__ == "__main__":
    Menu().menu()
