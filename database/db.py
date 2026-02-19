import sqlite3
import os

DB_PATH = "data/jobs.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            search_term TEXT,
            scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_jobs(jobs):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO jobs (title, company, location, search_term)
        VALUES (:title, :company, :location, :search_term)
    ''', jobs)
    conn.commit()
    conn.close()
    print(f"Saved {len(jobs)} jobs to database.")

def get_all_jobs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, company, location, search_term, scraped_at FROM jobs")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_latest_scrape():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT title, company, location, search_term
        FROM jobs
        WHERE DATE(scraped_at) = DATE('now')
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows