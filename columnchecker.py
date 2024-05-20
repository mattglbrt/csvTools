import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'source.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# List the columns in the CSV file
print("Available columns in the CSV file:")
print(df.columns.tolist())

# Ask the user to select a column to check for missing data
column_to_check = input("Enter the column name to check for missing data: ").strip()

# Ensure the selected column exists
if column_to_check not in df.columns:
    print(f"Error: The column '{column_to_check}' was not found in the CSV file.")
    exit()

# Create a new DataFrame with rows missing data in the selected column
missing_data_df = df[df[column_to_check].isna() | (df[column_to_check] == '')]

# Define the output file path
output_file_path = 'missing_data_entries.csv'  # Replace with your desired output file path

# Save the new DataFrame to a CSV file
missing_data_df.to_csv(output_file_path, index=False)

print(f"The new CSV file with missing data entries has been saved to '{output_file_path}'")
