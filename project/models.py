from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any


VALID_PRIORITIES = {"low", "medium", "high"}


@dataclass(slots=True)
class Task:
    task_id: int
    title: str
    priority: str = "medium"
    completed: bool = False
    due_date: date | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed,
            "due_date": self.due_date.isoformat() if self.due_date else None,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "Task":
        due_date_raw = payload.get("due_date")
        return cls(
            task_id=int(payload["task_id"]),
            title=str(payload["title"]),
            priority=str(payload.get("priority", "medium")),
            completed=bool(payload.get("completed", False)),
            due_date=date.fromisoformat(due_date_raw) if due_date_raw else None,
        )
