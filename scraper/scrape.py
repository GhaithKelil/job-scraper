from playwright.sync_api import sync_playwright
import pandas as pd
import os

def scrape_duunitori(search_term="python", max_jobs=50):
    print(f"Searching duunitori.fi for: {search_term}")
    
    url = f"https://duunitori.fi/tyopaikat?haku={search_term.replace(' ', '+')}"
    
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Opening browser...")
        page.goto(url, wait_until="networkidle")

        try:
            page.click("button:has-text('Hyväksy')", timeout=5000)
            print("Accepted cookies")
        except:
            pass

        page.wait_for_selector(".job-box", timeout=15000)

        job_cards = page.query_selector_all(".job-box")
        print(f"Found {len(job_cards)} job listings")

        for card in job_cards[:max_jobs]:
            try:
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
                        "location": location
                    })
            except Exception as e:
                print(f"Error parsing card: {e}")

        browser.close()

    if not jobs:
        print("No jobs found.")
        return

    df = pd.DataFrame(jobs)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/jobs.csv", index=False)

    print(f"\nScraped {len(jobs)} jobs!")
    print(df.head(10))

if __name__ == "__main__":
    scrape_duunitori(search_term="python")