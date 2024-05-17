# In Progress

Updating the readme to enable more customization based on the desired headers.

# CSV Overlap Finder

This script is designed to find overlapping rows based on email addresses from two CSV files and create a new CSV file with the overlapping data. It also creates a separate CSV file containing rows from the first CSV that have empty email addresses.

## Prerequisites

Make sure you have Python installed on your computer. You also need the `pandas` library. You can install it using the following command:

```sh
pip install pandas
```

## Usage

1. Save your first CSV file as `/source1.csv` and your second CSV file as `/source2.csv`.
2. Save the script as `find_overlapping_emails.py`.
3. Run the script from the command line:

```sh
python find_overlapping_emails.py
```

4. When prompted, enter the correct column names for the email fields in both CSV files.

The script will create two output files:

- `overlapping_emails.csv`: Contains rows with overlapping email addresses and relevant data from the first CSV file.
- `empty_emails.csv`: Contains rows from the first CSV file that have empty email addresses.

## Customization

### File Paths

If your CSV files are located at different paths, update the following lines in the script with the correct paths:

```python
file1 = '/path/to/your/first_file.csv'
file2 = '/path/to/your/second_file.csv'
```

### Column Names

If your email column names are different, update the script to reflect the correct column names. You will be prompted to enter these names when running the script. You can also look for any column heading by changing this.

### Retaining Specific Columns

If you want to retain specific columns from the first CSV file in the output, you can modify the selection in the script. For example, to retain only specific columns, update the following line:

```python
result = common_emails[['column1', 'column2', 'column3']].drop_duplicates()
```

Replace `'column1'`, `'column2'`, `'column3'` with the actual column names you want to retain.

## Script Overview

The script performs the following steps:

1. Loads the CSV files into DataFrames.
2. Strips leading/trailing spaces from column names.
3. Prints the column names of each CSV file for verification.
4. Prompts the user to input the correct column names for the email fields.
5. Filters out rows with empty emails from the first CSV file.
6. Merges the DataFrames based on the email columns.
7. Retains only the columns from the first CSV file.
8. Saves the overlapping data to `overlapping_emails.csv`.
9. Saves the rows with empty emails to `empty_emails.csv`.

## Example

Here is an example of how to run the script:

```sh
python find_overlapping_emails.py
```

When prompted:

```
Please enter the column name for email in the first CSV file: email
Please enter the column name for email in the second CSV file: Email
```

After running the script, you will have two new files: `overlapping_emails.csv` and `empty_emails.csv`.

## Troubleshooting

- Ensure that the CSV files are correctly formatted and that the email columns are specified accurately.
- If you encounter any issues, check the printed column names and ensure they match the input column names.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
