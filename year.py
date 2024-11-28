import pandas as pd

# Load the dataset
df = pd.read_csv('info_vis_assignment.csv')

# Convert 'year' column to a temporal format (datetime)
df['year'] = pd.to_datetime(df['year'], format='%Y')

# Check and print the data type of the 'year' column after conversion
print("Data type of 'year' column after conversion:", df['year'].dtype)

# Print unique values in the 'year' column
print("Unique values in 'year' column:")
print(df['year'].unique())

# Save the modified dataset
#df.to_csv('ussr_countries_only_modified.csv', index=False)
