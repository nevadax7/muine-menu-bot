import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Главное меню
@dp.message_handler(commands=['start', 'menu'])
async def send_main_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "🧍 Обо мне", "🛵 Аренда скутера",
        "🏠 Аренда жилья", "🍜 Кафе / Рестораны",
        "📍 Что посмотреть", "☀️ Погода в Муйне",
        "🛍 Что купить", "📞 Связаться со мной"
    ]
    keyboard.add(*[types.KeyboardButton(text=b) for b in buttons])
    await message.answer("Выберите интересующий раздел 👇", reply_markup=keyboard)

# Заглушка
@dp.message_handler(lambda message: message.text)
async def handle_buttons(message: types.Message):
    await message.answer(f"🔧 Раздел '{message.text}' пока в разработке.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
