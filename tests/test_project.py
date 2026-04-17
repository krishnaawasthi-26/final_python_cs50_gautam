from __future__ import annotations

from datetime import date

import pytest

from project import normalize_priority, parse_due_date, task_summary


def test_parse_due_date_valid() -> None:
    assert parse_due_date("2026-05-01") == date(2026, 5, 1)


def test_parse_due_date_invalid() -> None:
    with pytest.raises(ValueError):
        parse_due_date("05/01/2026")


def test_normalize_priority_valid() -> None:
    assert normalize_priority(" HIGH ") == "high"


def test_normalize_priority_invalid() -> None:
    with pytest.raises(ValueError):
        normalize_priority("urgent")


def test_task_summary() -> None:
    summary = task_summary("Read chapter", "medium", date(2026, 6, 10))
    assert summary == "Read chapter | priority=medium | due=2026-06-10"


def test_task_summary_empty_title() -> None:
    with pytest.raises(ValueError):
        task_summary("   ", "low", date(2026, 6, 10))
