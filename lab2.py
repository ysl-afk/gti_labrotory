import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

API_TOKEN = "8634629201:AAFtNSJjTIln-T2tVQRAt4nS3kYL0W3T95w"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def get_medicine_data(medicine_name):
    try:
        with open("farmacy.html", "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        products = soup.find_all("div", class_="product")
        query = medicine_name.lower().strip()
        found_item = []

        for item in products:
            title_el = item.find("h2", class_="title")
            price_el = item.find("span", class_="price")

            if title_el and price_el:
                name = title_el.get_text(strip=True)

                if query in name.lower():
                    price = price_el.get_text(strip=True)
                    found_item.append(f"{name} — {price} руб.")
                    break

        if found_item:
            result_text = "Результаты поиска:\n" + "\n".join(found_item)
            return result_text
        return "Ничего не найдено"
    except Exception as e:
        return f"Произошла непредвиденная ошибка: {e}"

@dp.message(Command("start"))
async def cmd_start(message):
    await message.answer("Привет! Я бот для поиска лекарств.\nВведите название препарата.")

@dp.message(F.text)
async def handle_search(message):
    result = get_medicine_data(message.text)
    await message.answer(result)

async def main():
    print("Ожидание сообщений в Telegram")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())