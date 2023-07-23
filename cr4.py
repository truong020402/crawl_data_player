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
driver.get("https://www.transfermarkt.com/")
time.sleep(10)
filename = 'link1.txt' 
with open(filename, 'r') as file:
    lines = file.readlines()  # Đọc toàn bộ nội dung của tệp thành danh sách các dòng
    i = 0
    for link in lines:
        link = link.strip()  # Loại bỏ ký tự xuống dòng và khoảng trắng thừa từ đầu và cuối dòng
        print(link)
        
        driver.get(link)
        time.sleep(random.randint(4,6))
        # Tính toán chiều cao của trang
        page_height = driver.execute_script("return document.documentElement.scrollHeight")

        # Tính toán vị trí cần cuộn đến
        scroll_position = int(page_height * 0.8)

        # Thực thi mã JavaScript để cuộn đến vị trí mong muốn
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(5)
        #driver.switch_to.default_content()
        data = []
        mains = driver.find_element(By.ID, "main")
        soup =  BeautifulSoup(mains.get_attribute("innerHTML"), "html.parser")
        
        club = soup.find("div", class_="data-header__box--big")
        info = soup.find("div", class_="data-header__info-box")
        value = soup.find("div", class_="tm-player-market-value-development__current-value").get_text(strip=True)
        print(value)
        tb = soup.find("div", class_="grid-table") #grid-table
        #print(tb)
        ban_thang = tb.find_all("div", class_="grid__cell grid__cell--center svelte-8sjxq3")[-5:]
                                              #"grid__cell grid__cell--center svelte-8sjxq3"
        print(ban_thang)
        print(type(ban_thang))
        danh_hieu = soup.find("div", class_="data-header__badge-container")
        #//*[@id="main"]/main/div[3]/div[1]/div[7]
        #break
        with open("data_players.csv", "a", newline="",encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            #
            try:
                name_club = club.find("span", class_="data-header__club")
                name_club = name_club.find("a")["title"]
                print(name_club)
                data.append(name_club)
            except:
                print("loi ten club")
                data.append("")
            #
            index = 1
            infos = info.find_all("span", class_="data-header__content")
            for in4 in infos:
                if index == 1 or index == 4 or index == 5:
                    print(in4.get_text(strip=True))
                    data.append(in4.get_text(strip=True))
                index += 1
                
            #
            #bts = ban_thang.find_all("div", class_="grid__cell grid__cell--center svelte-8sjxq3")
            for bt in ban_thang:
                data.append(bt.get_text(strip = True))
                print(bt.get_text(strip = True))
            #
            try:
                dh = len(danh_hieu.find_all("a"))
                print(dh)
                data.append(dh)
            except:
                print("Khong danh hieu")
                data.append(0)
            #
            data.append(value)
            writer.writerow(data)
            print(f"Done page {link}!")
                
        
        
             
