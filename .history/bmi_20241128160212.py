import pandas as pd

# Load the dataset
df = pd.read_csv('info_vis_assignment.csv')

# Convert height from cm to meters
df['height_m'] = df['height'] / 100

# Calculate BMI (weight in kg, height in meters)
df['bmi'] = df['weight'] / (df['height_m'] ** 2)

# Round BMI to 1 decimal place
df['bmi'] = df['bmi'].round(1)

# Overwrite the original file with the new BMI column
df.to_csv('info_vis_assignment.csv', index=False)

print("BMI calculated and file overwritten.")
