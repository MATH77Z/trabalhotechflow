import pytest
from src.task_manager import TaskManager

def test_task_flow():
    manager = TaskManager()
    task = manager.create_task("Entrega A", "Rota 1", "Alta")
    assert task["title"] == "Entrega A"
    assert task["priority"] == "Alta"
    assert manager.update_task_status(1, "Em Progresso")["status"] == "Em Progresso"
    manager.delete_task(1)
    assert len(manager.read_tasks()) == 0
