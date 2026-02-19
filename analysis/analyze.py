import pandas as pd

def analyze_jobs():
    df = pd.read_csv("data/jobs.csv")

    print("=== JOB MARKET ANALYSIS ===\n")

    print(f"Total jobs scraped: {len(df)}\n")

    print("--- Top 10 Most Common Job Titles ---")
    print(df["title"].value_counts().head(10))
    print()

    print("--- Top 10 Companies With Most Listings ---")
    print(df["company"].value_counts().head(10))
    print()

    print("--- Top 10 Most Common Locations ---")
    print(df["location"].value_counts().head(10))
    print()

    # Extract keywords from job titles
    keywords = ["Engineer", "Developer", "Manager", "Designer", 
                "Analyst", "Consultant", "Director", "Officer"]
    
    print("--- Job Title Keywords Breakdown ---")
    for keyword in keywords:
        count = df["title"].str.contains(keyword, case=False).sum()
        print(f"  {keyword}: {count} jobs")

if __name__ == "__main__":
    analyze_jobs()