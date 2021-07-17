import asyncio
import random
from notifications import news_notify
from parsers import parse_news
from aiogram.utils import executor
from config import BOT_TOKEN, ADMIN
import logging
from aiogram import Bot, Dispatcher, types
from db_monipulate.work_with_db import DbManager

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

DB = DbManager()


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}, '
                         f'ты успешно запустил новостной бот команды Boston Celtics!')


@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    user_id = message.from_user.id
    get_user = DB.get_user_from_subs(user_id)
    if not get_user:
        DB.add_user(user_id, True)
        await message.answer(f"Поздравляем! Вы успешно подписались {message.from_user.first_name}!")
    elif not get_user.is_subscribed:
        DB.set_status(user_id, True)
        await message.answer(f"Поздравляем! Вы успешно подписались {message.from_user.first_name}!")
    else:
        DB.set_status(user_id, True)
        await message.answer(f"Вы и так подписаны {message.from_user.first_name})")


@dp.message_handler(commands=["unsubscribe"])
async def unsubscribe(message: types.Message):
    user_id = message.from_user.id
    get_user = DB.get_user_from_subs(user_id)
    if get_user.is_subscribed:
        DB.set_status(user_id, False)
        await message.answer(f"Вы успешно отписались {message.from_user.first_name})")
    else:
        DB.set_status(user_id, False)
        await message.answer(f"Вы и так не подписаны {message.from_user.first_name}!")


@dp.message_handler(commands=['news'])
async def news(message: types.Message):
    parse = parse_news.parse_news_bleacher_report()
    for i in parse:
        await message.answer(f"{i['post_title']}: {i['link']} \n\nИсточник: {i['proof']}")


@dp.message_handler(commands=['allusers'])
async def all_users(message: types.Message):
    user = message.from_user
    if int(user.id) != int(ADMIN):
        random_message_text = [f"Вы не являетесь админом {user.first_name}!",
                               f"Ой-ой-ой придержите коней {user.first_name}! Вы не являетесь админом!"]
        random_message = random.choice(random_message_text)
        await message.answer(random_message)
    else:
        get = DB.get_all_subscribers()
        for user in get:
            get_user = await bot.get_chat_member(user.user_id, message.from_user.id)
            await message.answer(f"@{get_user['user']['username']}")


async def send_news(sleep_time):
    while True:
        await asyncio.sleep(sleep_time)
        await news_notify.notification()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(send_news(3000))
    executor.start_polling(dp)
