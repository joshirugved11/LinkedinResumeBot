from selenium.webdriver.common.by import By
import time
from scripts.login import login

def scrape_jobs():
    driver = login()
    driver.get("https://www.linkedin.com/jobs/search/")
    time.sleep(5)

    jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")

    job_list = []
    for job in jobs[:5]:
        title = job.find_element(By.CLASS_NAME, "job-card-list__title").text
        company = job.find_element(By.CLASS_NAME, "job-card-container__company-name").text
        job_list.append({"title": title, "company": company})

    driver.quit()
    return job_list

if __name__ == "__main__":
    jobs = scrape_jobs()
    for job in jobs:
        print(job)
