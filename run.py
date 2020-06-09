from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from secrets import souncloud_playlist

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 100)

driver.get(souncloud_playlist)

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
time.sleep(3)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'trackItem__trackTitle')))
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'trackItem__username')))
songs = []
artists = []
for elm in driver.find_elements_by_css_selector(".trackItem__trackTitle"):
    songs.append(elm.text)
for elm in driver.find_elements_by_css_selector(".trackItem__username"):
    artists.append(elm.text)
driver.quit()
