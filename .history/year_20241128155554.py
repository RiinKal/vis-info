import pandas as pd

# Load the dataset
df = pd.read_csv('info_vis_assignment.csv')

# Ensure 'year' is converted to datetime format
# Convert to datetime, handle errors gracefully
df['year'] = pd.to_datetime(df['year'], errors='coerce')

# Save the dataset with the fixed format
df.to_csv('info_vis_assignment.csv', index=False)

# Confirm the data type and unique values
print("Data type of 'year' column after conversion:", df['year'].dtype)
print("Unique values in 'year' column:")
print(df['year'].unique())
