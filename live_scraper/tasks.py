# live_scrapper/tasks.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from celery import shared_task


@shared_task
def scrape_live_data(live_url):
    driver_path = "C:\\Users\\Marcos\\Desktop\\LIVE SCRAPER\\drivers\\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    try:
        driver.get(live_url)
        time.sleep(5)  # Aguarde o carregamento da página

        live_title = driver.find_element(
            By.XPATH, "//div[@data-e2e='user-profile-live-title']"
        ).text

        views = driver.find_element(
            By.XPATH, "//div[@data-e2e='live-people-count']"
        ).text

        likes = driver.find_element(
            By.XPATH, "//div[@class='css-i3v4z1-DivLikeCount exkv4261']"
        ).text

        return {"live_title": live_title, "views": views, "likes": likes}

    except Exception as e:
        return {"error": str(e)}

    finally:
        driver.quit()
