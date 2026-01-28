from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import random

WEAPONS = {
    "Knives":{
        "file_name" : r"databases\Knives.csv", 
        "link" : "https://csgoskins.gg/types/knife?order=alphabetically&page=1",
    },
    "Gloves":{
        "file_name" : r"databases\Gloves.csv",
        "link" : "https://csgoskins.gg/types/gloves?order=alphabetically&page=1",
    },
    "Shotguns":{
        "file_name" : r"databases\STG.csv",
        "link" : "https://csgoskins.gg/types/shotgun?order=alphabetically&page=1",
    },
    "Snipers":{
        "file_name" : r"databases\Snipers.csv",
        "link" : "https://csgoskins.gg/types/sniper-rifle?order=alphabetically&page=1",
    },
    "LMG":{
        "file_name" : r"databases\LMG.csv",
        "link" : "https://csgoskins.gg/types/machinegun?order=alphabetically&page=1",
    },
    "Pistols":{
        "file_name" : r"databases\Pistols.csv",
        "link" : "https://csgoskins.gg/types/pistol?order=alphabetically&page=1",
    },
    "Rifles":{
        "file_name" : r"databases\Rifles.csv",
        "link" : "https://csgoskins.gg/types/rifle?order=alphabetically&page=1",
    },
    "SMG":{
        "file_name" : r"databases\SMG.csv",
        "link" : "https://csgoskins.gg/types/smg?order=alphabetically&page=1",
    }
}

def run_parser():
#Edge options
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # turn on if you want to sillenium work without window

    driver_path = r"C:\Users\nazar\Desktop\Programming\TgBot\msedge_driver\msedgedriver.exe"
    driver = webdriver.Edge(service=Service(driver_path), options=options)

    BASE_URL = "https://csgoskins.gg"


    #categories cycle

    for cat, data in WEAPONS.items():
        filename = data["file_name"]
        start_url = data["link"]

        print(f"\n=== CATEGORY: {cat} ===")
        print("START URL:", start_url)

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Gun", "Skin", "Image", "Price Link", "Min_Price", "Max_Price"])

            
            driver.get(start_url)
            try:
                
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "span.block.text-gray-400"))
                )
            except:
                print("❌ Page didn't load:", start_url)
                continue

            soup = BeautifulSoup(driver.page_source, "html.parser")

            pages_found = []
            # find all numbers of pages for pagination
            pages = soup.find_all(
                "a",
                class_="flex items-center px-4 py-2 text-sm font-medium text-blue-100 bg-gray-700 border-r border-gray-800 transition-colors hover:text-white hover:bg-gray-600 focus:outline-hidden"
            )

            # MAKE A LIST OF ALL PAGES
            pages_found = [p.get("href") for p in pages if p.get("href")]
            pages_found.insert(0, start_url)  # ADD FIRST PAGE


            if not pages_found:
                pages_found.append(start_url)

        
            for url in pages_found:
                print("PAGE:", url)
                driver.get(url)

                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "span.block.text-gray-400"))
                    )
                except:
                    print("❌ Elements didn't load:", url)
                    continue

                soup = BeautifulSoup(driver.page_source, "html.parser")
                time.sleep(0.3)
                guns = soup.find_all("span", class_="block text-gray-400 text-sm truncate")
                skins = soup.find_all("span", class_="block text-lg leading-7 truncate")
                imgs = soup.find_all("img", class_="mx-auto max-h-[237px]")
                links = soup.find_all(
                    "a",
                    class_="absolute left-0 right-0 bottom-0 rounded-b-sm "
                        "bg-gray-700 hover:bg-gray-600 transition-colors "
                        "text-center text-white py-2 focus:outline-hidden"
                )
                div_prices = soup.find_all(
                    "div",
                    class_="left-4 right-4 text-center text-lg absolute "
                        "whitespace-nowrap top-[395px]"
                )

                # check if data on page
                if not (guns and skins and imgs and links and div_prices):
                    print("❌ No data on page:", url)
                    continue

                min_list = []
                max_list = []
                for p in div_prices:
                    prices = p.find_all("a")
                    if len(prices) == 2:
                        min_list.append(prices[0])
                        max_list.append(prices[1])

            
                min_len = min(len(guns), len(skins), len(imgs), len(links), len(min_list), len(max_list))
                if min_len == 0:
                    print("❌ Empty data after check:", url)
                    continue

            #COMPLETING CSV
                for gun, skin, img, link, min_p, max_p in zip(guns[:min_len], skins[:min_len], imgs[:min_len],
                                                            links[:min_len], min_list[:min_len], max_list[:min_len]):
                    writer.writerow([
                        gun.text.strip(),
                        skin.text.strip(),
                        img.get("src"),
                        link.get("href"),
                        min_p.text.strip(),
                        max_p.text.strip(),
                    ])

            print("✔ Category finished:", cat)
            time.sleep(random.uniform(1, 3))


    driver.quit()
    print("✅ All data collected!")
