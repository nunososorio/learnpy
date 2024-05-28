import streamlit as st
import pandas as pd
import io

# Function to display the game instructions and the task for the current level
def show_instructions_and_task(level):
    st.title("Pandas Playground: Learn and Code!")
    st.info(
        """
        Welcome to the Pandas Playground! Improve your pandas skills by completing tasks and earning points.
        """
    )
    
    # Define tasks for each level
    tasks = {
        1: "Import a CSV file into a DataFrame using pd.read_csv().",
        2: "Display the first 5 rows of the DataFrame using .head().",
        3: "Display the data types of each column using .dtypes.",
        4: "Drop a column from the DataFrame using .drop().",
        5: "Calculate summary statistics using .describe().",
        6: "Filter the DataFrame based on a condition using boolean indexing.",
        7: "Group the data and calculate aggregates using .groupby().",
        8: "Merge two DataFrames using .merge().",
        9: "Pivot the data using .pivot_table().",
        10: "Save the DataFrame to a new CSV file using .to_csv().",
        # Add more tasks for additional levels
    }
    
    # Display the task for the current level
    task = tasks.get(level, "No task for this level.")
    st.write(f"**Level {level} Task**: {task}")

# Function to safely execute user's code and check task completion
def execute_user_code(code, task_id):
    # Define expected outputs for each task
    expected_outputs = {
        1: "DataFrame loaded from CSV",
        2: "First 5 rows of DataFrame",
        3: "Data types of each column",
        4: "DataFrame with a column dropped",
        5: "Summary statistics of DataFrame",
        6: "Filtered DataFrame",
        7: "Aggregated data using groupby",
        8: "Merged DataFrame",
        9: "Pivoted DataFrame",
        10: "DataFrame saved to CSV",
        # Define more expected outputs for additional tasks
    }
    
    try:
        # Safe environment setup
        safe_globals = {"pd": pd}
        safe_locals = {"output": io.StringIO()}
        
        # Execute user code
        exec(code, safe_globals, safe_locals)
        result = safe_locals["output"].getvalue()
        
        # Validate task completion
        if result.strip() == expected_outputs.get(task_id, ""):
            st.session_state.points += 10
            st.success("Great job! You've earned 10 points.")
            st.balloons()
            st.session_state.level += 1
        else:
            st.error("Try again, the output isn't quite right.")
        return result
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
