# Using xpath get total no of followers in guvi instagram

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class GuviInstaPage:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(10)

    def quit(self):
        self.driver.quit()

    def getNumberOfFollowers(self):
        xpath='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button/span/span'
        return self.driver.find_element(by=By.XPATH, value=xpath).text

url="https://www.instagram.com/guviofficial/"

obj=GuviInstaPage(url)
obj.boot()
followers=obj.getNumberOfFollowers()
print("Total number of Followers:",followers)
obj.quit()