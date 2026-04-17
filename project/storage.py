from __future__ import annotations

import json
from pathlib import Path

from project.models import Task


class JSONStorage:
    def __init__(self, file_path: str = "tasks.json") -> None:
        self._path = Path(file_path)

    def load(self) -> list[Task]:
        if not self._path.exists():
            return []

        raw = json.loads(self._path.read_text(encoding="utf-8"))
        return [Task.from_dict(item) for item in raw]

    def save(self, tasks: list[Task]) -> None:
        serialized = [task.to_dict() for task in tasks]
        self._path.write_text(
            json.dumps(serialized, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
