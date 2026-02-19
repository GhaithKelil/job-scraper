import pandas as pd

df = pd.read_csv("data/jobs.csv")
search_term = df["search_term"].iloc[0]

print(f"\n=== JOB MARKET ANALYSIS: {search_term.upper()} ===")
print(f"Total jobs found: {len(df)}")

print("\n--- Top 10 Companies ---")
print(df["company"].value_counts().head(10))

print("\n--- Top 10 Locations ---")
df["city"] = df["location"].str.split(" ja ").str[0].str.strip()
print(df["city"].value_counts().head(10))

print("\n--- Job Title Keywords ---")
keywords = ["Engineer", "Developer", "Manager", "Designer",
            "Analyst", "Architect", "Consultant", "Specialist"]
for kw in keywords:
    count = df["title"].str.contains(kw, case=False).sum()
    if count > 0:
        print(f"  {kw}: {count} jobs")