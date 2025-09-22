# Task 1: Data Cleaning and Preprocessing

Objective: Clean and prepare a raw dataset (with nulls, duplicates, inconsistent formats).

Tools: Python (Pandas)

Dataset: Customer Personality Analysis 

Steps Performed:

1. Load Dataset
Used pandas.read_csv() to load the dataset.

Since the raw file was tab-delimited, sep="\t" was used to correctly separate columns.

2. Identify and Handle Missing Values
Checked for missing values with df.isnull().sum().

Filled missing values in the Income column using the median, ensuring outliers do not affect the imputation.

3. Remove Duplicates
Detected duplicate rows with df.duplicated().sum().

Removed duplicates using df.drop_duplicates(inplace=True).

4. Standardize Text Values
Cleaned up text columns by removing extra spaces and making them consistent with str.strip().str.title().

Example: married → Married, single → Single.

Applied to Marital_Status and Education columns.

5. Convert Date Formats
Converted Dt_Customer (customer joining date) to a proper datetime format.

Re-saved it as a dd-mm-yyyy string so that Excel shows readable dates instead of serial numbers.

6. Rename Columns
Standardized column names by converting them to lowercase and replacing spaces with underscores.

Example: Year Birth → year_birth.

7. Fix Data Types
Converted year_birth to integer.

Converted income to float for consistency in analysis.

8. Save Cleaned Dataset
Saved the cleaned file as customer_personality_cleaned.csv.

Used UTF-8 encoding to ensure compatibility with Excel and other tools.

9. Cleaning Report (Console Output)
Number of rows after cleaning.

Count of duplicates removed.

Remaining missing values (if any).

Final data types of each column.

A quick preview of the cleaned dataset.
