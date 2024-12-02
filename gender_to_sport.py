import pandas as pd

# Load the datasets
sports_data = pd.read_csv('categorized_sports_data.csv')
gender_balance = pd.read_csv('gender_balance_best_worst.csv')

# Merge gender-related fields into the sports dataset based on 'region' and 'year'
# Ensure both datasets have 'region' and 'year' columns for alignment
if 'year' not in sports_data.columns:
    sports_data['year'] = None  # Placeholder if year is missing

# Merge datasets
merged_data = pd.merge(
    sports_data,
    gender_balance[['region', 'year', 'Male_P', 'Female_P']],
    on=['region', 'year'],
    how='left'
)

# Save the updated dataset
merged_data.to_csv('updated_sports_data.csv', index=False)
