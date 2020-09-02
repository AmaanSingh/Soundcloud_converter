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
"""
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
time.sleep(5)
"""
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'trackItem__trackTitle')))
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'trackItem__username')))
songs1 = []
songs = []
artists = []

for elm in driver.find_elements_by_css_selector(".trackItem__trackTitle"):
    songs1.append(elm.text)
for elm in driver.find_elements_by_css_selector(".trackItem__username"):
    artists.append(elm.text)
driver.quit()

for i in songs1:
    try:
        song2 = i.split('- ')[1]
        songs.append(song2)
    except Exception:
        songs.append(i)
