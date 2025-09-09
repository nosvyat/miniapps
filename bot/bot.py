from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging

# Логирование
logging.basicConfig(level=logging.INFO)

# Токен бота
TOKEN = "8466438446:AAFaLBkLFGhFCtzJYCUDw-TnKEOrSeylZco"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# URL вашего WebApp
WEBAPP_URL = "https://ваш-домен.com"  # <-- сюда вставь ссылку на твой WebApp

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    """
    Команда /start
    Отправляет кнопку для открытия WebApp
    """
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="Открыть приложение", web_app=WebAppInfo(url=WEBAPP_URL))
    kb.add(button)
    await message.answer("Добро пожаловать в Trading Mini App! 🚀", reply_markup=kb)

@dp.message_handler(commands=["help"])
async def help_cmd(message: types.Message):
    """
    Команда /help
    """
    await message.answer(
        "Список команд:\n"
        "/start - открыть WebApp\n"
        "/help - помощь"
    )

if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)
