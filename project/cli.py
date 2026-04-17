from __future__ import annotations

import argparse
from datetime import date

from project.manager import TaskManager
from project.storage import JSONStorage


def _parse_date(raw: str) -> date:
    try:
        return date.fromisoformat(raw)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Dates must be in YYYY-MM-DD format.") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="StudySprint task manager")
    parser.add_argument("--file", default="tasks.json", help="Path to task storage JSON file")

    subparsers = parser.add_subparsers(dest="command", required=True)

    add = subparsers.add_parser("add", help="Add a new task")
    add.add_argument("title", help="Task title")
    add.add_argument("--priority", default="medium", choices=["low", "medium", "high"])
    add.add_argument("--due", type=_parse_date, help="Due date in YYYY-MM-DD format")

    listing = subparsers.add_parser("list", help="List tasks")
    listing.add_argument("--status", default="all", choices=["all", "open", "done"])

    done = subparsers.add_parser("done", help="Mark a task as complete")
    done.add_argument("task_id", type=int)

    delete = subparsers.add_parser("delete", help="Delete a task")
    delete.add_argument("task_id", type=int)

    subparsers.add_parser("stats", help="Show task statistics")

    return parser


def run(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    manager = TaskManager(JSONStorage(args.file))

    try:
        if args.command == "add":
            task = manager.add_task(args.title, args.priority, args.due)
            print(f"Added task #{task.task_id}: {task.title}")
            return 0

        if args.command == "list":
            tasks = manager.list_tasks(args.status)
            if not tasks:
                print("No tasks found.")
                return 0

            for task in tasks:
                status = "✓" if task.completed else " "
                due = f" due={task.due_date.isoformat()}" if task.due_date else ""
                print(f"[{status}] #{task.task_id} {task.title} ({task.priority}){due}")
            return 0

        if args.command == "done":
            task = manager.complete_task(args.task_id)
            print(f"Completed task #{task.task_id}: {task.title}")
            return 0

        if args.command == "delete":
            task = manager.delete_task(args.task_id)
            print(f"Deleted task #{task.task_id}: {task.title}")
            return 0

        if args.command == "stats":
            stats = manager.stats()
            print(
                " | ".join(
                    [
                        f"Total={stats['total']}",
                        f"Open={stats['open']}",
                        f"Completed={stats['completed']}",
                        f"HighPriorityOpen={stats['high_priority_open']}",
                    ]
                )
            )
            return 0

        parser.error("Unknown command")
    except ValueError as error:
        print(f"Error: {error}")
        return 1

    return 0
