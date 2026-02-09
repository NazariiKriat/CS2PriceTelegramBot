from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import sqlite3

router = Router()

conn = sqlite3.connect("main.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()



def main_menu():
    kb = ReplyKeyboardBuilder()
    cursor.execute("SELECT name FROM categories")
    for row in cursor.fetchall():
        kb.button(text=row["name"])
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def back_menu():
    kb = ReplyKeyboardBuilder()
    kb.button(text="⬅ Main Menu")
    return kb.as_markup(resize_keyboard=True)



@router.message(F.text == "/start")
async def start(msg: Message):
    await msg.answer(
        "🔫 Choose a category:",
        reply_markup=main_menu()
    )


@router.message()
async def category_handler(msg: Message):
    cursor.execute("SELECT id FROM categories WHERE name = ?", (msg.text,))
    category = cursor.fetchone()

    if not category:
        return

    kb = ReplyKeyboardBuilder()
    cursor.execute(
        "SELECT name FROM guns WHERE category_id = ?",
        (category["id"],)
    )

    for row in cursor.fetchall():
        kb.button(text=row["name"])

    kb.button(text="⬅ Main Menu")
    kb.adjust(2)

    await msg.answer(
        f"🔫 {msg.text}:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )


@router.message()
async def gun_handler(msg: Message):
    cursor.execute("""
        SELECT guns.id FROM guns
        WHERE guns.name = ?
    """, (msg.text,))
    gun = cursor.fetchone()

    if not gun:
        return

    kb = ReplyKeyboardBuilder()
    cursor.execute(
        "SELECT skin FROM skins WHERE gun_id = ?",
        (gun["id"],)
    )

    for row in cursor.fetchall():
        kb.button(text=row["skin"])

    kb.button(text="⬅ Main Menu")
    kb.adjust(2)

    await msg.answer(
        f"🎨 Skins for {msg.text}:",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )



@router.message()
async def skin_handler(msg: Message):
    cursor.execute("""
        SELECT skins.image, skins.price_link,
               skins.min_price, skins.max_price
        FROM skins
        WHERE skins.skin = ?
        LIMIT 1
    """, (msg.text,))
    skin = cursor.fetchone()

    if not skin:
        return

    text = (
        f"💰 Min price: {skin['min_price']}$\n"
        f"💰 Max price: {skin['max_price']}$"
    )

    if skin["image"]:
        await msg.answer_photo(
            photo=skin["image"],
            caption=text
        )
    else:
        await msg.answer(text)

    if skin["price_link"]:
        await msg.answer(
            "🔗 Market link:",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        {
                            "text": "All current prices",
                            "url": skin["price_link"]
                        }
                    ]
                ]
            )
        )



@router.message(F.text == "⬅ Main Menu")
async def back(msg: Message):
    await msg.answer(
        "🏠 Main menu:",
        reply_markup=main_menu()
    )
