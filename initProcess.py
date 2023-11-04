from pyvirtualdisplay import Display
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class initProcess():
    def start_options(url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--disable-dev-shm-usage")
        #display = Display(visible=0, size= (800, 600))
        #display.start()
        driver = webdriver.Chrome('/Users/seungjeajoo/Library/Mobile Documents/com~apple~CloudDocs/Documents/Live-Metro-main/chromedriver',  options = chrome_options)
        #driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
        driver.get(url)
        return driver

    def find_start(driver, station):
        find_timetable = driver.find_element(By.CSS_SELECTOR, '#txtStation')
        find_timetable.send_keys(station)
        other_trains = driver.find_element(By.CSS_SELECTOR, '#chkTrainTypeETC')
        other_trains.click()
        new_window = driver.find_element(By.CSS_SELECTOR, '#chkNewWindow')
        #new_window.click()
        pass_train = driver.find_element(By.CSS_SELECTOR, '#chkSkip')
        #pass_train.click()
