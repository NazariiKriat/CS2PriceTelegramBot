# 🛠️ How to Start the Telegram Bot

To start this Telegram bot you need to complete a few steps such as:

1. Install all the Python libraries:

   ```bash
   pip install aiogram pandas beautifulsoup4
   ```

2. Get your own bot token through **BotFather** in Telegram and insert it into the `TOKEN` variable in the `config.py` file

3. Then just run the `run.py` file in the terminal:

   ```bash
   python run.py
   ```

---

## 🌐 Using Web Scrapers

If you want to use **web scrapers**, they will generate new CSV files containing all skins and related data. However, sometimes duplicate entries may appear.

In that case, you need to use `rem_dub.py`. This script removes all duplicates from the CSV files and recreates them as new files.

**VERY IMPORTANT:** the names of the recreated CSV files must be exactly the same as the original ones.

