import pandas as pd

# Load the yearly dataset
file_path = "yearly_arrivals_soe.csv"
df = pd.read_csv(file_path)

# Group by 'year' and 'soe' and sum up the arrivals data
soe_yearly_df = df.groupby(['year', 'soe']).agg({
    'arrivals': 'sum',
    'arrivals_male': 'sum',
    'arrivals_female': 'sum'
}).reset_index()

# Save the new dataset to a CSV file
output_file_path = "soe_yearly_arrivals_total_countries.csv"
soe_yearly_df.to_csv(output_file_path, index=False)

print(f"SOE-Yearly dataset saved to {output_file_path}")
