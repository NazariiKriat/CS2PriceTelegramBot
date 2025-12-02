from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputFile

import app.keyboards as kb
from app.keyboards import knifesN
from app.keyboards import riflesN
from app.keyboards import l1
from app.keyboards import skin_row
from app.keyboards import skin_rifles_row

router = Router()



@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Hi trader! ⚡ I am price checker bot. Write item's name to check!",
        reply_markup=kb.main,
    )





@router.message(F.text == "Knifes")     #all knife types
async def knifes(message: Message):
    await message.answer(text="Knifes: ", reply_markup=await kb.all_knifes())
    


@router.message(F.text.in_(knifesN))
async def skins_knifes(message: Message):
    text = message.text.strip()
    if text in knifesN:
        kb.l1 = text
        
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_skins(text)
        )

@router.message(F.text.in_(skin_row))
async def data_skins(message: Message):
    text = message.text.strip()
    if text in skin_row:
       
        keyboard, image_url, min_p, max_p = await kb.skins_data(text)
        if image_url:
            await message.answer_photo(
                photo= image_url,
                caption=f"🎯 {kb.l1} | {text}\n💰 Current prices for this item: {min_p} -- {max_p}.\n" 
                    
            
        )
        await message.answer(
            text= f"More info for {kb.l1} - {text}", reply_markup= keyboard
        )

#------------------------------------------------------------------------------------------------------------



@router.message(F.text == "Rifles")         #all rifles types
async def rifles(message: Message):
    await message.answer(text="Rifles: ", reply_markup=await kb.all_rifles())


@router.message(F.text.in_(riflesN))            #all rifles skins
async def skins_rifles(message: Message):
    text = message.text.strip()
    if text in riflesN:
        kb.l1 = text
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_rifle_skins(text)
        )

@router.message(F.text.in_(skin_rifles_row))                #skins rifles data
async def rifle_data_skins(message: Message):
    text = message.text.strip()
    
    if text in skin_rifles_row:
        keyboard, image_url, min_p, max_p = await kb.rifle_skins_data(text)
        if image_url:
            await message.answer_photo(
                photo= image_url,
                caption=f"🎯 {kb.l1} | {text}\n💰 Current prices for this item: {min_p} -- {max_p}.\n" 
                    
            
        )
        await message.answer(
            text= f"More info for {kb.l1} - {text}", reply_markup= keyboard
        )
        
        
        
        

@router.message(F.text == "Main Menu")
async def return_menu(message: Message):
    kb.l1 = "Nothing"
    await message.answer(text="Main", reply_markup=kb.main)
