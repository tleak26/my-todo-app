# Todo App

A simple to-do list web app built with **Streamlit**. Add todos via a text input and check them off to remove them; everything is persisted to a local `todos.txt` file. Configured to deploy directly to Streamlit Community Cloud or run in a GitHub Codespace.

**Live demo:** https://tleak26-my-todo-app-web-kqocnt.streamlit.app/

This is the deployed web version of [todo-app](https://github.com/tleak26/todo-app), which also has CLI and desktop GUI interfaces built on the same core logic.

---

## Project Structure

```
web.py           # Streamlit web interface
functions.py      # Core functions to read/write todos
todos.txt          # File storing todo items
Procfile           # Heroku-style start command
setup.sh           # Streamlit config for cloud deployment
.devcontainer/      # GitHub Codespaces configuration
```

---

## Running locally

```bash
pip install -r requirements.txt
streamlit run web.py
```

Access the app in your browser (default: http://localhost:8501).

## How it works

- `functions.py` handles reading and writing todos to `todos.txt`.
- `web.py` renders the Streamlit UI and calls into `functions.py`.
- Todos are stored as plain lines in `todos.txt`.
