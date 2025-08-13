import pandas as pd

# Load the messy CSV
df = pd.read_csv("data/messy_data.csv")

print("Before cleaning:")
print(df)

# Drop empty rows
df = df.dropna(how="all")

# Remove duplicate rows
df = df.drop_duplicates()

# Trim spaces from string columns
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Standardize casing
df["Name"] = df["Name"].str.title()
df["Email"] = df["Email"].str.lower()
df["Country"] = df["Country"].str.title()

# Convert Age to numeric (handles spaces, text, NaN)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Fill missing Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean().round(0))

# Save cleaned CSV
df.to_csv("data/cleaned_data.csv", index=False)

print("\nAfter cleaning:")
print(df)
