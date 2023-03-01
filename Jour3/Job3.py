class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status


class TaskList:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def remove_task(self, task):
        self.task_list.remove(task)

    def show_as_complete(self, task_number):
        self.task_list[task_number - 1].status = "Complete"

    def show_list(self, l):
        for task in l:
            print(f"______________________\nTitle:\n{task.title}\nDescription:\n{task.description}\nStatus:\n{task.status}")

    def filter_list(self, filter):
        filtered_list = []
        for task in self.task_list:
            if task.status == filter:
                filtered_list.append(task)
        return filtered_list


tasklist = TaskList()

task1 = Task("Manger", "il faut manger", "En cours")
task2 = Task("Dormir", "il faut dormir", "En cours")
task3 = Task("Reveiller", "il faut se reveiller", "En cours")

tasklist.add_task(task1)
tasklist.add_task(task2)
tasklist.add_task(task3)

tasklist.show_as_complete(2)
print(tasklist.show_list(tasklist.filter_list("En cours")))
