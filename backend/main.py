import logging
import httpx
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import asyncio

API_TOKEN = '8920670872:AAHPfC3yLR8fwyeeb88dY-KVlWvcTbxemmQ'
# Убедись, что адрес именно такой, без слеша в конце
API_URL = 'https://qr-menu-project-1fv4.onrender.com'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

class ChangePriceStates(StatesGroup):
    waiting_for_dish_id = State()
    waiting_for_new_price = State()

@dp.callback_query(F.data == "change_price")
async def start_change_price(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите ID блюда (цифру):")
    await state.set_state(ChangePriceStates.waiting_for_dish_id)

@dp.message(ChangePriceStates.waiting_for_new_price)
async def process_new_price(message: Message, state: FSMContext):
    new_price = message.text.strip()
    user_data = await state.get_data()
    dish_id = int(user_data['dish_id'])

    # ФОРМИРУЕМ ПУТЬ В ТОЧНОСТИ КАК В MAIN.PY
    url = f"{API_URL}/api/menu/shashlychnaya_one/item/{dish_id}"
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(url, json={"price": int(new_price)})
        
        if response.status_code == 200:
            await message.answer("✅ Успех!")
        else:
            # Если 404, бот напишет нам адрес, чтобы мы увидели, в чем дело
            await message.answer(f"Ошибка {response.status_code}. Адрес запроса: {url}")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
    await state.clear()

# ... (остальной код твоего бота)
