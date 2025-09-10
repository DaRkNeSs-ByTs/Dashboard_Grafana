import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = "usuario"
password = "senha"

urls = [
    "URL que deseas mostrar no dashboard",
]

login_url = "URL de login do dashboard"

chrome_options = Options()
chrome_options.add_argument("--kiosk") 
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(login_url)
time.sleep(3)

driver.find_element(By.NAME, "user").send_keys(username)

driver.find_element(By.NAME, "password").send_keys(password)

driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

time.sleep(5)

for i, url in enumerate(urls):
    if i == 0:
        driver.get(url)
    else:
        driver.execute_script(f"window.open('{url}');")

while True:
    for i in range(len(urls)):
        driver.switch_to.window(driver.window_handles[i])
        time.sleep(15)
