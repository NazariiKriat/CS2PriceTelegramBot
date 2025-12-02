from bs4 import BeautifulSoup
import requests
import csv

filename = "Rifles.csv"
n = 0

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.2210.91"
}




with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Gun", "Skin", "Image", "Price Link", "Min_Price", "Max_Price"])
    while n <= 7:
        url = f"https://csgoskins.gg/types/rifle?page={n}"

        response = requests.get(url, headers=headers)

        print("Status:", response.status_code)

        soup = BeautifulSoup(response.text, "html.parser")

        knifes = soup.find_all("span", class_ ="block text-gray-400 text-sm truncate") 
        skins = soup.find_all("span", class_ ="block text-lg leading-7 truncate")
        imgs = soup.find_all("img", class_="mx-auto max-h-[237px]")
        links = soup.find_all("a", class_ = "absolute left-0 right-0 bottom-0 rounded-b-sm bg-gray-700 hover:bg-gray-600 transition-colors text-center text-white py-2 focus:outline-hidden")
        div_prices = soup.find_all("div", class_="left-4 right-4 text-center text-lg absolute whitespace-nowrap top-[395px]")
        div_stat_prices = soup.find_all("div", class_="left-4 right-4 text-center text-lg absolute text-stattrak top-[420px]")
        
        min_list = []
        max_list = []
        
        stat_min_list = []
        stat_max_list = []
        
        for p in div_prices:
            price1, price2 = p.find_all("a")
            
            min_list.append(price1)
            max_list.append(price2)     
            
        
        
            
            
        
        for knife, skin, img, link, min_price, max_price  in zip(knifes, skins, imgs, links, min_list, max_list):
            name = knife.text.strip()
            skin_name = skin.text.strip()
            img_url = img.get("src")
            link_url = link.get("href")  
            price1 = min_price.text.strip()
            price2 = max_price.text.strip()
            
            writer.writerow([name, skin_name, img_url, link_url, price1, price2,])
        n+=1

print("Data changed")
print(url)