def validate_task(code, task_id):
    safe_globals = {"pd": pd}
    safe_locals = {}
    exec(code, safe_globals, safe_locals)
    
    if task_id == 1:
        if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
            return True
        else:
            return False
                
    elif task_id == 2:
        if "df" in safe_locals and hasattr(safe_locals["df"], 'head'):
            result = safe_locals["df"].head()
            expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv").head()
            if result.equals(expected):
                return True
            else:
                return False
        else:
            return False
                
    elif task_id == 3:
        if "df" in safe_locals and hasattr(safe_locals["df"], 'dtypes'):
            result = safe_locals["df"].dtypes
            expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv").dtypes
            if result.equals(expected):
                return True
            else:
                return False
        else:
            return False
                
    elif task_id == 4:
        if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
            expected_columns = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv").columns
            dropped_column = set(expected_columns) - set(safe_locals["df"].columns)
            if len(dropped_column) == 1:
                return True
            else:
                return False
        else:
            return False
                
    elif task_id == 5:
        if "df" in safe_locals and hasattr(safe_locals["df"], 'describe'):
            result = safe_locals["df"].describe()
            expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv").describe()
            if result.equals(expected):
                return True
            else:
                return False
        else:
            return False
                
    elif task_id == 6:
        if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
            result = safe_locals["df"]
            expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
            expected = expected[expected["species"] == "setosa"]
            if result.equals(expected):
                return True
            else:
                return False
        else:
            return False
                
    elif task_id == 7:
        if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
            result = safe_locals["df"]
            expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
            expected = expected.groupby("species").mean()
            if result.equals(expected):
                return True
            else:
                return False
        else:
            return False
                
    elif task_id == 8:
        if "df1" in safe_locals and "df2" in safe_locals:
            result = safe_locals["df1"]
            expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
            merged_expected = expected.merge(expected, on="species")
            if result.equals(merged_expected):
                return True
            else:
                return False
        else:
            return False
                
    elif task_id == 9:
        if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
            result = safe_locals["df"]
            expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
            pivot_expected = expected.pivot_table(index='species', values='sepal_length', aggfunc='mean')
            if result.equals(pivot_expected):
                return True
            else:
                return False
        else:
            return False
                
    elif task_id == 10:
        if "df" in safe_locals and isinstance(safe_locals["df"], pd.DataFrame):
            result = safe_locals["df"]
            expected = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
            if result.equals(expected):
                return True
            else:
                return False
        else:
            return False
                
    else:
        return False
