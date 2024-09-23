import pandas as pd

# Load the dataset
file_path = "soe_yearly_arrivals_total_countries.csv"
df = pd.read_csv(file_path)

# Get the unique years in the dataset
unique_years = df['year'].unique()

# Iterate through each year and create a separate file
for year in unique_years:
    # Filter the dataset for the current year
    yearly_data = df[df['year'] == year]
    
    # Define the file name for the current year
    output_file_path = f"soe_yearly_arrivals_{year}.csv"
    
    # Save the filtered data to a CSV file
    yearly_data.to_csv(output_file_path, index=False)
    
    print(f"Dataset for {year} saved to {output_file_path}")
