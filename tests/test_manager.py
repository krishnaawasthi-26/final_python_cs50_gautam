from __future__ import annotations

import tempfile
import unittest
from datetime import date

from project.manager import TaskManager
from project.storage import JSONStorage


class TaskManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.storage_path = f"{self.tempdir.name}/tasks.json"
        self.manager = TaskManager(JSONStorage(self.storage_path))

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_add_and_list_task(self) -> None:
        task = self.manager.add_task("Build final project", priority="high", due_date=date(2026, 5, 1))

        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Build final project")

        open_tasks = self.manager.list_tasks("open")
        self.assertEqual(len(open_tasks), 1)
        self.assertEqual(open_tasks[0].priority, "high")

    def test_complete_task_changes_status(self) -> None:
        task = self.manager.add_task("Write tests")
        self.manager.complete_task(task.task_id)

        done_tasks = self.manager.list_tasks("done")
        self.assertEqual(len(done_tasks), 1)
        self.assertTrue(done_tasks[0].completed)

    def test_delete_task_removes_it(self) -> None:
        task = self.manager.add_task("Delete me")
        self.manager.delete_task(task.task_id)

        self.assertEqual(self.manager.list_tasks("all"), [])

    def test_stats_counts_high_priority_open(self) -> None:
        self.manager.add_task("Open high", priority="high")
        self.manager.add_task("Open low", priority="low")
        done_task = self.manager.add_task("Done high", priority="high")
        self.manager.complete_task(done_task.task_id)

        stats = self.manager.stats()

        self.assertEqual(stats["total"], 3)
        self.assertEqual(stats["completed"], 1)
        self.assertEqual(stats["open"], 2)
        self.assertEqual(stats["high_priority_open"], 1)


if __name__ == "__main__":
    unittest.main()
