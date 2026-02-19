from playwright.sync_api import sync_playwright
import pandas as pd
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db import init_db, save_jobs

def scrape_duunitori(search_term, max_jobs=50):
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


# --- Ask user for search term ---
search_term = input("Enter a job title or field to search (e.g. teacher, doctor, python): ").strip()

if not search_term:
    print("No search term entered. Exiting.")
    sys.exit()

print(f"\nScraping Duunitori.fi for: {search_term}...")
results = scrape_duunitori(search_term, max_jobs=50)
print(f"Found {len(results)} jobs")

if not results:
    print("No jobs found. Try a different search term.")
    sys.exit()

init_db()
save_jobs(results)

df = pd.DataFrame(results)
df.drop_duplicates(subset=["title", "company"], inplace=True)
os.makedirs("data", exist_ok=True)
df.to_csv("data/jobs.csv", index=False)
print(f"Total unique jobs saved: {len(df)}")
print("\nNow run: python dashboard/dashboard.py")