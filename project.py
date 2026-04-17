from __future__ import annotations

from datetime import date


def parse_due_date(value: str) -> date:
    """Parse a due date in YYYY-MM-DD format."""
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("Due date must be in YYYY-MM-DD format.") from exc


def normalize_priority(value: str) -> str:
    """Normalize and validate task priority."""
    priority = value.strip().lower()
    valid = {"low", "medium", "high"}
    if priority not in valid:
        raise ValueError("Priority must be one of: low, medium, high.")
    return priority


def task_summary(title: str, priority: str, due: date) -> str:
    """Build a display summary for one task."""
    cleaned_title = title.strip()
    if not cleaned_title:
        raise ValueError("Title cannot be empty.")

    normalized = normalize_priority(priority)
    return f"{cleaned_title} | priority={normalized} | due={due.isoformat()}"


def main() -> None:
    """Simple interactive entrypoint for local manual testing."""
    title = input("Title: ").strip()
    priority = input("Priority (low/medium/high): ").strip()
    due_input = input("Due date (YYYY-MM-DD): ").strip()

    due = parse_due_date(due_input)
    print(task_summary(title, priority, due))


if __name__ == "__main__":
    main()
