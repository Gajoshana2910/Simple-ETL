import pandas as pd

def extract(file_path):
    """Extract data from CSV file."""
    df = pd.read_csv(file_path)  # Read CSV
    df.columns = df.columns.str.strip()  # Remove extra spaces in column names
    return df

def transform(df):
    """Handle missing values and format text."""
    # Use recommended method for Pandas 3.0+
    df.fillna({"age": df["age"].median(), "salary": df["salary"].median()}, inplace=True)

    # Convert names to uppercase
    df["name"] = df["name"].str.upper()

    return df

def load(df, output_path):
    """Save cleaned data to CSV."""
    df.to_csv(output_path, index=False)
    print(f"ETL Completed! Data saved to {output_path}")

if __name__ == "__main__":
    data = extract("data/data.csv")
    print("Extracted Data:\n", data.head())  # Debugging Step

    cleaned_data = transform(data)
    print("Transformed Data:\n", cleaned_data.head())  # Debugging Step

    load(cleaned_data, "data/cleaned_data.csv")
