import os
import json

# Define the file path (**
FILE_PATH = "src/data/models.py"

def fix_calendar_date(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
      content = f.read()

    # Replace missing 'calendar_date' with "NA"
    fixed_content = content.replace("''calendar_date'': None", "''calendar_date'': 'N/A'")

    if fixed_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(fixed_content)
        print("😵 Fixed missing 'calendar_date' values.")


if __name__ == "__main__":
    if os.path.exists(FILE_PATH):
        fix_calendar_date(FILE_PATH)
    else:
        print("✩ File not found: ",FILE_PATH)
