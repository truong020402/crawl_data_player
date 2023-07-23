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

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()

filename = 'D:\\HK6\\KHDL\\data_link.txt' 
with open(filename, 'r') as file:
    lines = file.readlines()  # Đọc toàn bộ nội dung của tệp thành danh sách các dòng
    i = 0
    for link in lines:
        link = link.strip()  # Loại bỏ ký tự xuống dòng và khoảng trắng thừa từ đầu và cuối dòng
        print(link)
        
        driver.get(link)
        time.sleep(random.randint(10,15))
        #driver.switch_to.default_content()
        
        club =  driver.find_element(By.XPATH, '//*[@id="main"]/main/header/div[4]/div')
        info = driver.find_element(By.XPATH, '//*[@id="main"]/main/header/div[6]')
        try:
            thanh_tich = driver.find_element(By.XPATH, '//*[@id="main"]/main/header/div[3]')
        except:
            thanh_tich = ""
            print("Could not find")
        value = driver.find_element(By.XPATH, '//*[@id="main"]/main/div[3]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]')
        ban_thang = driver.find_element(By.ID, 'player-performance-table')
        #//*[@id="main"]/main/div[3]/div[1]/div[7]
        data = []
        with open("data_players.csv", "a", newline="",encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
                #
            info_soup = BeautifulSoup(info.get_attribute("innerHTML"), "html.parser")
            rows = info_soup.find_all("span", class_="data-header__content")
            for row in rows:
                text = row.get_text(strip=True)
                data.append(text)
                #
            club_soup = BeautifulSoup(club.get_attribute("innerHTML"),"html.parser")
            try:
                name_club = club_soup.find("a")["title"]
                print(name_club)
                data.append(name_club)
            except:
                print("loi ten club")
                data.append("")
            #
            thanh_tich_soup = BeautifulSoup(thanh_tich.get_attribute("innerHTML"),"html.parser")
            ths = len(thanh_tich_soup.find_all("span", class_="data-header__success-number"))
            print(ths)
            data.append(ths)
                #
            ban_thang_soup = BeautifulSoup( ban_thang.get_attribute("innerHTML"), "html.parser")
            bts = ban_thang_soup.find_all("div", class_="grid__cell grid__cell--center svelte-8sjxq3")
            print(ban_thang_soup)
            for bt in bts:
                print(bt.get_text())
                data.append(bt.get_text())
                #    
            vl = BeautifulSoup(value.get_attribute("innerHTML"), "html.parser")
            vls = vl.find_all("div", class_="tm-player-market-value-development__current-value")
            for v in vls:
                data.append(v.get_text())
                print(v.get_text())
            #data.append(vl)
            writer.writerow(data)
            print(f"Done page {link}!")
                
        
        
             
