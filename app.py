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
# Hint System
def get_advanced_hint(level, hint_number):
    # Dictionary of hints for each level
    hints = {
        1: {
            1: "Start by importing pandas as pd.",
            2: "Use the pd.read_csv() function to read the CSV file.",
            3: "Make sure to pass the correct URL of the CSV file to the function.",
            4: "Solution: df = pd.read_csv('your_file.csv')"
        },
        2: {
            1: "Use the DataFrame variable to call methods.",
            2: "The .head() method displays the first few rows of the DataFrame.",
            3: "You don't need to pass any arguments if you just want to see the first 5 rows.",
            4: "Solution: df.head()"
        },
        3: {
            1: "Each column in a DataFrame has a data type.",
            2: "Use the .dtypes attribute to see the data types.",
            3: "Remember, it's an attribute, not a method, so you don't need parentheses.",
            4: "Solution: df.dtypes"
        },
        4: {
            1: "To drop a column, you need to specify the column name.",
            2: "The .drop() method requires the 'axis' parameter set to 1 for columns.",
            3: "You can use inplace=True to modify the DataFrame in place.",
            4: "Solution: df.drop('column_name', axis=1, inplace=True)"
        },
        5: {
            1: "Summary statistics include count, mean, std, min, and more.",
            2: "The .describe() method provides these statistics for numerical columns.",
            3: "Just call the method on your DataFrame to see the statistics.",
            4: "Solution: df.describe()"
        },
        6: {
            1: "Boolean indexing allows you to filter rows based on a condition.",
            2: "Create a condition that evaluates to True or False for each row.",
            3: "Use this condition to index the DataFrame and select rows.",
            4: "Solution: filtered_df = df[df['column'] > value]"
        },
        7: {
            1: "Grouping data involves selecting a column to group by.",
            2: "After grouping, you can apply an aggregate function like mean or sum.",
            3: "Call .groupby() and then an aggregate function on the result.",
            4: "Solution: df.groupby('column').mean()"
        },
        8: {
            1: "Merging combines two DataFrames based on a common column.",
            2: "Decide on the type of join you want: inner, outer, left, or right.",
            3: "Use the .merge() method with the 'on' parameter specifying the common column.",
            4: "Solution: merged_df = df1.merge(df2, on='common_column')"
        },
        9: {
            1: "Pivoting restructures data based on column values.",
            2: "Choose which column will be the new rows (index), columns, and values.",
            3: "Use the .pivot_table() method with the appropriate parameters.",
            4: "Solution: df.pivot_table(values='values_column', index='rows_column', columns='columns_column')"
        },
        10: {
            1: "Saving to CSV is useful for data persistence.",
            2: "The .to_csv() method allows you to specify a file name.",
            3: "You can also choose whether to include the index with the 'index' parameter.",
            4: "Solution: df.to_csv('new_file.csv', index=False)"
        },
        # Add more hints for each level
    }
    
    # Retrieve the specific hint for the level and hint number
    level_hints = hints.get(level, {})
    return level_hints.get(hint_number, "No more hints available.")

# Display hints based on user requests
if st.sidebar.button("Get a Hint"):
    if 'hint_number' not in st.session_state:
        st.session_state.hint_number = 1
    else:
        st.session_state.hint_number += 1

    hint = get_advanced_hint(st.session_state.level, st.session_state.hint_number)
    st.sidebar.write(hint)

    # Deduct points for using a hint, with increasing cost for additional hints
    st.session_state.points -= st.session_state.hint_number
