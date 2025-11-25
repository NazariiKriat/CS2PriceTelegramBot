from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputFile

import app.keyboards as kb
from app.keyboards import knifesN
from app.keyboards import l1
from app.keyboards import skin_row

router = Router()



@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "Hi trader! ⚡ I am price checker bot. Write item's name to check!",
        reply_markup=kb.main,
    )


@router.message(Command("category"))
async def category_command(message: Message):
    await message.answer("It's category command")


@router.message(F.text == "How are you?")
async def how_are_you(message: Message):
    await message.answer("OK!")


@router.message(F.text == "Knifes")
async def knifes(message: Message):
    await message.answer(text="Knifes: ", reply_markup=await kb.all_knifes())


@router.message(F.text.in_(knifesN))
async def skins_knifes(message: Message):
    text = message.text.strip()
    if text in knifesN:
        kb.l1 = text
        print(kb.l1)
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_skins(text)
        )

@router.message(F.text.in_(skin_row))
async def data_skins(message: Message):
    text = message.text.strip()
    
    if text in skin_row:
        keyboard, image_url = await kb.skins_data(text)
        if image_url:
            await message.answer_photo(
                photo= image_url,
                caption=f"🎯 {kb.l1} | {text}\n💰 Check prices below:"
            
        )
        await message.answer(
            text= f"Prices for {kb.l1} $ {text}", reply_markup= keyboard
        )

        
        
        
        

@router.message(F.text == "Main Menu")
async def return_menu(message: Message):
    kb.l1 = "Nothing"
    print(kb.l1)
    await message.answer(text="Main", reply_markup=kb.main)
