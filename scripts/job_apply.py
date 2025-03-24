from selenium.webdriver.common.by import By
import time
from scripts.login import login

def apply_jobs():
    driver = login()
    driver.get("https://www.linkedin.com/jobs/search/")
    time.sleep(5)

    jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")
    
    for job in jobs[:5]:  # Apply for first 5 jobs
        job.click()
        time.sleep(2)
        try:
            easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
            easy_apply.click()
            time.sleep(2)
            submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button")
            submit_button.click()
            print("Applied for a job!")
        except:
            print("No Easy Apply option available.")

    driver.quit()

if __name__ == "__main__":
    apply_jobs()
