# job-scraper 🔍

Scrapes live job listings from [Duunitori.fi](https://duunitori.fi) (Finland's largest job board), stores them in SQLite, and generates a self-contained interactive HTML report with charts.

Works for any job title or profession — not just tech roles.

## What it does

1. You enter a search term (e.g. "python", "nurse", "marketing manager")
2. Playwright scrapes live listings from Duunitori — handles JavaScript-rendered pages
3. Results are stored in SQLite with timestamps
4. A Plotly dashboard is generated as a single HTML file you can share with anyone

## Tech stack

- **Playwright** — browser automation for JS-rendered pages
- **BeautifulSoup4** — HTML parsing
- **Pandas** — data cleaning and analysis
- **SQLite** — persistent storage with timestamps
- **Plotly** — interactive charts in the report

## Setup

```bash
git clone https://github.com/GhaithKelil/job-scraper.git
cd job-scraper

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
playwright install chromium
```

## Usage

```bash
# 1. Scrape (you'll be prompted for a search term)
python scraper/scrape.py

# 2. Optional: print a summary in the terminal
python analysis/analyze.py

# 3. Generate the dashboard (opens automatically in browser)
python dashboard/dashboard.py
```

The report is saved as an HTML file in `data/` and can be shared with anyone — no Python needed to view it.

## Project structure

```
job-scraper/
├── scraper/
│   └── scrape.py       # Playwright scraper
├── analysis/
│   └── analyze.py      # Pandas analysis
├── dashboard/
│   └── dashboard.py    # HTML report generator
├── database/
│   └── db.py           # SQLite handler
├── data/               # Generated files (gitignored)
└── requirements.txt
```

## Sample findings

Searching for "python" in the Finnish market:

- Helsinki and Espoo account for most listings
- Engineer and Developer are the most common titles
- LahiTapiola, Fortum, and Tampereen yliopisto among top hirers

## License

MIT