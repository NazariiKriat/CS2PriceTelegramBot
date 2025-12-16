from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import KeyboardBuilder, ReplyKeyboardBuilder, InlineKeyboardBuilder
import pandas as pd
import re


df = pd.read_csv("databases\Knives.csv")                    #df module
df_rifles = pd.read_csv("databases\Rifles.csv")
df_gloves = pd.read_csv("databases\Gloves.csv")
df_snipers = pd.read_csv("databases\Snipers.csv")
df_pistols = pd.read_csv("databases\Pistols.csv")
df_smgs = pd.read_csv("databases\SMG.csv")
df_stgs = pd.read_csv("databases\STG.csv")
df_lmgs = pd.read_csv("databases\LMG.csv")

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
        [KeyboardButton(text='Knifes'), KeyboardButton(text='Gloves')],
        [KeyboardButton(text='Sniper Rifles'), KeyboardButton(text='Rifles')], 
        [KeyboardButton(text='Pistols'), KeyboardButton(text='SMG')],
        [KeyboardButton(text='Shotguns'), KeyboardButton(text='Machine guns')],
        [KeyboardButton(text="Contacts")],
    ],
    resize_keyboard=False,
    input_field_placeholder="Choose something in menu",
)

#lists of all weapons in cs2 ->
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
        


#----------------------------------------------------------------------------------------------------------------

async def all_gloves():             #all gloves types
    keyboard = ReplyKeyboardBuilder()

    for glove in glovesN:
        keyboard.add(KeyboardButton(text=glove))

    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup() 


async def all_gloves_skins(glove_name: str):           #all gloves skins
    keyboard = ReplyKeyboardBuilder()
    
    skins = df_gloves.loc[df_gloves.iloc[:, 0] == glove_name, df_gloves.columns[1]]
    
    for skin in skins:
        keyboard.add(KeyboardButton(text=str(skin)))
        
    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()
    


async def glove_skins_data(glove_name: str,glove_skin: str):              #glove link, pics, min and max prices
    k = InlineKeyboardBuilder()
    links = df_gloves.loc[
        (df_gloves.iloc[:, 0] == glove_name) & (df_gloves.iloc[:, 1] == glove_skin),
        df_gloves.columns[3]
    ]
    
    pics = df_gloves.loc[
        (df_gloves.iloc[:, 0] == glove_name) & (df_gloves.iloc[:, 1] == glove_skin),
        df_gloves.columns[2]
    ]
    min_prices = df_gloves.loc[
        (df_gloves.iloc[:,0] == glove_name) & (df_gloves.iloc[:, 1] == glove_skin),
        df_gloves.columns[4]
    ]
    
    max_prices = df_gloves.loc[
        (df_gloves.iloc[:,0] == glove_name) & (df_gloves.iloc[:, 1] == glove_skin),
        df_gloves.columns[5]
    ]
    
    
    pic_url = pics.iloc[0] if not pics.empty else None
    min_price = min_prices.iloc[0] if not min_prices.empty else None
    max_price = max_prices.iloc[0] if not max_prices.empty else None
    
    for link in links:
        k.button(text="All current prices", url=str(link))
    
    keyboard = k.adjust(1).as_markup()
    
    
    return keyboard, pic_url, min_price, max_price 


    
#--------------------------------------------------------------------------------------------------------------------

async def all_snipers():             #all sniper types
    keyboard = ReplyKeyboardBuilder()

    for sniper in snipersN:
        keyboard.add(KeyboardButton(text=sniper))

    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()        
    
    
async def all_sniper_skins(sniper_name: str):           #all sniper skins
    keyboard = ReplyKeyboardBuilder()
    
    skins = df_snipers.loc[df_snipers.iloc[:, 0] == sniper_name, df_snipers.columns[1]]
    
    for skin in skins:
        keyboard.add(KeyboardButton(text=str(skin)))
        
    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()

async def sniper_skins_data(sniper_name: str,sniper_skin: str):              #sniper link, pics, min and max prices
    k = InlineKeyboardBuilder()
    links = df_snipers.loc[
        (df_snipers.iloc[:, 0] == sniper_name) & (df_snipers.iloc[:, 1] == sniper_skin),
        df_snipers.columns[3]
    ]
    
    pics = df_snipers.loc[
        (df_snipers.iloc[:, 0] == sniper_name) & (df_snipers.iloc[:, 1] == sniper_skin),
        df_snipers.columns[2]
    ]
    min_prices = df_snipers.loc[
        (df_snipers.iloc[:,0] == sniper_name) & (df_snipers.iloc[:, 1] == sniper_skin),
        df_snipers.columns[4]
    ]
    
    max_prices = df_snipers.loc[
        (df_snipers.iloc[:,0] == sniper_name) & (df_snipers.iloc[:, 1] == sniper_skin),
        df_snipers.columns[5]
    ]
    
    
    pic_url = pics.iloc[0] if not pics.empty else None
    min_price = min_prices.iloc[0] if not min_prices.empty else None
    max_price = max_prices.iloc[0] if not max_prices.empty else None
    
    for link in links:
        k.button(text="All current prices", url=str(link))
    
    keyboard = k.adjust(1).as_markup()
    
    
    return keyboard, pic_url, min_price, max_price 

#-------------------------------------------------------------------------------------------------------------------------

async def all_pistols():             #all pistol types
    keyboard = ReplyKeyboardBuilder()

    for pistol in pistolsN:
        keyboard.add(KeyboardButton(text=pistol))

    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()        
    
    
async def all_pistol_skins(pistol_name: str):           #all pistol skins
    keyboard = ReplyKeyboardBuilder()
    
    skins = df_pistols.loc[df_pistols.iloc[:, 0] == pistol_name, df_pistols.columns[1]]
    
    for skin in skins:
        keyboard.add(KeyboardButton(text=str(skin)))
        
    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()

async def pistol_skins_data(pistol_name: str,pistol_skin: str):              #pistol link, pics, min and max prices
    k = InlineKeyboardBuilder()
    links = df_pistols.loc[
        (df_pistols.iloc[:, 0] == pistol_name) & (df_pistols.iloc[:, 1] == pistol_skin),
        df_pistols.columns[3]
    ]
    
    pics = df_pistols.loc[
        (df_pistols.iloc[:, 0] == pistol_name) & (df_pistols.iloc[:, 1] == pistol_skin),
        df_pistols.columns[2]
    ]
    min_prices = df_pistols.loc[
        (df_pistols.iloc[:,0] == pistol_name) & (df_pistols.iloc[:, 1] == pistol_skin),
        df_pistols.columns[4]
    ]
    
    max_prices = df_pistols.loc[
        (df_pistols.iloc[:,0] == pistol_name) & (df_pistols.iloc[:, 1] == pistol_skin),
        df_pistols.columns[5]
    ]
    
    
    pic_url = pics.iloc[0] if not pics.empty else None
    min_price = min_prices.iloc[0] if not min_prices.empty else None
    max_price = max_prices.iloc[0] if not max_prices.empty else None
    
    for link in links:
        k.button(text="All current prices", url=str(link))
    
    keyboard = k.adjust(1).as_markup()
    
    
    return keyboard, pic_url, min_price, max_price 

#-------------------------------------------------------------------------------------------------------------------------
async def all_smgs():             #all SMG types
    keyboard = ReplyKeyboardBuilder()

    for smg in smgN:
        keyboard.add(KeyboardButton(text=smg))

    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()  


async def all_smg_skins(smg_name: str):           #all smg skins
    keyboard = ReplyKeyboardBuilder()
    
    skins = df_smgs.loc[df_smgs.iloc[:, 0] == smg_name, df_smgs.columns[1]]
    
    for skin in skins:
        keyboard.add(KeyboardButton(text=str(skin)))
        
    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()  


async def smg_skins_data(smg_name: str,smg_skin: str):              #smg link, pics, min and max prices
    k = InlineKeyboardBuilder()
    links = df_smgs.loc[
        (df_smgs.iloc[:, 0] == smg_name) & (df_smgs.iloc[:, 1] == smg_skin),
        df_smgs.columns[3]
    ]
    
    pics = df_smgs.loc[
        (df_smgs.iloc[:, 0] == smg_name) & (df_smgs.iloc[:, 1] == smg_skin),
        df_smgs.columns[2]
    ]
    min_prices = df_smgs.loc[
        (df_smgs.iloc[:,0] == smg_name) & (df_smgs.iloc[:, 1] == smg_skin),
        df_smgs.columns[4]
    ]
    
    max_prices = df_smgs.loc[
        (df_smgs.iloc[:,0] == smg_name) & (df_smgs.iloc[:, 1] == smg_skin),
        df_smgs.columns[5]
    ]
    
    
    pic_url = pics.iloc[0] if not pics.empty else None
    min_price = min_prices.iloc[0] if not min_prices.empty else None
    max_price = max_prices.iloc[0] if not max_prices.empty else None
    
    for link in links:
        k.button(text="All current prices", url=str(link))
    
    keyboard = k.adjust(1).as_markup()
    
    
    return keyboard, pic_url, min_price, max_price

#------------------------------------------------------------------------------------------------------------------------


async def all_stgs():             #all stg types
    keyboard = ReplyKeyboardBuilder()

    for stg in stgN:
        keyboard.add(KeyboardButton(text=stg))

    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup() 


async def all_stg_skins(stg_name: str):           #all stg skins
    keyboard = ReplyKeyboardBuilder()
    
    skins = df_stgs.loc[df_stgs.iloc[:, 0] == stg_name, df_stgs.columns[1]]
    
    for skin in skins:
        keyboard.add(KeyboardButton(text=str(skin)))
        
    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()  

async def stg_skins_data(stg_name: str,stg_skin: str):              #stg link, pics, min and max prices
    k = InlineKeyboardBuilder()
    links = df_stgs.loc[
        (df_stgs.iloc[:, 0] == stg_name) & (df_stgs.iloc[:, 1] == stg_skin),
        df_stgs.columns[3]
    ]
    
    pics = df_stgs.loc[
        (df_stgs.iloc[:, 0] == stg_name) & (df_stgs.iloc[:, 1] == stg_skin),
        df_stgs.columns[2]
    ]
    min_prices = df_stgs.loc[
        (df_stgs.iloc[:,0] == stg_name) & (df_stgs.iloc[:, 1] == stg_skin),
        df_stgs.columns[4]
    ]
    
    max_prices = df_stgs.loc[
        (df_stgs.iloc[:,0] == stg_name) & (df_stgs.iloc[:, 1] == stg_skin),
        df_stgs.columns[5]
    ]
    
    
    pic_url = pics.iloc[0] if not pics.empty else None
    min_price = min_prices.iloc[0] if not min_prices.empty else None
    max_price = max_prices.iloc[0] if not max_prices.empty else None
    
    for link in links:
        k.button(text="All current prices", url=str(link))
    
    keyboard = k.adjust(1).as_markup()
    
    
    return keyboard, pic_url, min_price, max_price


#------------------------------------------------------------------------------------------------------------------------


async def all_lmgs():             #all lmg types
    keyboard = ReplyKeyboardBuilder()

    for lmg in lmgN:
        keyboard.add(KeyboardButton(text=lmg))

    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup() 


async def all_lmg_skins(lmg_name: str):           #all lmg skins
    keyboard = ReplyKeyboardBuilder()
    
    skins = df_lmgs.loc[df_lmgs.iloc[:, 0] == lmg_name, df_lmgs.columns[1]]
    
    for skin in skins:
        keyboard.add(KeyboardButton(text=str(skin)))
        
    keyboard.add(KeyboardButton(text="Main Menu"))
    return keyboard.adjust(2).as_markup()  

async def lmg_skins_data(lmg_name: str,lmg_skin: str):              #lmg link, pics, min and max prices
    k = InlineKeyboardBuilder()
    links = df_lmgs.loc[
        (df_lmgs.iloc[:, 0] == lmg_name) & (df_lmgs.iloc[:, 1] == lmg_skin),
        df_lmgs.columns[3]
    ]
    
    pics = df_lmgs.loc[
        (df_lmgs.iloc[:, 0] == lmg_name) & (df_lmgs.iloc[:, 1] == lmg_skin),
        df_lmgs.columns[2]
    ]
    min_prices = df_lmgs.loc[
        (df_lmgs.iloc[:,0] == lmg_name) & (df_lmgs.iloc[:, 1] == lmg_skin),
        df_lmgs.columns[4]
    ]
    
    max_prices = df_lmgs.loc[
        (df_lmgs.iloc[:,0] == lmg_name) & (df_lmgs.iloc[:, 1] == lmg_skin),
        df_lmgs.columns[5]
    ]
    
    
    pic_url = pics.iloc[0] if not pics.empty else None
    min_price = min_prices.iloc[0] if not min_prices.empty else None
    max_price = max_prices.iloc[0] if not max_prices.empty else None
    
    for link in links:
        k.button(text="All current prices", url=str(link))
    
    keyboard = k.adjust(1).as_markup()
    
    
    return keyboard, pic_url, min_price, max_price