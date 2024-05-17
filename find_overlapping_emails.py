import pandas as pd

# Load the CSV files into DataFrames
file1 = 'acton.csv'
file2 = 'source.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Strip leading/trailing spaces from column names
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Print the columns of each dataframe
print("First CSV file columns:")
print(df1.columns.tolist())

print("\nSecond CSV file columns:")
print(df2.columns.tolist())

# Prompt the user to input the correct column names for emails
email_column_name1 = input("Please enter the column name for email in the first CSV file: ")
email_column_name2 = input("Please enter the column name for email in the second CSV file: ")

# Ensure that the provided 'email' columns exist in both dataframes
if email_column_name1 not in df1.columns:
    print(f"Error: '{email_column_name1}' column not found in the first CSV file.")
elif email_column_name2 not in df2.columns:
    print(f"Error: '{email_column_name2}' column not found in the second CSV file.")
else:
    # Filter out rows with empty emails in the first dataframe
    df1_non_empty_email = df1[df1[email_column_name1].notna() & df1[email_column_name1].str.strip().ne('')]
    df1_empty_email = df1[df1[email_column_name1].isna() | df1[email_column_name1].str.strip().eq('')]

    # Merge the dataframes on the email column and retain only the first CSV columns
    common_emails = pd.merge(df1_non_empty_email, df2, left_on=email_column_name1, right_on=email_column_name2)

    # Select only the columns from the first CSV file
    result = common_emails[df1.columns].drop_duplicates()

    # Save the overlapping data to a new CSV file
    result.to_csv('overlapping_emails.csv', index=False)

    # Save the rows with empty emails to a separate CSV file
    df1_empty_email.to_csv('empty_emails.csv', index=False)

    print("The overlapping rows have been saved to 'overlapping_emails.csv'")
    print("The rows with empty emails have been saved to 'empty_emails.csv'")