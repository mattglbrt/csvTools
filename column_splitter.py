import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'source.csv'  # Replace with your actual file path
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: The file at path '{file_path}' was not found.")
    exit()

# Assuming the column with names is named 'Name', change if different
name_column = 'FNAME'  # Replace with the actual column name

# Check if the name column exists
if name_column not in df.columns:
    print(f"Error: The column '{name_column}' was not found in the CSV file.")
    exit()

# Split the 'Name' column into 'Last Name' and 'First Name' columns
def split_name(name):
    parts = name.split(', ')
    if len(parts) == 2:
        return parts
    else:
        return [name, '']  # Default to original name and empty first name if split fails

df[['Last Name', 'First Name']] = df[name_column].apply(split_name).tolist()

# Drop the original 'Name' column if no longer needed
df.drop(columns=[name_column], inplace=True)

# Save the updated DataFrame to a new CSV file
output_file_path = 'split_names.csv'  # Replace with your desired output file path
df.to_csv(output_file_path, index=False)

print(f"The updated CSV file has been saved to '{output_file_path}'")
