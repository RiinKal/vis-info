import pandas as pd

# Reload the merged dataset to ensure proper numeric formatting
merged_data_path = 'merged_data.csv'
merged_data = pd.read_csv(merged_data_path)

# Convert critical fields to numeric to ensure they are interpreted correctly
fields_to_check = ['total_count', 'agg_total_count']
for field in fields_to_check:
    merged_data[field] = pd.to_numeric(merged_data[field], errors='coerce')

# Save the cleaned dataset back to a file
output_path = 'cleaned_merged_data.csv'
merged_data.to_csv(output_path, index=False)

# Return the cleaned file path for user
output_path
