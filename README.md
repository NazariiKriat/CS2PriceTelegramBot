# 🎮 CS2 Skins Price Bot

## 📌 Project Overview

**CS2 Skins Price Bot** is an **asynchronous Telegram bot** that helps users quickly find up-to-date prices for **CS2 (Counter-Strike 2) weapon skins**.

Instead of manually browsing multiple websites, users can simply search for a skin inside Telegram and instantly receive:

* 🖼️ Weapon skin image
* 🔗 Link to buy the skin
* 💰 Minimum and maximum current prices

This makes checking CS2 skin prices **fast, convenient, and user-friendly**.

---

## ✨ Features

* 🔍 Fast search for CS2 weapon skins
* 🖼️ Displays weapon skin images
* 🔗 Provides direct purchase links
* 💰 Shows minimum and maximum prices
* ⚡ Fully asynchronous for high performance
* 📱 Works directly inside Telegram

---

## 🛠️ Tech Stack

* **Python**
* **Aiogram** (Telegram Bot Framework)
* **Asyncio** (Asynchronous programming)
* **Pandas** (Data processing)
* **Beautiful Soup** (Web scraping)
* **CSV database** (Data storage)

---

## 🚀 Getting Started

### 📦 Requirements

Make sure you have **Python 3.10+** installed.

Install required dependencies:

```bash
pip install -r requirements.txt
```

### ▶️ Run the Bot

Start the bot with:

```bash
python run.py
```

---

## 📖 How It Works

1. User opens the Telegram bot
2. Enters the name of a CS2 weapon skin
3. Bot asynchronously processes the request
4. User receives:

   * Weapon skin image
   * Purchase link
   * Minimum price
   * Maximum price

---

## 🎯 Purpose

This project was created as a **pet project and school project**.

In the future, it can be:

* Improved
* Optimized
* Scaled into a **production-ready application**

---

## 🧪 Example Use Case

* Quickly searching CS2 skin prices via Telegram
* Comparing minimum and maximum prices
* Finding a weapon skin without opening multiple websites

---

## 📂 Project Structure

```text
├── run.py
├── config.py
├── app/
│   ├── handlers.py
│   └── keyboards.py
├── databases/
│   ├── Knives.csv
│   ├── Gloves.csv
│   ├── Pistols.csv
│   ├── Rifles.csv
│   ├── SMGs.csv
│   ├── Snipers.csv
│   └── LMG.csv
├── webscrapers/
│   ├── webscraper.py
│   ├── webscraper_knives.py
│   ├── webscraper_gloves.py
│   ├── webscraper_pistols.py
│   ├── webscraper_rifles.py
│   ├── webscraper_smgs.py
│   ├── webscraper_snipers.py
│   └── webscraper_lmgs.py
├── venv/
├── requirements.txt
└── README.md
```

---

## 📌 Future Improvements

* 🔔 Price alerts
* 📊 Price history charts
* 🗄️ Replace CSV with a database (PostgreSQL / SQLite)
* 🌍 Multi-language support

---

## 📄 License

This project is intended for **educational and personal use**.

---

## 👤 Author

Developed by Nazarii Kriat as a personal and school project.

---

⭐ If you like this project, consider giving it a star on GitHub!
