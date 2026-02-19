from playwright.sync_api import sync_playwright
import pandas as pd
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db import init_db, save_jobs

def scrape_duunitori(search_term, max_jobs=30):
    url = f"https://duunitori.fi/tyopaikat?haku={search_term.replace(' ', '+')}"
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

        try:
            page.click("button:has-text('Hyväksy')", timeout=5000)
        except:
            pass

        try:
            page.wait_for_selector(".job-box", timeout=15000)
        except:
            print(f"  No results found for: {search_term}")
            browser.close()
            return []

        job_cards = page.query_selector_all(".job-box")

        for card in job_cards[:max_jobs]:
            title_el = card.query_selector("h3.job-box__title")
            company_el = card.query_selector("a.job-box__hover")
            location_el = card.query_selector("span.job-box__job-location")

            title = title_el.inner_text().strip() if title_el else "N/A"
            company = company_el.get_attribute("data-company") if company_el else "N/A"
            location = location_el.inner_text().strip().replace(" –", "") if location_el else "N/A"

            if title != "N/A":
                jobs.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "search_term": search_term
                })

        browser.close()
    return jobs


# --- Run for multiple search terms ---
search_terms = ["python", "developer", "data analyst", "cybersecurity"]
all_jobs = []

init_db()

for term in search_terms:
    print(f"Scraping: {term}...")
    results = scrape_duunitori(term, max_jobs=30)
    print(f"  Found {len(results)} jobs")
    all_jobs.extend(results)

# Save to database
save_jobs(all_jobs)

# Also keep CSV for dashboard compatibility
df = pd.DataFrame(all_jobs)
df.drop_duplicates(subset=["title", "company"], inplace=True)
os.makedirs("data", exist_ok=True)
df.to_csv("data/jobs.csv", index=False)
print(f"Total unique jobs scraped: {len(df)}")