from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Driver:
    def __init__(self):
        try:
            self.driver = webdriver.Firefox().get("https://www.youtube.com/")
        except Exception:
            print ("Error occurred finding driver.exe")

    def search_query(self, query):
        search = self.driver.find_element(By.ID, "search")
        search.send_keys(query)
        search.send_keys(Keys.ENTER)
        search = self.driver.find_element(By.ID, "video-title")
        href_value = search.get_attribute("href")
        return ( f"https://www.youtube.com/{href_value}")


    def selenium_driver():
        pass