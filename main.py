import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from PIL import Image, ImageDraw

BOT_TOKEN = os.getenv("BOT_TOKEN")
# Укажите username вашего канала (с @) или его ID
CHANNEL_ID = "@ваш_канал"

# Словарь: ключевое слово -> (координата X, координата Y на картинке static_map.png)
KEYWORD_MAP = {
    "симферополь": (400, 500),
    "севастополь": (200, 600),
    "евпатория": (150, 350),
    "джанкой": (500, 200),
}

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def draw_points_on_map(points):
    image = Image.open("static_map.png").convert("RGBA")
    draw = ImageDraw.Draw(image)

    for x, y in points:
        # Красный маркер
        draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill="red", outline="white", width=2)
        # Вектор / знак направления
        draw.line((x, y, x + 35, y - 35), fill="red", width=5)

    image.convert("RGB").save("result_map.png")


async def check_channel_and_draw():
    found_points = []
    async for message in bot.get_chat_history(CHANNEL_ID, limit=10):
        if not message.text:
            continue
        text_lower = message.text.lower()
        for kw, coords in KEYWORD_MAP.items():
            if kw in text_lower:
                found_points.append(coords)

    if found_points:
        draw_points_on_map(found_points)
        return True
    return False


@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer("Бот готов к работе. Напишите /map для получения карты.")


@dp.message(F.text == "/map")
async def send_map(message: Message):
    if await check_channel_and_draw():
        photo = FSInputFile("result_map.png")
        await message.answer_photo(photo, caption="📍 Карта направлений по сообщениям из канала")
    else:
        await message.answer("Ключевые слова в последних сообщениях не найдены.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

