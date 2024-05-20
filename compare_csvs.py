import pandas as pd
import os

# Load the CSV files into DataFrames
file1 = 'source1.csv'
file2 = 'source2.csv'

# Ensure the output directory exists
output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Strip leading/trailing spaces from column names
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Step 1: Map or Drop Columns
print("First CSV file columns:")
print(df1.columns.tolist())

print("\nSecond CSV file columns:")
print(df2.columns.tolist())

# Create a mapping dictionary
mapping = {}

for col in df2.columns:
    print(f"\nColumn in file 2: '{col}'")
    choice = input("Do you want to drop this column or map it to a column in file 1? (d/m): ").strip().lower()
    while choice not in ['d', 'm']:
        print("Invalid choice. Please enter 'd' to drop or 'm' to map.")
        choice = input("Do you want to drop this column or map it to a column in file 1? (d/m): ").strip().lower()
    
    if choice == 'm':
        target_col = input(f"Enter the column name from file 1 to map '{col}' to: ").strip()
        while target_col not in df1.columns:
            print(f"Error: '{target_col}' not found in the columns of file 1. Please enter a valid column name.")
            target_col = input(f"Enter the column name from file 1 to map '{col}' to: ").strip()
        mapping[col] = target_col
    else:
        mapping[col] = None

# Apply the mapping
df2_mapped = df2.rename(columns={k: v for k, v in mapping.items() if v is not None})
df2_mapped = df2_mapped[[v for v in mapping.values() if v is not None]]

# Update both DataFrames to have the same columns
common_columns = df1.columns.intersection(df2_mapped.columns)
df1_common = df1[common_columns]
df2_common = df2_mapped[common_columns]

# Save the updated CSV files
df1_common.to_csv(os.path.join(output_dir, 'updated_source1.csv'), index=False)
df2_common.to_csv(os.path.join(output_dir, 'updated_source2.csv'), index=False)

# Step 2: Create comparison files

# Find overlapping data
common_data = pd.merge(df1_common, df2_common, on=list(common_columns))

# Find data in file 2 but not in file 1
data_in_file2_not_in_file1 = df2_common[~df2_common.isin(df1_common)].dropna(how='all')

# Prompt for the column to check for missing data
while True:
    column_to_check = input("\nEnter the column name to check for missing data: ").strip()
    if column_to_check in df1.columns:
        break
    else:
        print(f"Error: '{column_to_check}' column not found in the first CSV file. Please enter a valid column name.")

# Find missing data based on the specified column
missing_data = df1_common[df1_common[column_to_check].isna()]

# Save the comparison files
common_data.to_csv(os.path.join(output_dir, 'common_data.csv'), index=False)
data_in_file2_not_in_file1.to_csv(os.path.join(output_dir, 'data_in_file2_not_in_file1.csv'), index=False)
missing_data.to_csv(os.path.join(output_dir, 'missing_data.csv'), index=False)

print("The comparison files have been saved to the 'data' directory.")
