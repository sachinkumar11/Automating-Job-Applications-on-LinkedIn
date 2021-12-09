# Automated Job Application Bot

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import config

chrome_driver_path = Service(r"C:\Users\sachin kumar\PycharmProjects\PySelenium\chromedriver.exe")
driver = webdriver.Chrome(service = chrome_driver_path)


LOGIN_URL = "https://www.linkedin.com/login"

JOBS_URL = "https://www.linkedin.com/jobs/search/?geoId=112376381&keywords=python%20developer&location=Bangalore%20Urban%2C%20Karnataka%2C%20India"



def login():

    driver.get(url=LOGIN_URL)
    time.sleep(2)

    accept_cookies = driver.find_element(By.XPATH,'//*[@id="artdeco-global-alert-container"]/div[1]/section/div/div[2]/button[2]')
    accept_cookies.click()

    driver.find_element(By.ID,"username").send_keys(config.LINKEDIN_EMAIL)
    driver.find_element(By.ID,"password").send_keys(config.LINKEDIN_PASS)
    driver.find_element(By.ID,"password").submit()


def get_job_urls():

    driver.get(url=JOBS_URL)
    time.sleep(2)
    jobs = driver.find_elements(By.CLASS_NAME,"job-card-container__link")
    job_url_list = []
    for job in jobs:
        job_url = job.get_attribute("href")

        if job_url.find("www.linkedin.com/jobs/view/") >= 0 and job_url not in job_url_list:
            job_url_list.append(job_url)
    return job_url_list


def apply_to_job(link):

    driver.get(url=link)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"jobs-apply-button").click()
    time.sleep(1)

    button = driver.find_element(By.CSS_SELECTOR,"footer button")
    if button.text == "Submit application":

        driver.find_element(By.CLASS_NAME,"fb-single-line-text__input").send_keys(config.LINKEDIN_PHONE)

        print(f"*** Pretending to click on the \"{button.text}\" button. ***")
    else:

        print(f"One-step application is not possible for this job.")


# driver = webdriver.Chrome()


login()


time.sleep(3)


url_list = get_job_urls()
if len(url_list) == 0:
    print("No jobs found.\nMake sure you're logged in properly or tweak the position or location name.")


for url in url_list:
    apply_to_job(url)
    time.sleep(5)


driver.close()