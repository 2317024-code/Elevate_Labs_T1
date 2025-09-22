import pandas as pd

df = pd.read_csv("C://Users//aabij//Downloads//marketing_campaign.csv", sep="\t")

#Missing Values
print("Missing values before cleaning:")
print(df.isnull().sum())

if 'Income' in df.columns:
    df['Income'] = df['Income'].fillna(df['Income'].median())

#Duplicates Removal
duplicates = df.duplicated().sum()
df.drop_duplicates(inplace=True)

#Standardize text values
if 'Marital_Status' in df.columns:
    df['Marital_Status'] = df['Marital_Status'].str.strip().str.title()
if 'Education' in df.columns:
    df['Education'] = df['Education'].str.strip().str.title()

#Date Formats
if 'Dt_Customer' in df.columns:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')
    df['Dt_Customer'] = df['Dt_Customer'].dt.strftime('%d-%m-%Y')

#Rename column names
df.columns = df.columns.str.lower().str.replace(" ", "_")
if 'year_birth' in df.columns:
    df['year_birth'] = df['year_birth'].astype(int)
if 'income' in df.columns:
    df['income'] = df['income'].astype(float)

#Saving Data Types
opfile = "Customer_Personality_Analysis.csv"
df.to_csv(opfile, index=False, encoding="utf-8")

#Cleaning Report
print("\nCleaning Report:")
print(f"Total rows after cleaning: {len(df)}")
print(f"Duplicates removed: {duplicates}")
print(f"Remaining missing values:\n{df.isnull().sum()}")
print("\nData types after cleaning:")
print(df.dtypes)
print(f"\nDataset cleaned and saved as: {opfile}")