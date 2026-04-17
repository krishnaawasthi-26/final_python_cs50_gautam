# StudySprint CLI
#### Video Demo:  https://youtu.be/REPLACE_WITH_YOUR_VIDEO_ID
#### Description:
StudySprint CLI is my CS50P final project, a command-line task manager written in Python. The goal of this project is to help a student or self-learner quickly organize study work from the terminal without needing a full graphical app. I focused on making the project simple to use while still applying clean software structure and testable design.

The application allows users to create tasks, mark tasks as complete, delete tasks, and list tasks by status. Each task supports useful metadata such as title, priority, due date, and completion state. This makes it easy to separate urgent work from low-priority items and to track progress over time. A separate summary command prints quick statistics so users can immediately see how many tasks are open or done.

I organized the code into multiple modules to keep responsibilities clear. The CLI layer in `project/cli.py` handles command parsing and user interaction. The manager layer in `project/manager.py` contains business logic for adding, updating, filtering, and deleting tasks. The storage layer in `project/storage.py` handles saving and loading JSON data from disk. The task model in `project/models.py` defines task structure and serialization behavior. The `main.py` file acts as the entrypoint and connects all parts together.

For testing, I included unit tests in `tests/test_manager.py` that validate core behaviors from the manager layer. These tests confirm that task creation, status updates, deletion, and filtering logic work correctly. By testing logic in isolation, I can confidently refactor internal code while preserving expected behavior.

This project demonstrates practical Python skills from CS50P: functions, classes, modules, file I/O, exception handling, command-line arguments, and automated testing. It also reflects software-engineering habits such as separation of concerns, reusable components, and maintainable project layout.
