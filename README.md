# Todo App

A simple **Todo application** implemented in Python that allows users to manage tasks via **Command-Line Interface (CLI)**, **Graphical User Interface (GUI)**, or a **Web Interface** using Streamlit. The app stores todos in a text file (`todos.txt`) for persistence.

---

## Features

- Add, edit, complete, and view todos.
- CLI interface for terminal usage.
- GUI interface built with **PySimpleGUI**.
- Web interface using **Streamlit**.
- Todos are saved in a local file (`todos.txt`).

---

## Project Structure

├── cli.py # Command-line interface
├── gui.py # Graphical interface using PySimpleGUI
├── web.py # Web interface using Streamlit
├── functions.py # Core functions to read/write todos
├── todos.txt # File storing todo items
├── README.md


---

## Requirements

- Python 3.10+
- [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) (for GUI)
- [Streamlit](https://pypi.org/project/streamlit/) (for Web)

Install dependencies with:

```bash
pip install PySimpleGUI streamlit

Usage

1. CLI Interface
Run the terminal-based interface: python cli.py

Commands inside CLI:

add <todo> → Add a new todo.
show → Display all todos.
edit <number> → Edit a todo by its number.
complete <number> → Remove a todo by its number.
exit → Exit the app.

2. GUI Interface (PySimpleGUI)
Run the GUI version: python gui.py

Type a todo in the input box and click Add.
Select a todo and click Edit to modify it.
Select a todo and click Complete to remove it.
Click Exit to close the GUI.

3. Web Interface (Streamlit)
Run the web interface: streamlit run web.py

Access the app in your browser (default: http://localhost:8501).
Add todos via the input box.
Complete todos by checking the checkbox.
Todos automatically update in the todos.txt file.

Todos File

The application stores tasks in todos.txt. Example content:
Make pizza
Wash the car.
Help the neighbor.
Clean the bag.

How It Works

functions.py contains the main logic to read/write todos.
CLI, GUI, and Web interfaces use functions.py to interact with todos.
Todos are stored persistently in a plain text file (todos.txt).
