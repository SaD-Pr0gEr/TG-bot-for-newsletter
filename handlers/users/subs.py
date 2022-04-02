from aiogram import types
from aiogram.dispatcher.filters import Command

from filters.private_chat import IsPrivate
from filters.subs import IsSubscribed, IsNotSubscribed
from loader import dp, DB


@dp.message_handler(Command("subscribe", prefixes="!/"), IsPrivate(), IsNotSubscribed())
async def subscribe(message: types.Message):
    check_user = DB.retrieve_user(message.from_user.id)
    if check_user:
        DB.set_status(user_id=message.from_user.id, status=True)
        await message.answer("Вы успешно подписались на рассылку! Ждите от нас много спама))")
        return
    await message.answer(f"Поздравляем! Вы успешно подписались {message.from_user.first_name}!")


@dp.message_handler(Command("unsubscribe", prefixes="!/"), IsPrivate(), IsSubscribed())
async def unsubscribe(message: types.Message):
    DB.set_status(message.from_user.id, False)
    await message.answer(f"Вы успешно отписались {message.from_user.first_name})")
