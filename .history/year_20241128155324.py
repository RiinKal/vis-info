import pandas as pd

# Load the dataset
df = pd.read_csv('info_vis_assignment.csv')

# Ensure 'year' is converted to datetime format
# df['year'] = pd.to_datetime(df['year'])

# Save the dataset again
# df.to_csv('ussr_countries_only_modified.csv', index=False)

# Confirm the data type
print("Data type of 'year' column after conversion:", df['year'].dtype)
print("Unique values in 'year' column:")
print(df['year'].unique())
