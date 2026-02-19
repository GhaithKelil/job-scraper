import pandas as pd
import plotly.express as px

df = pd.read_csv("data/jobs.csv")

# --- Chart 1: Jobs by search term comparison ---
term_counts = df["search_term"].value_counts().reset_index()
term_counts.columns = ["Search Term", "Job Count"]

fig1 = px.bar(term_counts, x="Search Term", y="Job Count",
              title="Job Market Demand by Tech/Role in Finland",
              color="Search Term",
              text="Job Count")
fig1.update_traces(textposition="outside")
fig1.update_layout(height=500, showlegend=False)
fig1.show()

# --- Chart 2: Job Title Keywords Breakdown ---
keywords = ["Engineer", "Developer", "Manager", "Designer",
            "Officer", "Executive", "Analyst", "Architect"]

keyword_counts = {}
for keyword in keywords:
    keyword_counts[keyword] = df["title"].str.contains(keyword, case=False).sum()

kw_df = pd.DataFrame(list(keyword_counts.items()), columns=["Keyword", "Count"])
kw_df = kw_df[kw_df["Count"] > 0].sort_values("Count", ascending=False)

fig2 = px.bar(kw_df, x="Keyword", y="Count",
              title="Most In-Demand Job Types in Finland",
              color="Count", color_continuous_scale="Blues",
              text="Count")
fig2.update_traces(textposition="outside")
fig2.update_layout(height=500, showlegend=False)
fig2.show()

# --- Chart 3: Top Companies ---
top_companies = df["company"].value_counts().head(10).reset_index()
top_companies.columns = ["Company", "Listings"]

fig3 = px.bar(top_companies, x="Listings", y="Company",
              orientation="h",
              title="Top Companies Hiring in Finland",
              color="Listings", color_continuous_scale="Greens",
              text="Listings")
fig3.update_traces(textposition="outside")
fig3.update_layout(height=600, yaxis=dict(autorange="reversed"), showlegend=False)
fig3.show()

# --- Chart 4: Top Locations ---
df["city"] = df["location"].str.split(" ja ").str[0].str.strip()
top_cities = df["city"].value_counts().head(10).reset_index()
top_cities.columns = ["City", "Count"]

fig4 = px.bar(top_cities, x="Count", y="City",
              orientation="h",
              title="Top Cities for Tech Jobs in Finland",
              color="Count", color_continuous_scale="Oranges",
              text="Count")
fig4.update_traces(textposition="outside")
fig4.update_layout(height=500, yaxis=dict(autorange="reversed"), showlegend=False)
fig4.show()

print("Dashboard opened in browser!")