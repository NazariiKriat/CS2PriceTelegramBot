from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Hi trader! ⚡ I am price checker bot. Write item's name to check!", reply_markup= kb.main)

@router.message(Command("category"))
async def category_command(message: Message):
    await message.answer("It's category command")
    
@router.message(F.text == "How are you?")
async def how_are_you(message:Message):
    await message.answer('OK!')
    
@router.callback_query(F.data == "knifes")
async def knifes(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text("All knifes: ", reply_markup= await kb.all_knifes())
    
@router.callback_query(F.data == "to_main" )
async def return_menu(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text("Main", reply_markup= kb.main)

    