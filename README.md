# Finnish Job Market Scraper & Analyzer

A Python automation tool that scrapes live job listings from [Duunitori.fi](https://duunitori.fi) — Finland's largest job board — processes the data with pandas, and presents market insights through an interactive visual dashboard.

Built as a portfolio project demonstrating web scraping, data analysis, and visualization skills.

---

## Features

- Scrapes real-time job listings including title, company, and location
- Handles JavaScript-rendered pages using browser automation
- Stores structured data in CSV format for reproducibility
- Analyzes hiring trends: most in-demand roles, top companies, geographic distribution
- Generates interactive, browser-based charts with Plotly

---

## Tech Stack

| Library | Purpose |
|---|---|
| Python 3.11 | Core language |
| Playwright | Browser automation for JavaScript-rendered pages |
| BeautifulSoup4 | HTML parsing |
| Pandas | Data cleaning and analysis |
| Plotly | Interactive data visualization |

---

## Project Structure

```
job-scraper/
├── scraper/
│   └── scrape.py           # Playwright-based web scraper
├── analysis/
│   └── analyze.py          # Pandas data analysis and summary
├── dashboard/
│   └── dashboard.py        # Interactive Plotly dashboard
├── data/
│   └── jobs.csv            # Output data from scraper
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
# Step 1 - Scrape job listings from Duunitori.fi
python scraper/scrape.py

# Step 2 - Run data analysis
python analysis/analyze.py

# Step 3 - Launch interactive dashboard (opens in browser)
python dashboard/dashboard.py
```

---

## Sample Insights

Running the scraper for Python-related roles reveals:

- **Helsinki** and **Espoo** account for the majority of listings
- **Engineer** and **Analyst** are the most common role types
- Companies such as **LähiTapiola**, **Fortum**, and **Tampereen yliopisto** are among the most active hirers

---

## Future Improvements

- Schedule automated daily scraping using Windows Task Scheduler or cron
- Migrate data storage from CSV to SQLite for better querying
- Expand search terms to compare demand across multiple tech stacks
- Add trend tracking over time to observe market changes

---

## Author

Ghaith Kelil — [GitHub](https://github.com/GhaithKelil)