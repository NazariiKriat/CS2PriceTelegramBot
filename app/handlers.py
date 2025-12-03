from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import app.keyboards as kb
from app.keyboards import knifesN
from app.keyboards import riflesN

from app.keyboards import skin_row
from app.keyboards import skin_rifles_row

router = Router()


class Skins_Reg(StatesGroup):
    unitName = State()
    unitSkin = State()
    
    
    


@router.message(CommandStart())
async def start_command(message: Message,):
    await message.answer(
        "Hi trader! ⚡ I am price checker bot. Write item's name to check!",
        reply_markup=kb.main,
        
    )
    

@router.message(F.text == "Knifes")     #all knife types
async def knifes(message: Message,state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitName)
    await message.answer(text="Knifes: ", reply_markup=await kb.all_knifes())
    


@router.message(F.text.in_(knifesN), Skins_Reg.unitName)
async def skins_knifes(message: Message, state:FSMContext):
    await state.update_data(unitName= message.text)
    await state.set_state(Skins_Reg.unitSkin)
    text = message.text.strip()                 #all skins for the knifes
    if text in knifesN:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_skins(text)
        )


@router.message(F.text.in_(skin_row), Skins_Reg.unitSkin)
async def data_skins(message: Message, state: FSMContext):                             # all prices pictures and urls
    await state.update_data(unitSkin= message.text)
    data = await state.get_data()
    text = message.text.strip()
    knife_name = data.get("unitName")
    knife_skin = data.get("unitSkin")
    if text in skin_row:
       
        keyboard, image_url, min_p, max_p = await kb.skins_data(knife_name, knife_skin)
        if image_url:
            await message.answer_photo(
                photo= image_url,
                caption=f"🎯 {knife_name} | {knife_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n" 
            
        )
        await message.answer(
            text= f"More info for {knife_name} - {knife_skin}", reply_markup= keyboard
        )
        await state.update_data(unitSkin= None)
        
        
#------------------------------------------------------------------------------------------------------------



@router.message(F.text == "Rifles")         #all rifles types
async def rifles(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitName)
    await message.answer(text="Rifles: ", reply_markup=await kb.all_rifles())


@router.message(F.text.in_(riflesN),  Skins_Reg.unitName)            #all rifles skins
async def skins_rifles(message: Message, state: FSMContext):
    await state.update_data(unitName=message.text)
    await state.set_state(Skins_Reg.unitSkin)
    text = message.text.strip()
    if text in riflesN:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_rifle_skins(text)
        )

@router.message(F.text.in_(skin_rifles_row), Skins_Reg.unitSkin)                #skins rifles data
async def rifle_data_skins(message: Message, state: FSMContext):
    await state.update_data(unitSkin=message.text)
    data = await state.get_data()
    text = message.text.strip()
    rifle_name = data.get("unitName")
    rifle_skin = data.get("unitSkin")
    
    if text in skin_rifles_row:
        keyboard, image_url, min_p, max_p = await kb.rifle_skins_data(rifle_name, rifle_skin)
        if image_url:
            await message.answer_photo(
                photo= image_url,
                caption=f"🎯 {rifle_name} | {rifle_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n"   
        )
            
        await message.answer(
            text= f"More info for {rifle_name} - {rifle_skin}", reply_markup= keyboard
        )
        await state.update_data(unitSkin= None)
        
        
        

@router.message(F.text == "Main Menu")
async def return_menu(message: Message, state: FSMContext):
    await message.answer(text="Main", reply_markup=kb.main)
    await state.clear()
