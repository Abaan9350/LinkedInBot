from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# --- LOGIN DETAILS ---
username = "atemp@gmail.com"
password = "..." #Replace ... with your password

# --- SETUP CHROMEDRIVER ---
service = Service("chromedriver.exe")  # Make sure chromedriver.exe is in the same folder
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# --- LOGIN TO LINKEDIN ---
driver.get("https://www.linkedin.com/login")
time.sleep(3)

driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# --- GO TO 'MY NETWORK' PAGE ---
driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(5)

# --- SCROLL TO LOAD MORE CONNECTIONS ---
for i in range(3):  # You can increase this if you want to load more suggestions
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

# --- FIND AND CLICK ALL "CONNECT" BUTTONS ---
connect_buttons = driver.find_elements(By.XPATH, "//span[text()='Connect']/ancestor::button")

count = 0
for btn in connect_buttons:
    try:
        btn.click()
        time.sleep(2)  # Wait a bit between clicks
        count += 1
    except Exception as e:
        print("Skipped one button due to error:", e)
        continue

print(f"\n✅ Successfully sent {count} connection requests!")

# --- CLOSE BROWSER ---
driver.quit()
