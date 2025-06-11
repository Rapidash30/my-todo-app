import streamlit as st
import functions

contents = functions.read()
def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    contents.append(todo)
    functions.write(contents)


contents = functions.read()

st.title("Hello World!")
st.subheader("How are you?")
st.write("Goodbye!")

for index, todo in enumerate(contents):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        contents.pop(index)
        functions.write(contents)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = " ", placeholder = "Enter task here.",
             on_change = add_todo, key = "new_todo" )


print("hi")
st.session_state
