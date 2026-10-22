import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

df = pd.read_excel(r"D:\Vihaan's download\challenge.xlsx")
print("Excel headers:", list(df.columns))

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rpachallenge.com/")
time.sleep(2)

input("Click START on the site, then press Enter...")

for i, row in df.iterrows():
    print(f"→ Filling form {i + 1}")
    for label, value in row.items():
        try:
            field = driver.find_element(By.XPATH, f"//*[@placeholder='{label.strip()}']")
            field.clear()
            for char in str(value):
                field.send_keys(char)
                time.sleep(random.uniform(0.03, 0.07))
        except Exception as e:
            print(f"⚠️ Could not fill '{label}': {e}")
    try:
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
    except:
        print("⚠️ Submit failed.")
    time.sleep(1)

print("✅ Done submitting all rows.")
driver.quit()
