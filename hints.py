# hints.py
hints = {
    1: {
        1: "Start by importing pandas as pd.",
        2: "Use the pd.read_csv() function to read the CSV file.",
        3: "Make sure to pass the correct URL of the CSV file to the function.",
        4: "Solution: df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')"
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
        4: "Solution: df.drop('sepal_width', axis=1, inplace=True)"
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
        4: "Solution: filtered_df = df[df['sepal_length'] > 5.0]"
    },
    7: {
        1: "Grouping data involves selecting a column to group by.",
        2: "After grouping, you can apply an aggregate function like mean or sum.",
        3: "Call .groupby() and then an aggregate function on the result.",
        4: "Solution: df.groupby('species').mean()"
    },
    8: {
        1: "Merging combines two DataFrames based on a common column.",
        2: "Decide on the type of join you want: inner, outer, left, or right.",
        3: "Use the .merge() method with the 'on' parameter specifying the common column.",
        4: "Solution: merged_df = df1.merge(df2, on='species')"
    },
    9: {
        1: "Pivoting restructures data based on column values.",
        2: "Choose which column will be the new rows (index), columns, and values.",
        3: "Use the .pivot_table() method with the appropriate parameters.",
        4: "Solution: df.pivot_table(values='sepal_length', index='species', columns='petal_width')"
    },
    10: {
        1: "Saving to CSV is useful for data persistence.",
        2: "The .to_csv() method allows you to specify a file name.",
        3: "You can also choose whether to include the index with the 'index' parameter.",
        4: "Solution: df.to_csv('new_file.csv', index=False)"
    },
    # Add more hints for each level
}
