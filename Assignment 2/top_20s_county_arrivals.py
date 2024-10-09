import pandas as pd

# Load the dataset
file_path = 'data/yearly_arrivals_soe.csv'
data = pd.read_csv(file_path)

# Step 1: Sum up the arrivals for each country
country_arrivals = data.groupby('country')['arrivals'].sum().reset_index()

# Step 2: Sort the countries by total arrivals in descending order
country_arrivals = country_arrivals.sort_values(by='arrivals', ascending=False)

# Step 3: Create separate files for top 20, next 20, etc.
group_size = 20
for i in range(0, len(country_arrivals), group_size):
    # Select a subset of the top countries
    sub_data = country_arrivals.iloc[i:i + group_size]
    
    # Generate a file name based on the group number
    file_name = f'data/top_countries_{i // group_size + 1}.csv'
    
    # Save the subset to a new CSV file
    sub_data.to_csv(file_name, index=False)

print("Files created successfully.")
