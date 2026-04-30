# 1 ВАРИАНТ
Реализуйте приложение с GUI (приложения-игры допускается делать с использованием TUI-пакетов) по своему варианту. Можно изменить задание на собственную тему, согласовав с преподавателем. Требования:

- приложение должно быть написано с применением ОО парадигмы
- исключительные ситуации должны обрабатываться с использованием собственных исключений
- GUI/TUI фреймворки не должны повторяться в группе


# Результаты вычислений:
```python
from appJar import gui

class TaskError(Exception):
    def error(self, app):
        app.errorBox("Ошибка", str(self))

class TaskNotFoundError(TaskError):
    def error(self, app):
        app.errorBox("Ошибка", "Выберите задачу")

class EmptyError(TaskError):
    def error(self, app):
        app.errorBox("Ошибка", "Задача не может быть пустой")

class Task:
    def __init__(self, title):
        if not title.strip():
            raise EmptyError()
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
            raise TaskNotFoundError()

    def complete_task(self, index):
        try:
            self.tasks[index].done()
        except IndexError:
            raise TaskNotFoundError()

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
            e.error(self.app)

    def delete_task(self, btn):
        try:
            selected = self.app.getListBox("tasks")
            if not selected:
                raise TaskNotFoundError()
            index = self.manager.get_tasks().index(selected[0])
            self.manager.delete_task(index)
            self.refresh_list()
        except TaskError as e:
            e.error(self.app)

    def complete_task(self, btn):
        try:
            selected = self.app.getListBox("tasks")
            if not selected:
                raise TaskNotFoundError()
            index = self.manager.get_tasks().index(selected[0])
            self.manager.complete_task(index)
            self.refresh_list()
        except TaskError as e:
            e.error(self.app)
    def run(self):
        self.app.go()


if __name__ == "__main__":
    TodoApp().run()
```
<img width="402" height="452" alt="image" src="https://github.com/user-attachments/assets/a896dc10-004f-4dd6-96be-c505bc558d89" />










1. Класс Task описывает отдельную задачу и хранит её название и состояние выполнения. <br>
2. Класс TaskManager управляет списком задач и выполняет операции добавления, удаления и изменения статуса задач. <br>
3. Каждое действие пользователя создаёт или изменяет объект задачи, а результат сразу обновляется в графическом интерфейсе. <br>






# Список использованных источников:
1. [AppJar — Python](https://appjar.readthedocs.io/en/stable/mkdocs/docs/)
