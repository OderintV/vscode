from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

data = [
    {'First Name': 'John', 'Last Name': 'Smith', 'Company Name': 'IT Solutions', 'Role in Company': 'Analyst', 'Address': '98 North Road', 'Email': 'jsmith@itsolutions.co.uk', 'Phone Number': '40716543298'},
    {'First Name': 'Jane', 'Last Name': 'Dorsey', 'Company Name': 'MediCare', 'Role in Company': 'Medical Engineer', 'Address': '11 Crown Street', 'Email': 'jdorsey@mc.com', 'Phone Number': '40791345621'},
    {'First Name': 'Albert', 'Last Name': 'Kipling', 'Company Name': 'Waterfront', 'Role in Company': 'Accountant', 'Address': '22 Guild Street', 'Email': 'kipling@waterfront.com', 'Phone Number': '40735416854'},
    {'First Name': 'Michael', 'Last Name': 'Robertson', 'Company Name': 'MediCare', 'Role in Company': 'IT Specialist', 'Address': '17 Farburn Terrace', 'Email': 'mrobertson@mc.com', 'Phone Number': '40733652145'},
    {'First Name': 'Doug', 'Last Name': 'Derrick', 'Company Name': 'Timepath Inc.', 'Role in Company': 'Analyst', 'Address': '99 Shire Oak Road', 'Email': 'dderrick@timepath.co.uk', 'Phone Number': '40799885412'},
    {'First Name': 'Jessie', 'Last Name': 'Marlowe', 'Company Name': 'Aperture Inc.', 'Role in Company': 'Scientist', 'Address': '27 Cheshire Street', 'Email': 'jmarlowe@aperture.us', 'Phone Number': '40733154268'},
    {'First Name': 'Stan', 'Last Name': 'Hamm', 'Company Name': 'Sugarwell', 'Role in Company': 'Advisor', 'Address': '10 Dam Road', 'Email': 'shamm@sugarwell.org', 'Phone Number': '40712462257'},
    {'First Name': 'Michelle', 'Last Name': 'Norton', 'Company Name': 'Aperture Inc.', 'Role in Company': 'Scientist', 'Address': '13 White Rabbit Street', 'Email': 'mnorton@aperture.us', 'Phone Number': '40731254562'},
    {'First Name': 'Stacy', 'Last Name': 'Shelby', 'Company Name': 'TechDev', 'Role in Company': 'HR Manager', 'Address': '19 Pineapple Boulevard', 'Email': 'sshelby@techdev.com', 'Phone Number': '40741785214'},
    {'First Name': 'Lara', 'Last Name': 'Palmer', 'Company Name': 'Timepath Inc.', 'Role in Company': 'Programmer', 'Address': '87 Orange Street', 'Email': 'lpalmer@timepath.co.uk', 'Phone Number': '40731653845'},
]


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://rpachallenge.com/")
time.sleep(2)

input("Click START on the site, then press Enter...")

for i, row in enumerate(data):
    for label, value in row.items():
        try:
            field = driver.find_element(By.XPATH, f"//label[text()='{label}']/following-sibling::input")
            field.clear()
            field.send_keys(str(value))
        except Exception as e:
            print(f"Could not fill '{label}': {e}")
    try:
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
    except:
        print("Submit failed.")
    time.sleep(0.2) 

print("Done submitting all rows.")
