# Finnish Job Market Scraper & Analyzer

A Python tool that scrapes live job listings from [Duunitori.fi](https://duunitori.fi), stores them in a SQLite database, and visualizes market trends through an interactive dashboard.

Built as a portfolio project demonstrating web scraping, data pipelines, database management, and data visualization.

---

## What It Does

Most job market tools are static. This one pulls real, current data directly from Finland's largest job board, stores every scrape run with a timestamp, and lets you explore the results visually.

You can compare demand across multiple roles at once — for example, how many Python jobs are available versus developer, data analyst, or cybersecurity roles — and see which companies and cities are hiring the most.

---

## Features

- Scrapes live job listings (title, company, location) using browser automation
- Handles JavaScript-rendered pages that basic scrapers cannot access
- Runs multiple search terms in one pass and tags each result
- Stores all scraped data in a SQLite database with timestamps for historical tracking
- Exports to CSV for quick access
- Analyzes trends: role types, top companies, geographic distribution
- Generates interactive browser-based charts with Plotly

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core language |
| Playwright | Browser automation for JavaScript-rendered pages |
| BeautifulSoup4 | HTML parsing |
| Pandas | Data cleaning and analysis |
| SQLite | Persistent database storage |
| Plotly | Interactive data visualization |

---

## Project Structure

```
job-scraper/
├── scraper/
│   └── scrape.py           # Playwright web scraper
├── analysis/
│   └── analyze.py          # Pandas data analysis
├── dashboard/
│   └── dashboard.py        # Interactive Plotly dashboard
├── database/
│   └── db.py               # SQLite database handler
├── data/
│   └── jobs.db             # Auto-generated database
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/GhaithKelil/job-scraper.git
cd job-scraper

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt
playwright install chromium
```

### Usage

```bash
# Step 1 - Scrape jobs from Duunitori.fi
python scraper/scrape.py

# Step 2 - Run analysis
python analysis/analyze.py

# Step 3 - Open interactive dashboard in browser
python dashboard/dashboard.py
```

---

## Sample Results

Scraping across four search terms (python, developer, data analyst, cybersecurity) returns around 70-100 unique listings per run. Key findings from the Finnish market:

- Helsinki and Espoo account for the majority of tech listings
- Engineer and Analyst are the most common role types
- LähiTapiola, Fortum, and Tampereen yliopisto are among the most active hirers
- Developer roles have the highest overall listing count

---

## Potential Extensions

- Schedule daily scraping with Windows Task Scheduler or cron
- Add trend tracking to compare market changes over time
- Expand to additional job boards for broader coverage

---

## Author

Ghaith Kelil — [GitHub](https://github.com/GhaithKelil)git add README.md
git commit -m "Update README"
git push