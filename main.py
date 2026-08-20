
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = "ТВОЙ_ТОКЕН_БОТА"
WEBAPP_URL = "ССЫЛКА_НА_ТВОЙ_ХОСТИНГ_С_INDEX_HTML"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🗺 Открыть карту Крыма", 
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    await message.answer(
        "Нажми на кнопку ниже, чтобы открыть интерактивную карту:", 
        reply_markup=builder.as_markup()
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
