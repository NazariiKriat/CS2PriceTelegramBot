from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton 
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Knifes', callback_data='knifes')],
    [InlineKeyboardButton(text='Gloves', callback_data='gloves')],
    [InlineKeyboardButton(text='Rifles',callback_data='rifles'), InlineKeyboardButton(text='Pistols', callback_data='pistols')],
    [InlineKeyboardButton(text='Shotguns', callback_data= 'shotguns'), InlineKeyboardButton(text='SMG', callback_data='smg')],
    [InlineKeyboardButton(text='Contacts', callback_data= 'contacts')]
    
],              
                           resize_keyboard= False,
                           input_field_placeholder= 'Choose something in menu'
                           )

knifes = ["Bayonet", "M9 Bayonet",
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
"Classic Knife",]

async def all_knifes():
    keyboard = InlineKeyboardBuilder()
    
    for knife in knifes:
        keyboard.add(InlineKeyboardButton(text=knife, callback_data= f'knife_{knife}'))
        
    keyboard.add(InlineKeyboardButton(text="Main Menu", callback_data="to_main"))
    return keyboard.adjust(2).as_markup()
    