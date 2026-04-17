# StudySprint CLI

#### Video Demo: https://youtu.be/REPLACE_WITH_YOUR_VIDEO_ID

#### Description:

StudySprint CLI is my CS50P final project. It is a command-line study task manager designed for students who want a quick way to capture and track assignments, goals, and deadlines without leaving the terminal. I chose this project because I wanted to build something practical that I could realistically use every day while practicing core CS50P concepts such as functions, classes, modules, file I/O, error handling, and unit testing.

The basic idea is simple: users should be able to add tasks, list tasks, complete tasks, and delete tasks with clear commands. Even though the idea is simple, I focused on implementing it with a modular structure instead of putting everything in one file. That design decision helped me practice writing cleaner code with separate responsibilities. I also made sure tasks include useful details beyond just a title, because in real planning tools metadata matters a lot.

## Core features

The application supports these key features:

1. **Add tasks** with a title, priority, and optional due date.
2. **List tasks** in three modes: all tasks, open tasks, or completed tasks.
3. **Complete tasks** by task ID to mark progress.
4. **Delete tasks** by task ID to remove work that is no longer needed.
5. **View statistics** to get a snapshot of progress.

Each task includes:

- A numeric task ID.
- A title.
- A priority level (`low`, `medium`, or `high`).
- A completion flag.
- An optional due date.

This structure makes the project more realistic than a plain to-do list and allows simple prioritization. For example, if I have ten tasks but only two high-priority tasks still open, I can quickly focus on what matters most.

## Project architecture

I organized the project into multiple Python modules:

- `main.py` is the top-level program entrypoint for the CLI application.
- `project/cli.py` parses command-line arguments and handles user-facing command behavior.
- `project/manager.py` contains task management logic (adding, filtering, completing, deleting, and calculating stats).
- `project/storage.py` is responsible for persistence using JSON.
- `project/models.py` defines the `Task` model and related validation/constants.
- `project.py` contains top-level helper functions and a `main()` function to satisfy CS50P project requirements.

I intentionally separated **storage**, **business logic**, and **command parsing** to follow good software design habits. This also makes testing easier: I can test behavior in the manager layer without relying on manual input every time.

## Storage approach

Data is saved in a JSON file. I selected JSON because:

- It is human-readable.
- It maps naturally to Python dictionaries/lists.
- It keeps the project lightweight (no database dependency).

The `JSONStorage` class handles reading and writing. It converts task objects to dictionaries before saving and reconstructs them when loading. If no file exists yet, the app starts with an empty task list. This gives a smooth first-run experience and avoids crashes.

## Input validation and errors

Validation is implemented in multiple places:

- Empty task titles are rejected.
- Priority must be one of three valid values.
- Status filters are restricted to allowed options.
- Completing/deleting a missing task ID raises a clear error.
- In `project.py`, due date parsing validates `YYYY-MM-DD` format.

These checks make the tool more robust and user-friendly. Instead of failing silently or producing corrupt data, the program returns helpful error messages.

## Testing strategy

I included automated tests because testing is one of the most important parts of writing reliable software.

- `tests/test_manager.py` verifies manager-level behavior:
  - Add and list tasks.
  - Complete task changes status correctly.
  - Delete task removes the task.
  - Statistics calculations are accurate.
- `tests/test_project.py` verifies top-level functions in `project.py`:
  - Due date parsing for valid and invalid input.
  - Priority normalization and validation.
  - Task summary creation and title validation.

The tests use temporary files where needed so they do not interfere with real data. Running tests gives confidence that refactoring or adding features will not break existing behavior.

## Design trade-offs

I made a few deliberate trade-offs:

1. **Simple file storage over database**: keeps setup easy and suitable for a classroom project.
2. **CLI over GUI**: focuses on Python fundamentals and speed of interaction.
3. **Small feature set with clean structure**: I prioritized maintainability and clarity over trying to build every possible feature.

Possible future improvements include recurring tasks, task tags, search, sorting by due date, and export/import options.

## What I learned

Building this project helped me practice:

- Designing and organizing a medium-sized Python project.
- Writing reusable classes and methods.
- Validating user input and handling exceptions cleanly.
- Separating concerns between interface, logic, and persistence.
- Writing unit tests that check behavior and edge cases.

Most importantly, I learned how much easier code becomes to maintain when responsibilities are clearly separated. This project reflects not only CS50P syntax knowledge but also practical software engineering habits.

Overall, StudySprint CLI is a focused, realistic final project that demonstrates Python programming skills through a useful productivity tool.
