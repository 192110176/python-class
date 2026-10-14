import pandas as pd

# Read the first Excel file
df = pd.read_excel(r"C:\Users\Kavitha\OneDrive\Documents\emp3.xlsx")

# Select alternative rows
alternative_rows = df.iloc[::2]

# Save them into the second Excel file
alternative_rows.to_excel(
    r"C:\Users\Kavitha\OneDrive\Documents\emp4.xlsx",
    index=False
)

print("Alternative rows copied successfully!")