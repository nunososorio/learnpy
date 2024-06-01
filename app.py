import streamlit as st
import pandas as pd
import random

# Gamification class to learn pandas concepts
class PandasGamification:
    def __init__(self):
        self.tasks = {
            'function': 'Use the pd.read_csv() function to read the "iris.csv" file into a DataFrame.',
            'method': 'Use the .head() method to display the first 5 rows of the DataFrame.',
            'attribute': 'Access the .shape attribute to get the dimensions of the DataFrame.'
        }
        self.answers = {
            'function': lambda df: isinstance(df, pd.DataFrame),
            'method': lambda result: isinstance(result, pd.DataFrame) and len(result) == 5,
            'attribute': lambda result: isinstance(result, tuple) and len(result) == 2
        }

    def get_random_task(self):
        self.current_task_key = random.choice(list(self.tasks.keys()))
        return self.current_task_key, self.tasks[self.current_task_key]

    def check_answer(self, key, result):
        if self.answerskey:
            return "Correct! You've earned a point.", True
        else:
            return "Incorrect. Try again!", False

# Initialize session state variables
if 'game' not in st.session_state:
    st.session_state.game = PandasGamification()
    st.session_state.score = 0
    st.session_state.task_key, st.session_state.task_description = st.session_state.game.get_random_task()

# Start the Streamlit app
st.title("Pandas Concepts Game")

# Display the task
st.subheader("Task")
st.write(st.session_state.task_description)

# User code input area
user_code = st.text_area("Your Code", height=200)

# Run code button
if st.button("Check Answer"):
    try:
        # Execute user code
        exec(user_code)
        # Assume the result is stored in a variable named 'result'
        message, success = st.session_state.game.check_answer(st.session_state.task_key, locals().get('result'))
        if success:
            st.session_state.score += 1
            st.success(message)
            # Get a new task
            st.session_state.task_key, st.session_state.task_description = st.session_state.game.get_random_task()
        else:
            st.error(message)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Show current score
st.sidebar.header("Scoreboard")
st.sidebar.write(f"Score: {st.session_state.score}")

# Reset game button
if st.sidebar.button("Reset Game"):
    st.session_state.game = PandasGamification()
    st.session_state.score = 0
    st.session_state.task_key, st.session_state.task_description = st.session_state.game.get_random_task()
    st.experimental_rerun()
