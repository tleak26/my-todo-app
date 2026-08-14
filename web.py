import streamlit as st
import functions

st.set_page_config(page_title="My Todo App", page_icon="✅", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}
.app-header {
    text-align: center;
    padding: 1rem 0 0.5rem;
}
.app-header h1 {
    font-family: 'Poppins', sans-serif !important;
    font-weight: 700;
    margin-bottom: 0.2rem;
}
.app-header p {
    color: #8b8fa3;
    margin-bottom: 0;
}
.todo-counter {
    text-align: center;
    color: #8b8fa3;
    font-size: 0.95rem;
    margin-bottom: 1rem;
}
div[data-testid="stCheckbox"] {
    background-color: rgba(120, 120, 140, 0.08);
    border-radius: 10px;
    padding: 0.6rem 0.9rem;
    margin-bottom: 0.5rem;
    transition: background-color 0.15s ease;
}
div[data-testid="stCheckbox"]:hover {
    background-color: rgba(120, 120, 140, 0.16);
}
.empty-state {
    text-align: center;
    color: #8b8fa3;
    padding: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"].strip()
    if new_todo:
        todos.append(new_todo + "\n")
        functions.write_todos(todos)


st.markdown("""
<div class="app-header">
    <h1>✅ My Todo App</h1>
    <p>Keep track of what needs to get done.</p>
</div>
""", unsafe_allow_html=True)

remaining = len(todos)
if remaining > 0:
    st.markdown(
        f'<p class="todo-counter">{remaining} task{"s" if remaining != 1 else ""} remaining</p>',
        unsafe_allow_html=True,
    )

if not todos:
    st.markdown(
        '<div class="empty-state">🎉 Nothing on your list — add a task below to get started.</div>',
        unsafe_allow_html=True,
    )
else:
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            st.rerun()

st.text_input(label="New todo", placeholder="Add new todo and press Enter...",
              on_change=add_todo, key='new_todo', label_visibility="collapsed")
