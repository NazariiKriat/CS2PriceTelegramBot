import sqlite3
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


conn = sqlite3.connect("main.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()



def main_menu():
    kb = ReplyKeyboardBuilder()

    cursor.execute("SELECT name FROM categories ORDER BY name")
    for row in cursor.fetchall():
        kb.add(KeyboardButton(text=row["name"]))

    kb.add(KeyboardButton(text="Contacts"))
    return kb.adjust(2).as_markup(
        resize_keyboard=True,
        input_field_placeholder="Choose something in menu"
    )



async def all_weapons(category_name: str):
    kb = ReplyKeyboardBuilder()

    cursor.execute("""
        SELECT guns.name
        FROM guns
        JOIN categories ON guns.category_id = categories.id
        WHERE categories.name = ?
        ORDER BY guns.name
    """, (category_name,))

    for row in cursor.fetchall():
        kb.add(KeyboardButton(text=row["name"]))

    kb.add(KeyboardButton(text="Main Menu"))
    return kb.adjust(2).as_markup(resize_keyboard=True)


async def all_skins(category_name: str, gun_name: str):
    kb = ReplyKeyboardBuilder()

    cursor.execute("""
        SELECT skins.skin
        FROM skins
        JOIN guns ON skins.gun_id = guns.id
        JOIN categories ON guns.category_id = categories.id
        WHERE categories.name = ?
          AND guns.name = ?
        ORDER BY skins.skin
    """, (category_name, gun_name))

    for row in cursor.fetchall():
        kb.add(KeyboardButton(text=row["skin"]))

    kb.add(KeyboardButton(text="Main Menu"))
    return kb.adjust(2).as_markup(resize_keyboard=True)


async def skins_data(category_name: str, gun_name: str, skin_name: str):
    kb = InlineKeyboardBuilder()

    cursor.execute("""
        SELECT skins.image,
               skins.price_link,
               skins.min_price,
               skins.max_price
        FROM skins
        JOIN guns ON skins.gun_id = guns.id
        JOIN categories ON guns.category_id = categories.id
        WHERE categories.name = ?
          AND guns.name = ?
          AND skins.skin = ?
        LIMIT 1
    """, (category_name, gun_name, skin_name))

    row = cursor.fetchone()

    if not row:
        return None, None, None, None

    if row["price_link"]:
        kb.button(
            text="All current prices",
            url=row["price_link"]
        )

    return (
        kb.adjust(1).as_markup(),
        row["image"],
        row["min_price"],
        row["max_price"]
    )
