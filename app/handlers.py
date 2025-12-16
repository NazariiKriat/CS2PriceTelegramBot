from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import app.keyboards as kb
from app.keyboards import knifesN
from app.keyboards import riflesN
from app.keyboards import glovesN
from app.keyboards import snipersN
from app.keyboards import pistolsN
from app.keyboards import smgN
from app.keyboards import stgN
from app.keyboards import lmgN

from app.keyboards import skin_row
from app.keyboards import skin_rifles_row
from app.keyboards import skin_gloves_row
from app.keyboards import skin_snipers_row
from app.keyboards import skin_pistols_row
from app.keyboards import skin_smgs_row
from app.keyboards import skin_stgs_row
from app.keyboards import skin_lmgs_row

router = Router()


class Skins_Reg(StatesGroup):
    unitName = State()
    unitSkin = State()


@router.message(CommandStart())
async def start_command(
    message: Message,
):
    await message.answer(
        "Hi trader! ⚡ I am price checker bot. Write item's name to check!",
        reply_markup=kb.main,
    )


@router.message(F.text == "Knifes")  # all knife types
async def knifes(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitName)
    await message.answer(text="Knifes: ", reply_markup=await kb.all_knifes())


@router.message(F.text.in_(knifesN), Skins_Reg.unitName)
async def skins_knifes(message: Message, state: FSMContext):
    await state.update_data(unitName=message.text)
    await state.set_state(Skins_Reg.unitSkin)
    text = message.text.strip()  # all skins for the knifes
    if text in knifesN:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_skins(text)
        )


@router.message(F.text.in_(skin_row), Skins_Reg.unitSkin)
async def data_skins(
    message: Message, state: FSMContext
):  # all prices pictures and urls
    await state.update_data(unitSkin=message.text)
    data = await state.get_data()
    text = message.text.strip()
    knife_name = data.get("unitName")
    knife_skin = data.get("unitSkin")
    if text in skin_row:

        keyboard, image_url, min_p, max_p = await kb.skins_data(knife_name, knife_skin)
        if image_url:
            await message.answer_photo(
                photo=image_url,
                caption=f"🎯 {knife_name} | {knife_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n",
            )
        await message.answer(
            text=f"More info for {knife_name} - {knife_skin}", reply_markup=keyboard
        )
        await state.update_data(unitSkin=None)


# ------------------------------------------------------------------------------------------------------------


@router.message(F.text == "Rifles")  # all rifles types
async def rifles(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitName)
    await message.answer(text="Rifles: ", reply_markup=await kb.all_rifles())


@router.message(F.text.in_(riflesN), Skins_Reg.unitName)  # all rifles skins
async def skins_rifles(message: Message, state: FSMContext):
    await state.update_data(unitName=message.text)
    await state.set_state(Skins_Reg.unitSkin)
    text = message.text.strip()
    if text in riflesN:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_rifle_skins(text)
        )


@router.message(F.text.in_(skin_rifles_row), Skins_Reg.unitSkin)  # skins rifles data
async def rifle_data_skins(message: Message, state: FSMContext):
    await state.update_data(unitSkin=message.text)
    data = await state.get_data()
    text = message.text.strip()
    rifle_name = data.get("unitName")
    rifle_skin = data.get("unitSkin")

    if text in skin_rifles_row:
        keyboard, image_url, min_p, max_p = await kb.rifle_skins_data(
            rifle_name, rifle_skin
        )
        if image_url:
            await message.answer_photo(
                photo=image_url,
                caption=f"🎯 {rifle_name} | {rifle_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n",
            )

        await message.answer(
            text=f"More info for {rifle_name} - {rifle_skin}", reply_markup=keyboard
        )
        await state.update_data(unitSkin=None)


@router.message(F.text == "Main Menu")
async def return_menu(message: Message, state: FSMContext):
    await message.answer(text="Main", reply_markup=kb.main)
    await state.clear()


# ----------------------------------------------------------------------------------------------------------------------


@router.message(F.text == "Gloves")  # all gloves types
async def rifles(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitName)
    await message.answer(text="Gloves: ", reply_markup=await kb.all_gloves())


@router.message(F.text.in_(glovesN), Skins_Reg.unitName)  # all gloves skins
async def skins_gloves(message: Message, state: FSMContext):
    await state.update_data(unitName=message.text)
    await state.set_state(Skins_Reg.unitSkin)
    text = message.text.strip()
    if text in glovesN:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_gloves_skins(text)
        )


@router.message(F.text.in_(skin_gloves_row), Skins_Reg.unitSkin)  # skins gloves data
async def glove_data_skins(message: Message, state: FSMContext):
    await state.update_data(unitSkin=message.text)
    data = await state.get_data()
    text = message.text.strip()
    glove_name = data.get("unitName")
    glove_skin = data.get("unitSkin")

    if text in skin_gloves_row:
        keyboard, image_url, min_p, max_p = await kb.glove_skins_data(
            glove_name, glove_skin
        )
        if image_url:
            await message.answer_photo(
                photo=image_url,
                caption=f"🎯 {glove_name} | {glove_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n",
            )

        await message.answer(
            text=f"More info for {glove_name} - {glove_skin}", reply_markup=keyboard
        )
        await state.update_data(unitSkin=None)


#--------------------------------------------------------------------------------------------------------------------

@router.message(F.text == "Sniper Rifles")  # all sniper rifle types
async def snipers(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitName)
    await message.answer(text="Sniper Rifles: ", reply_markup=await kb.all_snipers())

@router.message(F.text.in_(snipersN), Skins_Reg.unitName)  # all sniper rifle skins
async def skins_snipers(message: Message, state: FSMContext):
    await state.update_data(unitName=message.text)
    await state.set_state(Skins_Reg.unitSkin)
    text = message.text.strip()
    if text in snipersN:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_sniper_skins(text)
            )
        
@router.message(F.text.in_(skin_snipers_row), Skins_Reg.unitSkin)  # skins rifle data
async def sniper_data_skins(message: Message, state: FSMContext):
    await state.update_data(unitSkin=message.text)
    data = await state.get_data()
    text = message.text.strip()
    sniper_name = data.get("unitName")
    sniper_skin = data.get("unitSkin")

    if text in skin_snipers_row:
        keyboard, image_url, min_p, max_p = await kb.sniper_skins_data(
           sniper_name, sniper_skin
        )
        if image_url:
            await message.answer_photo(
                photo=image_url,
                caption=f"🎯 {sniper_name} | {sniper_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n",
            )

        await message.answer(
            text=f"More info for {sniper_name} - {sniper_skin}", reply_markup=keyboard
        )
        await state.update_data(unitSkin=None)


#---------------------------------------------------------------------------------------------------------------------------


@router.message(F.text == "Pistols")  # all pistol types
async def pistols(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitName)
    await message.answer(text="Pistols: ", reply_markup=await kb.all_pistols())

@router.message(F.text.in_(pistolsN), Skins_Reg.unitName)  # all pistol skins
async def skins_pistols(message: Message, state: FSMContext):
    await state.update_data(unitName=message.text)
    await state.set_state(Skins_Reg.unitSkin)
    text = message.text.strip()
    if text in pistolsN:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_pistol_skins(text)
            )
        
@router.message(F.text.in_(skin_pistols_row), Skins_Reg.unitSkin)  # skins pistol data
async def pistol_data_skins(message: Message, state: FSMContext):
    await state.update_data(unitSkin=message.text)
    data = await state.get_data()
    text = message.text.strip()
    pistol_name = data.get("unitName")
    pistol_skin = data.get("unitSkin")

    if text in skin_pistols_row:
        keyboard, image_url, min_p, max_p = await kb.pistol_skins_data(
           pistol_name, pistol_skin
        )
        if image_url:
            await message.answer_photo(
                photo=image_url,
                caption=f"🎯 {pistol_name} | {pistol_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n",
            )

        await message.answer(
            text=f"More info for {pistol_name} - {pistol_skin}", reply_markup=keyboard
        )
        await state.update_data(unitSkin=None)
        
        
@router.message(F.text == "Main Menu")
async def return_menu(message: Message, state: FSMContext):
    await message.answer(text="Main", reply_markup=kb.main)
    await state.clear()


#-------------------------------------------------------------------------------------------------------------------------


@router.message(F.text == "SMG")  # all smg types
async def smgs(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitName)
    await message.answer(text="SMGs: ", reply_markup=await kb.all_smgs())

@router.message(F.text.in_(smgN), Skins_Reg.unitName)  # all pistol skins
async def skins_smgs(message: Message, state: FSMContext):
    await state.update_data(unitName=message.text)
    await state.set_state(Skins_Reg.unitSkin)
    text = message.text.strip()
    if text in smgN:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_smg_skins(text)
            )
        
@router.message(F.text.in_(skin_smgs_row), Skins_Reg.unitSkin)  # skins pistol data
async def smg_data_skins(message: Message, state: FSMContext):
    await state.update_data(unitSkin=message.text)
    data = await state.get_data()
    text = message.text.strip()
    smg_name = data.get("unitName")
    smg_skin = data.get("unitSkin")

    if text in skin_smgs_row:
        keyboard, image_url, min_p, max_p = await kb.smg_skins_data(
           smg_name, smg_skin
        )
        if image_url:
            await message.answer_photo(
                photo=image_url,
                caption=f"🎯 {smg_name} | {smg_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n",
            )

        await message.answer(
            text=f"More info for {smg_name} - {smg_skin}", reply_markup=keyboard
        )
        await state.update_data(unitSkin=None)
        
        

    
#----------------------------------------------------------------------------------------------------------------

@router.message(F.text == "Shotguns")  # all shotguns types
async def stgs(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitName)
    await message.answer(text="Shotguns: ", reply_markup=await kb.all_stgs())
    
@router.message(F.text.in_(stgN), Skins_Reg.unitName)  # all pistol skins
async def skins_stgs(message: Message, state: FSMContext):
    await state.update_data(unitName=message.text)
    await state.set_state(Skins_Reg.unitSkin)
    text = message.text.strip()
    if text in stgN:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_stg_skins(text)
            )

@router.message(F.text.in_(skin_stgs_row), Skins_Reg.unitSkin)  # skins pistol data
async def stg_data_skins(message: Message, state: FSMContext):
    await state.update_data(unitSkin=message.text)
    data = await state.get_data()
    text = message.text.strip()
    stg_name = data.get("unitName")
    stg_skin = data.get("unitSkin")

    if text in skin_stgs_row:
        keyboard, image_url, min_p, max_p = await kb.stg_skins_data(
           stg_name, stg_skin
        )
        if image_url:
            await message.answer_photo(
                photo=image_url,
                caption=f"🎯 {stg_name} | {stg_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n",
            )

        await message.answer(
            text=f"More info for {stg_name} - {stg_skin}", reply_markup=keyboard
        )
        await state.update_data(unitSkin=None)

#--------------------------------------------------------------------------------------------------------------------------
#lmgs
@router.message(F.text == "Machine guns")  # all shotguns types
async def lmgs(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Skins_Reg.unitName)
    await message.answer(text="Machine guns: ", reply_markup=await kb.all_lmgs())
    
@router.message(F.text.in_(lmgN), Skins_Reg.unitName)  # all pistol skins
async def skins_lmgs(message: Message, state: FSMContext):
    await state.update_data(unitName=message.text)
    await state.set_state(Skins_Reg.unitSkin)
    text = message.text.strip()
    if text in lmgN:
        await message.answer(
            text=f"Skins for the: {text}", reply_markup=await kb.all_lmg_skins(text)
            )

@router.message(F.text.in_(skin_lmgs_row), Skins_Reg.unitSkin)  # skins pistol data
async def lmg_data_skins(message: Message, state: FSMContext):
    await state.update_data(unitSkin=message.text)
    data = await state.get_data()
    text = message.text.strip()
    lmg_name = data.get("unitName")
    lmg_skin = data.get("unitSkin")

    if text in skin_lmgs_row:
        keyboard, image_url, min_p, max_p = await kb.lmg_skins_data(
           lmg_name, lmg_skin
        )
        if image_url:
            await message.answer_photo(
                photo=image_url,
                caption=f"🎯 {lmg_name} | {lmg_skin}\n💰 Current prices for this item: {min_p} -- {max_p}.\n",
            )

        await message.answer(
            text=f"More info for {lmg_name} - {lmg_skin}", reply_markup=keyboard
        )
        await state.update_data(unitSkin=None)

@router.message(F.text == "Main Menu")
async def return_menu(message: Message, state: FSMContext):
    await message.answer(text="Main", reply_markup=kb.main)
    await state.clear()