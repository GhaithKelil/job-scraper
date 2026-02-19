import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

df = pd.read_csv("data/jobs.csv")
search_term = df["search_term"].iloc[0]
total_jobs = len(df)

# --- Prep data ---
# Top companies
top_companies = df["company"].value_counts().head(10).reset_index()
top_companies.columns = ["Company", "Count"]

# Top cities
df["city"] = df["location"].str.split(" ja ").str[0].str.strip()
top_cities = df["city"].value_counts().head(10).reset_index()
top_cities.columns = ["City", "Count"]

# Keywords
keywords = ["Engineer", "Developer", "Manager", "Designer",
            "Analyst", "Architect", "Consultant", "Specialist"]
kw_counts = {k: df["title"].str.contains(k, case=False).sum() for k in keywords}
kw_df = pd.DataFrame(list(kw_counts.items()), columns=["Keyword", "Count"])
kw_df = kw_df[kw_df["Count"] > 0].sort_values("Count", ascending=False)

# --- Build dashboard ---
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "Most Common Role Types",
        "Top 10 Companies Hiring",
        "Top 10 Cities",
        ""
    ),
    vertical_spacing=0.15,
    horizontal_spacing=0.1
)

# Chart 1: Keywords
fig.add_trace(go.Bar(
    x=kw_df["Keyword"], y=kw_df["Count"],
    marker_color="#4C9BE8",
    text=kw_df["Count"], textposition="outside",
    name="Role Types"
), row=1, col=1)

# Chart 2: Companies
fig.add_trace(go.Bar(
    x=top_companies["Count"], y=top_companies["Company"],
    orientation="h",
    marker_color="#57B894",
    text=top_companies["Count"], textposition="outside",
    name="Companies"
), row=1, col=2)

# Chart 3: Cities
fig.add_trace(go.Bar(
    x=top_cities["Count"], y=top_cities["City"],
    orientation="h",
    marker_color="#F4A261",
    text=top_cities["Count"], textposition="outside",
    name="Cities"
), row=2, col=1)

# Layout
fig.update_layout(
    title=dict(
        text=f'Job Market Report: "{search_term}" — {total_jobs} listings found',
        font=dict(size=22)
    ),
    height=900,
    showlegend=False,
    template="plotly_dark",
    paper_bgcolor="#1e1e1e",
    plot_bgcolor="#1e1e1e",
)

fig.update_yaxes(autorange="reversed", row=1, col=2)
fig.update_yaxes(autorange="reversed", row=2, col=1)

# Save and open
os.makedirs("data", exist_ok=True)
output_path = f"data/report_{search_term.replace(' ', '_')}.html"
fig.write_html(output_path)

import webbrowser
webbrowser.open(os.path.abspath(output_path))
print(f"Report saved to: {output_path}")