from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import KeyboardBuilder, ReplyKeyboardBuilder, InlineKeyboardBuilder
import pandas as pd
import re

df = pd.read_csv(r"databases\Knives.csv")
df_rifles = pd.read_csv(r"databases\Rifles.csv")
df_gloves = pd.read_csv(r"databases\Gloves.csv")
df_snipers = pd.read_csv(r"databases\Snipers.csv")
df_pistols = pd.read_csv(r"databases\Pistols.csv")
df_smgs = pd.read_csv(r"databases\SMG.csv")
df_stgs = pd.read_csv(r"databases\STG.csv")
df_lmgs = pd.read_csv(r"databases\LMG.csv")

skin_row = list(df.iloc[:, 1])
skin_rifles_row = list(df_rifles.iloc[:, 1])
skin_gloves_row = list(df_gloves.iloc[:, 1])
skin_snipers_row = list(df_snipers.iloc[:, 1])
skin_pistols_row = list(df_pistols.iloc[:, 1])
skin_smgs_row = list(df_smgs.iloc[:, 1])
skin_stgs_row = list(df_stgs.iloc[:, 1])
skin_lmgs_row = list(df_lmgs.iloc[:, 1])


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Knives'), KeyboardButton(text='Gloves')],
        [KeyboardButton(text='Snipers'), KeyboardButton(text='Rifles')], 
        [KeyboardButton(text='Pistols'), KeyboardButton(text='SMG')],
        [KeyboardButton(text='Shotguns'), KeyboardButton(text='LMG')],
        [KeyboardButton(text="Contacts")],
    ],
    resize_keyboard=False,
    input_field_placeholder="Choose something in menu",
)

catN = ['Knives','Gloves','Snipers','Rifles','Pistols','SMG','Shotguns','LMG']

# lists of all weapons in cs2 ->
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

glovesN = [
    "Bloodhound Gloves",
    "Broken Fang Gloves",
    "Driver Gloves",
    "Hand Wraps",
    "Hydra Gloves",
    "Moto Gloves",
    "Specialist Gloves",
    "Sport Gloves"
]
snipersN = [
                  "AWP",
                  "G3SG1",
                  "SCAR-20",
                  "SSG 08"
                  ]

pistolsN = [
    "Glock-18",
    "USP-S",
    "P2000",
    "P250",
    "Five-SeveN",
    "Tec-9",
    "CZ75-Auto",
    "Desert Eagle",
    "R8 Revolver",
    "Dual Berettas"
] 

smgN = [
    "MP7",
    "MP9",
    "MAC-10",
    "UMP-45",
    "MP5-SD",
    "P90",
    "PP-Bizon"
]

stgN = [
    "Nova",
    "XM1014",
    "MAG-7",
    "Sawed-Off",
]

lmgN = [
    "Negev",
    "M249",
]






DB = {
    "Knives": {
        "df" : pd.read_csv(r"databases\Knives.csv"),
        "weapons": knifesN,
        "skins": skin_row
    },
    "Rifles": {
        "df" : pd.read_csv(r"databases\Rifles.csv"),
        "weapons": riflesN,
        "skins": skin_rifles_row
    },
    "Gloves": {
        "df" : pd.read_csv(r"databases\Gloves.csv"),
        "weapons": glovesN,
        "skins": skin_gloves_row
    },
    "Snipers": {
        "df" : pd.read_csv(r"databases\Snipers.csv"),
        "weapons": snipersN,
        "skins": skin_snipers_row
    },
    "Pistols": {
        "df" : pd.read_csv(r"databases\Pistols.csv"),
        "weapons": pistolsN,
        "skins": skin_pistols_row
    },
    "SMG": {
        "df" : pd.read_csv(r"databases\SMG.csv"),
        "weapons": smgN,
        "skins": skin_smgs_row
    },
    "Shotguns": {
        "df" : pd.read_csv(r"databases\STG.csv"),
        "weapons": stgN,
        "skins": skin_stgs_row
    },
    "LMG": {
        "df" : pd.read_csv(r"databases\LMG.csv"),
        "weapons": lmgN,
        "skins": skin_lmgs_row
    }
}





async def all_weapons(item_type: str):             #all weapon types
    keyboard = ReplyKeyboardBuilder()

    weapons = DB[item_type]["weapons"]
    for weapon in weapons:
        keyboard.add(KeyboardButton(text=str(weapon)))
    
    

    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()

async def all_skins(item_type: str, item_name: str):           #all weapon skins
    keyboard = ReplyKeyboardBuilder()
    df = DB[item_type]["df"]
    
    skins = df.loc[df.iloc[:, 0] == item_name, df.columns[1]]
    
    for skin in skins:
        keyboard.add(KeyboardButton(text=str(skin)))
        
    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()

async def skins_data(item_type: str, item_name: str,item_skin: str):              #weapon link, pics, min and max prices
    k = InlineKeyboardBuilder()
    df = DB[item_type]["df"]
    links = df.loc[
        (df.iloc[:, 0] == item_name) & (df.iloc[:, 1] == item_skin),
        df.columns[3]
    ]
    
    pics = df.loc[
        (df.iloc[:, 0] == item_name) & (df.iloc[:, 1] == item_skin),
        df.columns[2]
    ]
    min_prices = df.loc[
        (df.iloc[:,0] == item_name) & (df.iloc[:, 1] == item_skin),
        df.columns[4]
    ]
    
    max_prices = df.loc[
        (df.iloc[:,0] == item_name) & (df.iloc[:, 1] == item_skin),
        df.columns[5]
    ]
    
    pic_url = pics.iloc[0] if not pics.empty else None
    min_price = min_prices.iloc[0] if not min_prices.empty else None
    max_price = max_prices.iloc[0] if not max_prices.empty else None
    
    for link in links:
        k.button(text="All current prices", url=str(link))
    
    keyboard = k.adjust(1).as_markup()
    
    
    return keyboard, pic_url, min_price, max_price
# -------------------------------------------------------------------------------------------


    


