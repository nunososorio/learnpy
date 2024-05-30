def get_task(level):
    tasks = {
        1: 'Import the CSV "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv" file into a DataFrame using pd.read_csv().',
        # Add more tasks for additional levels
    }
    return tasks.get(level, "No task for this level.")
