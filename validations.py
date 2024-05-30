def get_validation(task_id):
    validations = {
        1: validate_task_1,
        # Add more validation checks for each task
    }
    return validations.get(task_id, lambda x: ("This task is not yet implemented for validation.", False))

def validate_task_1(locals):
    if "df" in locals and isinstance(locals["df"], pd.DataFrame):
        return ("", True)
    else:
        return ("The DataFrame is not correctly loaded.", False)
