from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import KeyboardBuilder, ReplyKeyboardBuilder, InlineKeyboardBuilder
import pandas as pd
import re
import numpy as np

df = pd.read_csv("databases\knives.csv")
df_rifles = pd.read_csv("databases\Rifles.csv")
skin_row = list(df.iloc[:, 1])
skin_rifles_row = list(df_rifles.iloc[:, 1])


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Knifes")],
        # [KeyboardButton(text='Gloves')],
        [KeyboardButton(text='Rifles')], 
        #KeyboardButton(text='Pistols')],
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

riflesN =[
    "AK-47",
    "M4A4",
    "M4A1-S",
    "AUG",
    "SG 553",
    "FAMAS",
    "Galil AR",
]





async def all_knifes():             #all knife types
    keyboard = ReplyKeyboardBuilder()

    for knife in knifesN:
        keyboard.add(KeyboardButton(text=knife))

    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()

async def all_skins(knife_name: str):           #all knife skins
    keyboard = ReplyKeyboardBuilder()
    
    skins = df.loc[df.iloc[:, 0] == knife_name, df.columns[1]]
    
    for skin in skins:
        keyboard.add(KeyboardButton(text=str(skin)))
        
    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()

async def skins_data(knife_name: str,knife_skin: str):              #knife link, pics, min and max prices
    k = InlineKeyboardBuilder()
    links = df.loc[
        (df.iloc[:, 0] == knife_name) & (df.iloc[:, 1] == knife_skin),
        df.columns[3]
    ]
    
    pics = df.loc[
        (df.iloc[:, 0] == knife_name) & (df.iloc[:, 1] == knife_skin),
        df.columns[2]
    ]
    min_prices = df.loc[
        (df.iloc[:,0] == knife_name) & (df.iloc[:, 1] == knife_skin),
        df.columns[4]
    ]
    
    max_prices = df.loc[
        (df.iloc[:,0] == knife_name) & (df.iloc[:, 1] == knife_skin),
        df.columns[5]
    ]
    
    
    pic_url = pics.iloc[0] if not pics.empty else None
    min_price = min_prices.iloc[0] if not min_prices.empty else None
    max_price = max_prices.iloc[0] if not max_prices.empty else None
    
    for link in links:
        k.button(text="All current prices", url=str(link))
    
    keyboard = k.adjust(1).as_markup()
    
    
    return keyboard, pic_url, min_price, max_price
#-------------------------------------------------------------------------------------------

async def all_rifles():             #all rifle types
    keyboard = ReplyKeyboardBuilder()

    for rifle in riflesN:
        keyboard.add(KeyboardButton(text=rifle))

    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()



async def all_rifle_skins(rifle_name: str):           #all knife skins
    keyboard = ReplyKeyboardBuilder()
    
    skins = df_rifles.loc[df_rifles.iloc[:, 0] == rifle_name, df_rifles.columns[1]]
    
    for skin in skins:
        keyboard.add(KeyboardButton(text=str(skin)))
        
    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()


async def rifle_skins_data(rifle_name: str,rifle_skin: str):              #rifle link, pics, min and max prices
    k = InlineKeyboardBuilder()
    links = df_rifles.loc[
        (df_rifles.iloc[:, 0] == rifle_name) & (df_rifles.iloc[:, 1] == rifle_skin),
        df_rifles.columns[3]
    ]
    
    pics = df_rifles.loc[
        (df_rifles.iloc[:, 0] == rifle_name) & (df_rifles.iloc[:, 1] == rifle_skin),
        df_rifles.columns[2]
    ]
    min_prices = df_rifles.loc[
        (df_rifles.iloc[:,0] == rifle_name) & (df_rifles.iloc[:, 1] == rifle_skin),
        df_rifles.columns[4]
    ]
    
    max_prices = df_rifles.loc[
        (df_rifles.iloc[:,0] == rifle_name) & (df_rifles.iloc[:, 1] == rifle_skin),
        df_rifles.columns[5]
    ]
    
    
    pic_url = pics.iloc[0] if not pics.empty else None
    min_price = min_prices.iloc[0] if not min_prices.empty else None
    max_price = max_prices.iloc[0] if not max_prices.empty else None
    
    for link in links:
        k.button(text="All current prices", url=str(link))
    
    keyboard = k.adjust(1).as_markup()
    
    
    return keyboard, pic_url, min_price, max_price
        


   
    
 


    
        
    