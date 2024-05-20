# CSV Comparison Script

This script is designed to compare two CSV files with different headers, allowing you to map or drop columns from the second CSV file to match the headers of the first CSV file. It then updates both CSV files to use the same header format and creates three new files: one with data that is present in both documents, one with data that is in the second file but not in the first, and one with data that is missing based on specified criteria.

## Prerequisites

Make sure you have Python installed on your computer. You also need the `pandas` library. You can install it using the following command:

pip install pandas

## Usage
Save your first CSV file as source1.csv and your second CSV file as source2.csv.

Save the script as compare_csvs.py.

Ensure the source1.csv, source2.csv, and compare_csvs.py files are in the same directory.

Create a directory named data in the same location to store the output files.

## Running the Script
Open a terminal or command prompt, navigate to the directory where the compare_csvs.py script is saved, and run the script using Python:

python compare_csvs.py

## Follow the Prompts
The script will list the columns of both CSV files.
For each column in the second CSV file, you will be asked whether to map it to a column in the first CSV file or to drop it. Use d to drop and m to map.
If mapping, provide the corresponding column name from the first CSV file.
The script will then align the columns of both CSV files and create the three comparison files.
## Output Files
The following files will be saved in the data directory:

updated_source1.csv: The first CSV file with updated headers.
updated_source2.csv: The second CSV file with updated headers.
common_data.csv: Data that is present in both files.
data_in_file2_not_in_file1.csv: Data that is in the second file but not in the first.
missing_data.csv: Data that is missing based on the specified 
column.
## License
This project is licensed under the MIT License

# Column Splitter


# CSV Name Splitter Script
This script is designed to split a column in a CSV file that contains names in the format "Last Name, First Name" into two separate columns: "Last Name" and "First Name".  

## Prerequisites  Make sure you have Python installed on your computer. You also need the `pandas` library. You can install it using the following command:  

pip install pandas```

## Usage

1. Save your CSV file as `names.csv` or update the script with the correct file path.
2. Save the script as `split_names.py`.

### Running the Script

Open a terminal or command prompt, navigate to the directory where the `split_names.py` script is saved, and run the script using Python:

`python split_names.py`

### Output

The script will create a new CSV file named `split_names.csv` with the following columns:

- `Last Name`
- `First Name`

### Script Explanation

- **Load the CSV file:** The script loads the CSV file into a DataFrame and handles a `FileNotFoundError` if the file does not exist.
- **Check for the name column:** The script checks if the specified name column exists in the DataFrame.
- **Split the name column:** The script defines a `split_name` function to handle cases where the format might not be as expected. If the split operation does not produce two parts, it defaults to using the original name and an empty string.
- **Drop the original name column:** The script drops the original name column after splitting.
- **Save the updated DataFrame:** The script saves the updated DataFrame with separate 'Last Name' and 'First Name' columns to a new CSV file.

### Customization

- **File Path:** Update the `file_path` variable with the correct path to your CSV file.
- **Column Name:** Update the `name_column` variable with the correct column name if it is different from "Name".
- **Output File Path:** Update the `output_file_path` variable with the desired output file path.

## License

This project is licensed under the MIT License.