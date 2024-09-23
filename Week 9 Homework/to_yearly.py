import pandas as pd

# Load the dataset
file_path = "arrivals_soe.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Extract the year from the date
df['year'] = df['date'].dt.year

# Group by 'year', 'country', and 'soe' and sum up the arrivals data
yearly_df = df.groupby(['year', 'country', 'soe']).agg({
    'arrivals': 'sum',
    'arrivals_male': 'sum',
    'arrivals_female': 'sum'
}).reset_index()

# Save the new dataset to a CSV file
output_file_path = "yearly_arrivals_soe.csv"
yearly_df.to_csv(output_file_path, index=False)

print(f"Yearly dataset saved to {output_file_path}")
