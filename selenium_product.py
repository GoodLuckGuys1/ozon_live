from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random

import lib.config

class UseSelenium:
    def __init__(self, url: str, filename: str):
        self.url = url
        self.filename = filename

    def save_page(self):

        options = webdriver.ChromeOptions()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.147 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")


        s = Service(executable_path="/lib/chromedriver")

        driver = webdriver.Chrome(options=options, service=s)

        try:
            driver.get(self.url)
            elem = driver.find_element(By.TAG_NAME, "pre").get_attribute('innerHTML')
            with open('products/' + self.filename, 'w', encoding='utf-8') as f:
                f.write(elem)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
