from __future__ import annotations

from datetime import date

from project.models import Task, VALID_PRIORITIES
from project.storage import JSONStorage


class TaskManager:
    def __init__(self, storage: JSONStorage) -> None:
        self._storage = storage
        self._tasks = self._storage.load()

    def add_task(self, title: str, priority: str = "medium", due_date: date | None = None) -> Task:
        cleaned = title.strip()
        if not cleaned:
            raise ValueError("Task title cannot be empty.")

        priority = priority.lower()
        if priority not in VALID_PRIORITIES:
            valid = ", ".join(sorted(VALID_PRIORITIES))
            raise ValueError(f"Invalid priority '{priority}'. Use one of: {valid}.")

        next_id = max((task.task_id for task in self._tasks), default=0) + 1
        task = Task(task_id=next_id, title=cleaned, priority=priority, due_date=due_date)
        self._tasks.append(task)
        self._storage.save(self._tasks)
        return task

    def list_tasks(self, status: str = "all") -> list[Task]:
        normalized = status.lower()
        if normalized == "all":
            return list(self._tasks)
        if normalized == "open":
            return [task for task in self._tasks if not task.completed]
        if normalized == "done":
            return [task for task in self._tasks if task.completed]

        raise ValueError("Status must be one of: all, open, done.")

    def complete_task(self, task_id: int) -> Task:
        task = self._get_task(task_id)
        task.completed = True
        self._storage.save(self._tasks)
        return task

    def delete_task(self, task_id: int) -> Task:
        task = self._get_task(task_id)
        self._tasks = [item for item in self._tasks if item.task_id != task_id]
        self._storage.save(self._tasks)
        return task

    def stats(self) -> dict[str, int]:
        total = len(self._tasks)
        completed = sum(task.completed for task in self._tasks)
        return {
            "total": total,
            "completed": completed,
            "open": total - completed,
            "high_priority_open": sum(
                (task.priority == "high") and (not task.completed)
                for task in self._tasks
            ),
        }

    def _get_task(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.task_id == task_id:
                return task
        raise ValueError(f"Task #{task_id} not found.")
