# Finnish Job Market Scraper & Analyzer

A Python tool that scrapes live job listings from [Duunitori.fi](https://duunitori.fi), stores them in a SQLite database, and generates a single-page interactive HTML report with charts and stats.

Built as a portfolio project demonstrating web scraping, data pipelines, database management, and data visualization.

---

## What It Does

Enter any job title or field and the tool scrapes live listings from Finland's largest job board, stores the results in a SQLite database with timestamps, and generates a single-page interactive HTML report with all charts and stats.

It works for any profession — teacher, nurse, marketing manager, software developer — not just tech roles.

---

## Features

- Accepts any search term at runtime — works for any job or field
- Scrapes live job listings (title, company, location) using browser automation
- Handles JavaScript-rendered pages that basic scrapers cannot access
- Stores all scraped data in a SQLite database with timestamps
- Exports to CSV for quick access
- Generates a single-page interactive HTML report with all charts
- Report can be shared with anyone — no Python required to view it

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
│   └── dashboard.py        # Single-page HTML dashboard
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
# Step 1 - Run the scraper (you will be prompted to enter a search term)
python scraper/scrape.py

# Step 2 - Optional: print analysis summary in terminal
python analysis/analyze.py

# Step 3 - Generate and open the dashboard
python dashboard/dashboard.py
```

The dashboard saves as an HTML file in the `data/` folder and opens automatically in your browser. It can be shared with anyone — no Python required to view it.

---

## Sample Results

Searching for "python" returns around 25-50 live listings. Key findings from the Finnish market:

- Helsinki and Espoo account for the majority of tech listings
- Engineer and Analyst are the most common role types
- LähiTapiola, Fortum, and Tampereen yliopisto are among the most active hirers

---

## Potential Extensions

- Schedule daily scraping with Windows Task Scheduler or cron
- Add trend tracking to compare market changes over time
- Expand to additional job boards for broader coverage

---

## Author

Ghaith Kelil — [GitHub](https://github.com/GhaithKelil)