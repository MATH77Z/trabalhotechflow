class TaskManager:
    def __init__(self): self.tasks = {}; self.counter = 1
    def create_task(self, title, description, priority="Média"):
        if not title: raise ValueError("Título vazio")
        task = {"id": self.counter, "title": title, "description": description, "priority": priority, "status": "A Fazer"}
        self.tasks[self.counter] = task; self.counter += 1
        return task
    def read_tasks(self): return list(self.tasks.values())
    def update_task_status(self, task_id, new_status):
        if task_id in self.tasks: self.tasks[task_id]["status"] = new_status; return self.tasks[task_id]
        return None
    def delete_task(self, task_id): return self.tasks.pop(task_id, None)
