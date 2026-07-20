import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from PIL import Image, ImageDraw

BOT_TOKEN = os.getenv("BOT_TOKEN")
# Укажи тут свой канал!
CHANNEL_ID = "@bad_news_crimea"

KEYWORD_MAP = {
    "симферополь": (400, 500),
    "севастополь": (200, 600),
    "евпатория": (150, 350),
    "джанкой": (500, 200),
}

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
found_points = set()

def draw_points_on_map(points):
    image = Image.open("static_map.png").convert("RGBA")
    draw = ImageDraw.Draw(image)
    for x, y in points:
        draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill="red", outline="white", width=2)
        draw.line((x, y, x + 35, y - 35), fill="red", width=5)
    image.convert("RGB").save("result_map.png")

@dp.channel_post()
async def listen_channel(message: Message):
    if not message.text:
        return
    text = message.text.lower()
    for kw, coords in KEYWORD_MAP.items():
        if kw in text:
            found_points.add(coords)

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer("Бот работает. Жду новые сообщения в канале...")

@dp.message(F.text == "/map")
async def send_map(message: Message):
    if not os.path.exists("static_map.png"):
        await message.answer("Ошибка: в репозитории нет файла static_map.png")
        return

    if found_points:
        draw_points_on_map(found_points)
        photo = FSInputFile("result_map.png")
        await message.answer_photo(photo, caption="📍 Карта направлений")
    else:
        await message.answer("Пока нет новых совпадений по городам.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
