from scripts.job_apply import apply_jobs
from scripts.message_recruiters import message_recruiters
from scripts.scraper import scrape_jobs

if __name__ == "__main__":
    print("Starting LinkedIn Auto Bot...")
    jobs = scrape_jobs()
    print(f"Found {len(jobs)} jobs!")
    
    apply_jobs()
    message_recruiters()

    print("Bot execution completed!")
