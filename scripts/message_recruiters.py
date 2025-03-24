from selenium.webdriver.common.by import By
import time
from scripts.login import login
from utils.file_handler import get_settings

def message_recruiters():
    driver = login()
    settings = get_settings()
    
    driver.get("https://www.linkedin.com/search/results/people/?keywords=recruiter")
    time.sleep(5)

    recruiters = driver.find_elements(By.CLASS_NAME, "entity-result")
    
    for recruiter in recruiters[:5]:  # Message 5 recruiters
        recruiter.click()
        time.sleep(2)
        
        try:
            message_button = driver.find_element(By.CLASS_NAME, "message-anywhere-button")
            message_button.click()
            time.sleep(2)
            
            message_box = driver.find_element(By.CLASS_NAME, "msg-form__contenteditable")
            message_box.send_keys(settings["message_template"].format(name="Recruiter", resume_link="your_resume_link"))
            time.sleep(2)
            
            send_button = driver.find_element(By.CLASS_NAME, "msg-form__send-button")
            send_button.click()
            print("Message sent to a recruiter!")
        except:
            print("Unable to send message.")

    driver.quit()

if __name__ == "__main__":
    message_recruiters()
