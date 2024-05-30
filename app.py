import streamlit as st
import pandas as pd
import io
import tasks
import validations
import hints

def show_instructions_and_task(level):
    st.title("Pandas Playground: Learn and Code!")
    st.info(
        """
        Welcome to the Pandas Playground! Improve your pandas skills by completing tasks and earning points.
        """
    )
    
    # Display the task for the current level
    task = tasks.get_task(level)
    st.write(f"**Level {level} Task**: {task}")

def execute_user_code(code, task_id):
    try:
        # Safe environment setup
        safe_globals = {"pd": pd}
        safe_locals = {}
        
        # Execute user code
        exec(code, safe_globals, safe_locals)
        
        # Run the validation check for the current task
        validation_check = validations.get_validation(task_id)
        message, success = validation_check(safe_locals)
        
        if success:
            st.session_state.points += 10
            st.success(f"Great job! You've earned 10 points. {message}")
            st.balloons()
            st.session_state.level += 1
        else:
            st.error(message)
            
        return safe_locals
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return ""

# Initialize session state variables
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'hints_used' not in st.session_state:
    st.session_state.hints_used = 0

# Display instructions and the task for the current level
show_instructions_and_task(st.session_state.level)

# User code input area
user_code = st.text_area("Your Code", height=200)

# Run code button
if st.button("Run Code"):
    if user_code:
        output = execute_user_code(user_code, st.session_state.level)
        st.subheader("Output")
        st.text(output)
    else:
        st.warning("Please enter some code to run.")

# Display hints based on user requests
if st.button("Get a Hint"):
    if 'hint_number' not in st.session_state:
        st.session_state.hint_number = 1
    else:
        st.session_state.hint_number += 1

    hint = hints.get_hint(st.session_state.level, st.session_state.hint_number)
    st.write(hint)

    # Deduct points for using a hint, with increasing cost for additional hints
    st.session_state.points -= st.session_state.hint_number
