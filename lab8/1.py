from appJar import gui

class TaskError(Exception):
    pass

class TaskNotFoundError(TaskError):
    pass

class EmptyError(TaskError):
    pass

class Task:
    def __init__(self, title):
        if not title.strip():
            raise EmptyError("Задача не может быть пустой")
        self.title = title
        self.completed = False

    def done(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.title} [{status}]"



class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def delete_task(self, index):
        try:
            del self.tasks[index]
        except IndexError:
            raise TaskNotFoundError("Задача не найдена")

    def complete_task(self, index):
        try:
            self.tasks[index].done()
        except IndexError:
            raise TaskNotFoundError("Задача не найдена")

    def get_tasks(self):
        return [str(task) for task in self.tasks]


class TodoApp:
    def __init__(self):
        self.manager = TaskManager()
        self.app = gui("ToDo", "400x400")

        self.app.addLabel("title", "Список задач")
        self.app.addListBox("tasks", [])

        self.app.addEntry("taskEntry")
        self.app.addButton("Добавить", self.add_task)
        self.app.addButton("Удалить", self.delete_task)
        self.app.addButton("Выполнено", self.complete_task)

    def refresh_list(self):
        self.app.updateListBox("tasks", self.manager.get_tasks())

    def add_task(self, btn):
        try:
            title = self.app.getEntry("taskEntry")
            self.manager.add_task(title)
            self.refresh_list()
            self.app.clearEntry("taskEntry")
        except TaskError as e:
            self.app.errorBox("Ошибка", str(e))

    def delete_task(self, btn):
        try:
            selected = self.app.getListBox("tasks")
            if not selected:
                raise TaskNotFoundError("Выберите задачу")
            index = self.manager.get_tasks().index(selected[0])
            self.manager.delete_task(index)
            self.refresh_list()
        except TaskError as e:
            self.app.errorBox("Ошибка", str(e))

    def complete_task(self, btn):
        try:
            selected = self.app.getListBox("tasks")
            if not selected:
                raise TaskNotFoundError("Выберите задачу")
            index = self.manager.get_tasks().index(selected[0])
            self.manager.complete_task(index)
            self.refresh_list()
        except TaskError as e:
            self.app.errorBox("Ошибка", str(e))
    def run(self):
        self.app.go()


if __name__ == "__main__":
    TodoApp().run()
