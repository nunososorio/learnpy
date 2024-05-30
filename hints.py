def get_hint(level, hint_number):
    hints = {
        1: {
            1: "Start by importing pandas as pd.",
            # Add more hints for each level
        },
        # Add more hints for each level
    }
    level_hints = hints.get(level, {})
    return level_hints.get(hint_number, "No more hints available.")
