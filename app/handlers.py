from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import app.keyboards as kb
from app.keyboards import DB
from app.keyboards import catN


router = Router()

ALL_WEAPONS = []
ALL_SKINS = []

for category in DB.values():
    ALL_WEAPONS.extend(category["weapons"])
    
for category in DB.values():
    ALL_SKINS.extend(category["skins"])

class Skins_Reg(StatesGroup):
    unitItem = State()
    unitName = State()
    unitSkin = State()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitItem)
    await message.answer(
        "Hi trader! ⚡ I am price checker bot. Write item's name to check!",
        reply_markup=kb.main,
    )


@router.message(F.text.in_(catN), Skins_Reg.unitItem)  # all knife types
async def knifes(message: Message, state: FSMContext):
    await state.update_data(unitItem=message.text)
    await state.set_state(Skins_Reg.unitName)
    text = message.text.strip()
    await message.answer(text="Item: ", reply_markup=await kb.all_weapons(text))


@router.message(F.text.in_(ALL_WEAPONS), Skins_Reg.unitName)
async def skins_items(message: Message, state: FSMContext):
    await state.update_data(unitName=message.text)
    await state.set_state(Skins_Reg.unitSkin)
    data = await state.get_data()
    unit_item = data.get("unitItem")
    text = message.text.strip()  # all skins for the knifes
    if text in ALL_WEAPONS:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_skins(unit_item,text)
        )


@router.message(F.text.in_(ALL_SKINS), Skins_Reg.unitSkin)
async def data_skins(
    message: Message, state: FSMContext
):  # all prices pictures and urls
    await state.update_data(unitSkin=message.text)
    data = await state.get_data()
    text = message.text.strip()
    item_type = data.get("unitItem")
    item_name = data.get("unitName")
    item_skin = data.get("unitSkin")
    if text in ALL_SKINS:

        keyboard, image_url, min_p, max_p = await kb.skins_data(item_type, item_name, item_skin)
        if image_url:
            await message.answer_photo(
                photo=image_url,
                caption=f"🎯 {item_name} | {item_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n",
            )
        await message.answer(
            text=f"More info for {item_name} - {item_skin}", reply_markup=keyboard
        )
        await state.update_data(unitSkin=None)


# ------------------------------------------------------------------------------------------------------------
@router.message(F.text == "Contacts")
async def contacts_button(message: Message, state: FSMContext):
    await message.answer(
        "Hi trader! ⚡ Bot was made by @godofwar888",
        reply_markup=kb.main,
    )
    await state.clear()
    await state.set_state(Skins_Reg.unitItem)

@router.message(F.text == "Main Menu")
async def return_menu(message: Message, state: FSMContext):
    await message.answer(text="Main Menu", reply_markup=kb.main)
    await state.clear()
    await state.set_state(Skins_Reg.unitItem)
   
