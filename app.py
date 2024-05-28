import streamlit as st
import pandas as pd
import io

# Function to execute the user's code
def execute_user_code(code):
    try:
        # Redirect stdout to capture print statements
        buffer = io.StringIO()
        exec(code, {'pd': pd, 'output': buffer})
        result = buffer.getvalue()
    except Exception as e:
        result = str(e)
    return result

# Streamlit App
st.title("Python and Pandas Live Code Playground")

# Progress tracking
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'points' not in st.session_state:
    st.session_state.points = 0

# Display current level and points
st.sidebar.title("Your Progress")
st.sidebar.write(f"Level: {st.session_state.level}")
st.sidebar.write(f"Points: {st.session_state.points}")

# Code input area
st.write("Enter your Python code using pandas below and see the result in real-time.")
user_code = st.text_area("Your Code", height=200)

# Execute the code when the button is pressed
if st.button("Run Code"):
    if user_code:
        output = execute_user_code(user_code)
        st.subheader("Output")
        st.text(output)

        # Check if the user has successfully completed the task
        if 'import pandas as pd' in user_code:
            st.session_state.points += 10
            st.success("Task completed! You've earned 10 points.")
            st.balloons()

            # Progress to the next level
            st.session_state.level += 1
    else:
        st.warning("Please enter some code to run.")

# Example code snippets to help users
st.sidebar.title("Examples")
example1 = '''
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

# Display the DataFrame
output.write(df)
'''

st.sidebar.subheader("Example 1: Create and Display DataFrame")
st.sidebar.code(example1, language='python')

if st.sidebar.button("Load Example 1"):
    user_code = example1
    st.text_area("Your Code", value=user_code, height=200)

example2 = '''
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

# Display basic statistics
output.write(df.describe())
'''

st.sidebar.subheader("Example 2: DataFrame Statistics")
st.sidebar.code(example2, language='python')

if st.sidebar.button("Load Example 2"):
    user_code = example2
    st.text_area("Your Code", value=user_code, height=200)

# Note: Users need to use `output.write` to display results in the app
