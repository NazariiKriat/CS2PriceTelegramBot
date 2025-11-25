from bs4 import BeautifulSoup
import requests
import csv

filename = "knives.csv"
n = 1

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.2210.91"
}




with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Knife", "Skin", "Image", "Price Link"])
    while n <= 13:
        url = f"https://csgoskins.gg/types/knife?page={n}"

        response = requests.get(url, headers=headers)

        print("Status:", response.status_code)

        soup = BeautifulSoup(response.text, "html.parser")

        knifes = soup.find_all("span", class_ ="block text-gray-400 text-sm truncate") 
        skins = soup.find_all("span", class_ ="block text-lg leading-7 truncate")
        imgs = soup.find_all("img", class_="mx-auto max-h-[237px]")
        links = soup.find_all("a", class_ = "absolute left-0 right-0 bottom-0 rounded-b-sm bg-gray-700 hover:bg-gray-600 transition-colors text-center text-white py-2 focus:outline-hidden")
        
        
        
        for knife, skin, img, link in zip(knifes, skins, imgs, links):
            name = knife.text.strip()
            skin_name = skin.text.strip()
            img_url = img.get("src")
            link_url = link.get("href")  
            writer.writerow([name, skin_name, img_url, link_url])
        n+=1

print("Data changed")
print(url)
