def get_task(level):
    tasks = {
        1: 'Import the CSV "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv" file into a DataFrame using pd.read_csv().',
        2: "Display the first 5 rows of the DataFrame using .head().",
        3: "Display the data types of each column using .dtypes.",
        4: "Drop a column from the DataFrame using .drop().",
        5: "Calculate summary statistics using .describe().",
        6: "Filter the DataFrame to include only ‘species’ equal to ‘setosa’.",
        7: "Group the data and calculate aggregates using .groupby().",
        8: "Merge two DataFrames using .merge().",
        9: "Pivot the data using .pivot_table().",
        10: "Save the DataFrame to a new CSV file using .to_csv().",
        # Add more tasks for additional levels
    }
    return tasks.get(level, "No task for this level.")
