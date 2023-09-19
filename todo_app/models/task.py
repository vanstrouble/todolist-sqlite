class Task:
    def __init__(self, id_task=None, name_task=None, details=None, created_at=None, limit_date=None, status=None) -> None:
        self._id_task = id_task
        self._name_task = name_task
        self._details = details
        self._created_at = created_at
        self._limit_date = limit_date
        self._status = status

    def __str__(self):
        status_str = 'Completed' if self._status else 'Incomplete'
        return f'''
        Task ID: {self._id_task}
        Task Name: {self._name_task}
        Task Details: {self._details}
        Created Date: {self._created_at}
        Limit Date: {self._limit_date}
        Status: {status_str}
        '''

    @property
    def id_task(self):
        return self._id_task

    @id_task.setter
    def id(self, id_task):
        self._id_task = id_task

    @property
    def name_task(self):
        return self._name_task

    @name_task.setter
    def name_task(self, name_task):
        self._name_task = name_task

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, details):
        self._details = details

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def limit_date(self):
        return self._limit_date

    @limit_date.setter
    def limit_date(self, limit_date):
        self._limit_date = limit_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status


if __name__ == '__main__':
    task1 = Task(1, "Hacer compras", "Comprar leche y pan", "2023-09-20", "2023-09-22", False)
    print(task1)

    task2 = Task(2, "Recoger la casa", "Limpiar el piso y los muebles", "2023-09-20", "2023-09-22", False)
    print(task2)
