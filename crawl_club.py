import numpy as np
import time 
from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv


from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get('https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?land_id=0&ausrichtung=alle&spielerposition_id=alle&altersklasse=alle&jahrgang=0&kontinent_id=0&plus=1')
# time.sleep(random.randint(10,15))
# # click1 = driver.find_element(By.XPATH,"//button[contains(text(), 'ACCEPT ALL')]")
# # click1.click()
# iframe = driver.find_element(By.ID, 'sp_message_iframe_764226')
# driver.switch_to.frame(iframe)

# WebDriverWait(driver, random.randint(10,15)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="notice"]/div[3]/div[2]/button'))).click()

driver.switch_to.default_content()

time.sleep(5)

# names =  driver.find_element(By.XPATH, '//*[@id="yw1"]/table/tbody')


# soup = BeautifulSoup(names.get_attribute("innerHTML"), "html.parser")
# rows = soup.find_all("tr", class_=["odd", "even"])
# with open("data.csv", "a", newline="",encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     for row in rows:
#         dt = []
#         cells = row.find_all("td")
#         i = 0
#         for cell in cells:
#             text = cell.get_text(strip=True)
#             dt.append(text)
#             try:
#                 img_elements = cell.find_all("img")
#                 countries = [img["title"] for img in img_elements]
#                 dt.append(countries[0])
#             except:
#                 print()
                
#             i += 1
#     #writer to file csv
#         writer.writerow(dt)
#         print("Done page 1!")


#time.sleep(random.randint(10,15))
for page in range(1,5):
    time.sleep(random.randint(6,10))
    link = 'https://www.transfermarkt.com/vereins-statistik/wertvollstemannschaften/marktwertetop?ajax=yw1&kontinent_id=0&land_id=0&page='+ str(page)
    driver.get(link)
    driver.switch_to.default_content()
    time.sleep(random.randint(10,15))

    names =  driver.find_element(By.XPATH, '//*[@id="yw1"]/table/tbody')


    soup = BeautifulSoup(names.get_attribute("innerHTML"), "html.parser")
    rows = soup.find_all("tr", class_=["odd", "even"])
    with open("data_clubs.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            dt = []
            cells = row.find_all("td")
            i = 0
            for cell in cells:
                text = cell.get_text(strip=True)
                dt.append(text)
                try:
                    img_elements = cell.find_all("img")
                    countries = [img["title"] for img in img_elements]
                    dt.append(countries[0])
                except:
                    print()
                    
                i += 1
        #writer to file csv
            writer.writerow(dt)
            print(f"Done page {page}!")
time.sleep(random.randint(10,15))
#print(driver.get_cookies())