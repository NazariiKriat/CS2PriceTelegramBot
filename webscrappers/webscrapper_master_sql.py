import sqlite3
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WEAPONS = {
    "Knives": {"link": "https://csgoskins.gg/types/knife?order=alphabetically&page=1"},
    "Gloves": {"link": "https://csgoskins.gg/types/gloves?order=alphabetically&page=1"},
    "Shotguns": {"link": "https://csgoskins.gg/types/shotgun?order=alphabetically&page=1"},
    "Snipers": {"link": "https://csgoskins.gg/types/sniper-rifle?order=alphabetically&page=1"},
    "LMG": {"link": "https://csgoskins.gg/types/machinegun?order=alphabetically&page=1"},
    "Pistols": {"link": "https://csgoskins.gg/types/pistol?order=alphabetically&page=1"},
    "Rifles": {"link": "https://csgoskins.gg/types/rifle?order=alphabetically&page=1"},
    "SMG": {"link": "https://csgoskins.gg/types/smg?order=alphabetically&page=1"},
}


def run_parser():
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS guns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category_id INTEGER,
        UNIQUE(name, category_id),
        FOREIGN KEY (category_id) REFERENCES categories(id)
    );

    CREATE TABLE IF NOT EXISTS skins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gun_id INTEGER,
        skin TEXT,
        image TEXT,
        price_link TEXT,
        min_price REAL,
        max_price REAL,
        FOREIGN KEY (gun_id) REFERENCES guns(id)
    );
    """)

    conn.commit()


    def get_or_create_category(name):
        cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (name,))
        conn.commit()
        cursor.execute("SELECT id FROM categories WHERE name = ?", (name,))
        return cursor.fetchone()[0]

    def get_or_create_gun(name, category_id):
        cursor.execute(
            "INSERT OR IGNORE INTO guns (name, category_id) VALUES (?, ?)",
            (name, category_id)
        )
        conn.commit()
        cursor.execute(
            "SELECT id FROM guns WHERE name = ? AND category_id = ?",
            (name, category_id)
        )
        return cursor.fetchone()[0]

    def parse_price(text):
        return float(text.replace("$", "").strip())


    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    driver_path = r"C:\Users\nazar\Desktop\Programming\TgBot\msedge_driver\msedgedriver.exe"
    driver = webdriver.Edge(service=Service(driver_path), options=options)

    for category_name, data in WEAPONS.items():
        print(f"\n=== CATEGORY: {category_name} ===")
        category_id = get_or_create_category(category_name)

        driver.get(data["link"])

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.block.text-gray-400"))
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")

        pages = soup.find_all("a", class_="flex items-center px-4 py-2 text-sm font-medium")
        pages_found = [p.get("href") for p in pages if p.get("href")]
        pages_found.insert(0, data["link"])

        for url in pages_found:
            driver.get(url)
            time.sleep(0.5)

            soup = BeautifulSoup(driver.page_source, "html.parser")

            guns = soup.find_all("span", class_="block text-gray-400 text-sm truncate")
            skins = soup.find_all("span", class_="block text-lg leading-7 truncate")
            imgs = soup.find_all("img", class_="mx-auto max-h-[237px]")
            links = soup.find_all("a", class_="absolute left-0 right-0 bottom-0 rounded-b-sm")
            prices = soup.find_all("div", class_="left-4 right-4 text-center text-lg absolute")

            min_list, max_list = [], []
            for p in prices:
                a = p.find_all("a")
                if len(a) == 2:
                    min_list.append(a[0])
                    max_list.append(a[1])

            for gun, skin, img, link, min_p, max_p in zip(
                guns, skins, imgs, links, min_list, max_list
            ):
                gun_name = gun.text.strip()
                gun_id = get_or_create_gun(gun_name, category_id)

                cursor.execute("""
                    INSERT INTO skins (
                        gun_id, skin, image, price_link, min_price, max_price
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    gun_id,
                    skin.text.strip(),
                    img.get("src"),
                    link.get("href"),
                    parse_price(min_p.text),
                    parse_price(max_p.text),
                ))

            conn.commit()
            print("✔ Page done:", url)

        time.sleep(random.uniform(1, 3))

    driver.quit()
    conn.close()
    print("✅ All data saved into SQLite")
