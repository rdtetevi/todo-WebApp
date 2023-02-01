import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    """
    the session_state is a dictionary whose
    key is related to the key of the object invoking
    it and the value the content of the object.
    for example the function add_todo which
    is an callback (onchange) to the text_input object
    allows the session_state to use the key of
    the text_input and thereafter its value.
    :return: list of todos.
    """
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")


#if i use session_state on checkboxes i notice that
#the keys are the texts written on each row and
#their values are booleans.
#if i have ticked a checkbox then the value will be TRUE.

for index, todo in enumerate(todos):

    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #if checkboxis checked
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new todos...",
              on_change=add_todo, key='new_todo')


