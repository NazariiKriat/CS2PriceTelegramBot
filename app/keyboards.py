from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import KeyboardBuilder, ReplyKeyboardBuilder, InlineKeyboardBuilder
import pandas as pd


df = pd.read_csv("knives.csv")
skin_row = list(df.iloc[:, 1])


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Knifes")],
        # [KeyboardButton(text='Gloves')],
        # [KeyboardButton(text='Rifles'), KeyboardButton(text='Pistols')],
        # [KeyboardButton(text='Shotguns'), KeyboardButton(text='SMG')],
        [KeyboardButton(text="Contacts")],
    ],
    resize_keyboard=False,
    input_field_placeholder="Choose something in menu",
)

knifesN = [
    "Bayonet",
    "M9 Bayonet",
    "Huntsman Knife",
    "Butterfly Knife",
    "Falchion Knife",
    "Bowie Knife",
    "Flip Knife",
    "Shadow Daggers",
    "Karambit",
    "Stiletto Knife",
    "Paracord Knife",
    "Gut Knife",
    "Survival Knife",
    "Navaja Knife",
    "Nomad Knife",
    "Classic Knife",
]

l1 = "Nothing"



async def all_knifes():
    keyboard = ReplyKeyboardBuilder()

    for knife in knifesN:
        keyboard.add(KeyboardButton(text=knife))

    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()

async def all_skins(knife_name: str):
    keyboard = ReplyKeyboardBuilder()
    
    skins = df.loc[df.iloc[:, 0] == knife_name, df.columns[1]]
    
    for skin in skins:
        keyboard.add(KeyboardButton(text=str(skin)))
        
    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()

async def skins_data(knife_skin: str):
    k = InlineKeyboardBuilder()
    links = df.loc[
        (df.iloc[:, 0] == l1) & (df.iloc[:, 1] == knife_skin),
        df.columns[3]
    ]
    
    pics = df.loc[
        (df.iloc[:, 0] == l1) & (df.iloc[:, 1] == knife_skin),
        df.columns[2]
    ]
    
    pic_url = pics.iloc[0] if not pics.empty else None
    
    for link in links:
        k.button(text="All current prices", url=str(link))
    
    keyboard = k.adjust(1).as_markup()
    
    
    return keyboard, pic_url
        


   
    
 


    
        
    