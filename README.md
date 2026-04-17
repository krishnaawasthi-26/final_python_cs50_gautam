# StudySprint CLI

StudySprint is a simple but production-style Python CLI project for managing personal tasks.

## Features
- Add tasks with optional due dates and priorities.
- List tasks with filters (`all`, `open`, `done`).
- Mark tasks complete.
- Delete tasks.
- View summary statistics.
- Persist data in a local JSON file.

## Project structure
- `main.py` — app entrypoint.
- `project/cli.py` — command-line interface.
- `project/manager.py` — business logic.
- `project/storage.py` — persistence layer.
- `project/models.py` — task model.
- `tests/test_manager.py` — automated tests.

## Requirements
- Python 3.10+

## Usage
Run commands from the repository root:

```bash
python main.py add "Finish CS50 project" --priority high --due 2026-04-30
python main.py list --status open
python main.py done 1
python main.py stats
```

By default, data is stored in `tasks.json` in the current working directory.

## Running tests
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
