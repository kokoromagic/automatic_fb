from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fb_getcookies import __chrome_driver__
import time
import os

try:
    drivers = []
    scoped_dir = os.getenv("SCPDIR")
    for opt in [
        (scoped_dir, False, True),
    ]:
        driver = __chrome_driver__(*opt)
        driver.get("https://deviceandbrowserinfo.com/are_you_a_bot")
        drivers.append(driver)
    time.sleep(5)
    for driver in drivers:
        wait = WebDriverWait(driver, 20)
        wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        resultsBotTest = driver.find_element(By.ID, "resultsBotTest").text
        resultsBotTestDetails = driver.find_element(By.ID, "resultsBotTestDetails").text
        print("resultsBotTest:", resultsBotTest)
        print("resultsBotTestDetails:", resultsBotTestDetails)
        driver.quit()
    
except Exception as e:
    print(e)
finally:
    for driver in drivers:
        driver.quit()
