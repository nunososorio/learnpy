import streamlit as st
import pandas as pd
import io

def show_instructions_and_task(level):
    st.title("Pandas Playground: Learn and Code!")
    st.info(
        """
        Welcome to the Pandas Playground! Improve your pandas skills by completing tasks and earning points.
        """
    )
    
    # Define tasks for each level
    tasks = {
        1: 'Import the CSV "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv" file into a DataFrame using pd.read_csv().',
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

def execute_user_code(code, task_id):
    try:
        # Safe environment setup
        safe_globals = {"pd": pd}
        safe_locals = {}
        
        # Execute user code
        exec(code, safe_globals, safe_locals)
        
        if task_id == 1:
            if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
                st.session_state.points += 10
                st.success("Great job! You've earned 10 points.")
                st.balloons()
                st.session_state.level += 1
            else:
                st.error("The DataFrame is not correctly loaded.")
                
        elif task_id == 2:
            if "df" in safe_locals and hasattr(safe_locals["df"], 'head'):
                result = safe_locals["df"].head()
                expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv").head()
                if result.equals(expected):
                    st.session_state.points += 10
                    st.success("Great job! You've earned 10 points.")
                    st.balloons()
                    st.session_state.level += 1
                else:
                    st.error("The output isn't quite right.")
            else:
                st.error("The DataFrame is not correctly displayed.")
                
        elif task_id == 3:
            if "df" in safe_locals and hasattr(safe_locals["df"], 'dtypes'):
                result = safe_locals["df"].dtypes
                expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv").dtypes
                if result.equals(expected):
                    st.session_state.points += 10
                    st.success("Great job! You've earned 10 points.")
                    st.balloons()
                    st.session_state.level += 1
                else:
                    st.error("The output isn't quite right.")
            else:
                st.error("The DataFrame dtypes are not correctly displayed.")
                
        elif task_id == 4:
            if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
                expected_columns = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv").columns
                dropped_column = set(expected_columns) - set(safe_locals["df"].columns)
                if len(dropped_column) == 1:
                    st.session_state.points += 10
                    st.success("Great job! You've earned 10 points.")
                    st.balloons()
                    st.session_state.level += 1
                else:
                    st.error("The column was not dropped correctly.")
            else:
                st.error("The DataFrame is not correctly modified.")
                
        elif task_id == 5:
            if "df" in safe_locals and hasattr(safe_locals["df"], 'describe'):
                result = safe_locals["df"].describe()
                expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv").describe()
                if result.equals(expected):
                    st.session_state.points += 10
                    st.success("Great job! You've earned 10 points.")
                    st.balloons()
                    st.session_state.level += 1
                else:
                    st.error("The summary statistics are not correct.")
            else:
                st.error("The DataFrame summary statistics are not correctly calculated.")
                
        elif task_id == 6:
            if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
                # Assuming some filtering condition, here we use "species == 'setosa'"
                result = safe_locals["df"]
                expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
                expected = expected[expected["species"] == "setosa"]
                if result.equals(expected):
                    st.session_state.points += 10
                    st.success("Great job! You've earned 10 points.")
                    st.balloons()
                    st.session_state.level += 1
                else:
                    st.error("The DataFrame filtering is not correct.")
            else:
                st.error("The DataFrame is not correctly filtered.")
                
        elif task_id == 7:
            if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
                result = safe_locals["df"]
                expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
                expected = expected.groupby("species").mean()
                if result.equals(expected):
                    st.session_state.points += 10
                    st.success("Great job! You've earned 10 points.")
                    st.balloons()
                    st.session_state.level += 1
                else:
                    st.error("The DataFrame grouping and aggregation is not correct.")
            else:
                st.error("The DataFrame is not correctly grouped and aggregated.")
                
        elif task_id == 8:
            if "df1" in safe_locals and "df2" in safe_locals:
                result = safe_locals["df1"]
                expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
                merged_expected = expected.merge(expected, on="species")
                if result.equals(merged_expected):
                    st.session_state.points += 10
                    st.success("Great job! You've earned 10 points.")
                    st.balloons()
                    st.session_state.level += 1
                else:
                    st.error("The DataFrame merging is not correct.")
            else:
                st.error("The DataFrames are not correctly merged.")
                
        elif task_id == 9:
            if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
                result = safe_locals["df"]
                expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
                pivot_expected = expected.pivot_table(index='species', values='sepal_length', aggfunc='mean')
                if result.equals(pivot_expected):
                    st.session_state.points += 10
                    st.success("Great job! You've earned 10 points.")
                    st.balloons()
                    st.session_state.level += 1
                else:
                    st.error("The DataFrame pivot is not correct.")
            else:
                st.error("The DataFrame is not correctly pivoted.")
                
        elif task_id == 10:
            if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
                result = safe_locals["df"]
                expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
                if result.equals(expected):
                    st.session_state.points += 10
                    st.success("Great job! You've earned 10 points.")
                    st.balloons()
                    st.session_state.level += 1
                else:
                    st.error("The DataFrame saving is not correct.")
            else:
                st.error("The DataFrame is not correctly saved.")
                
        else:
            st.error("This task is not yet implemented for validation.")
        return safe_locals
    except Exception as e:
        st.error(f
