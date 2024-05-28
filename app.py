import streamlit as st
import pandas as pd
import io

# Function to display the game instructions
def show_instructions():
    st.sidebar.title("How to Play")
    st.sidebar.info(
        """
        Welcome to the Python and Pandas Live Code Playground! Here's how you can learn and earn points:
        
        1. **Write Code**: In the code area, type your Python code using pandas to solve the given tasks.
        2. **Run Code**: Press the 'Run Code' button to execute your code and see the output.
        3. **Earn Points**: Complete tasks correctly to earn points and progress through levels.
        4. **Use Hints**: Stuck? Use the 'Get a Hint' button for help, but beware, it costs points!
        5. **Learn**: Check the 'Examples' section for code snippets that can help you learn pandas functions.
        6. **Import Data**: Use the provided dataset URLs to practice importing and analyzing data.
        7. **Have Fun**: Enjoy the process of learning and challenge yourself to improve!
        
        Ready to start coding? Enter your code in the text area and hit 'Run Code' to begin!
        """
    )

# Call the function to display the instructions
show_instructions()


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
if 'hints_used' not in st.session_state:
    st.session_state.hints_used = 0

# Display current level, points, and hints used
st.sidebar.title("Your Progress")
st.sidebar.write(f"Level: {st.session_state.level}")
st.sidebar.write(f"Points: {st.session_state.points}")
st.sidebar.write(f"Hints Used: {st.session_state.hints_used}")

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

# Hint system
def get_hint(level):
    hints = {
        1: "Remember to import pandas as pd to use the library.",
        2: "Use pd.read_csv() to import data from a CSV file.",
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
        2: ('Boston Housing Dataset', 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'),
        # Add more datasets with increasing complexity
    }
    level_dataset = datasets.get(st.session_state.level)
    if level_dataset:
        st.sidebar.write(f"Dataset for Level {st.session_state.level}: {level_dataset[0]}")
        return level_dataset[1]
    else:
        return None

dataset_url = load_random_dataset()
if dataset_url:
    st.sidebar.write("Use the URL below to import the dataset with pandas:")
    st.sidebar.write(dataset_url)

# Example code snippets to help users
st.sidebar.title("Examples")
example1 = '''
import pandas as pd

# Importing a dataset from a URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Display the DataFrame
output.write(df)
'''

st.sidebar.subheader("Example 1: Import and Display Dataset")
st.sidebar.code(example1, language='python')

if st.sidebar.button("Load Example 1"):
    user_code = example1
    st.text_area("Your Code", value=user_code, height=200)

# Note: Users need to use `output.write` to display results in the app
