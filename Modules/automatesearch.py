from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
def checkDriver():
    os.chdir("C:")
    c = os.listdir()
    if("chromedriver.exe" in c):
        return True
    else:
        return False

def startChrome():
    search=input("Enter Search Keyword: ")
    chrome_options = Options() 
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe",options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    m = driver.find_element_by_name("q")
    m.send_keys(search)
    time.sleep(0.2)
    m.send_keys(Keys.ENTER)
    time.sleep(4)
    os.system("cls")
    input("Press Enter key to continue")
def search():
    if checkDriver()==True:
        startChrome()
    else:
        print("Download Chrome Driver from https://chromedriver.chromium.org/downloads")
        
        input("Press Enter key to continue")

#Akshay