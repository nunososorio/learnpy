import streamlit as st
import pandas as pd
import io

# Function to display the game instructions
def show_instructions():
    st.title("Welcome to the Pandas Playground!")
    st.info(
        """
        This is a live code environment where you can learn pandas and earn points by solving tasks.
        - **Write Code**: Type your Python code using pandas in the code box.
        - **Run Code**: Click 'Run Code' to execute and see the output.
        - **Earn Points**: Solve tasks correctly to earn points.
        - **Use Hints**: Need help? Click 'Get a Hint' (costs points).
        - **Learn**: Check 'Examples' for helpful code snippets.
        - **Import Data**: Practice with datasets provided.
        - **Have Fun**: Enjoy learning and challenge yourself!
        """
    )

# Function to safely execute user's code and check task completion
def execute_user_code(code, task_id):
    # Define expected outputs for each task
    expected_outputs = {
        1: "Expected output for task 1",
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

# Display instructions and progress
show_instructions()
st.sidebar.title("Your Progress")
st.sidebar.write(f"Level: {st.session_state.level}")
st.sidebar.write(f"Points: {st.session_state.points}")
st.sidebar.write(f"Hints Used: {st.session_state.hints_used}")

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

# Hint system
def get_hint(level):
    hints = {
        1: "Use pd.read_csv() to read a CSV file into a DataFrame.",
        # Add more hints for each level
    }
    return hints.get(level, "No hint for this level.")

if st.sidebar.button("Get a Hint"):
    hint = get_hint(st.session_state.level)
    st.sidebar.write(hint)
    st.session_state.hints_used += 1
    st.session_state.points -= 1  # Deduct points for using a hint

# Dataset import challenge
def load_random_dataset():
    datasets = {
        1: ('Iris Dataset', 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'),
        # Add more datasets with increasing complexity
    }
    return datasets.get(st.session_state.level, (None, None))

dataset_info = load_random_dataset()
if dataset_info[0]:
    st.sidebar.write(f"Dataset for Level {st.session_state.level}: {dataset_info[0]}")
    st.sidebar.write("Use the URL below to import the dataset:")
    st.sidebar.write(dataset_info[1])

# Example code snippets
st.sidebar.title("Examples")
example1 = '''
import pandas as pd

# Importing a dataset from a URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Display the DataFrame
print(df.head())
'''

st.sidebar.subheader("Example 1: Import and Display Dataset")
st.sidebar.code(example1, language='python')

if st.sidebar.button("Load Example 1"):
    st.text_area("Your Code", value=example1, height=200)
