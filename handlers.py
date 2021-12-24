from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from main import dp, bot
from config import users, admin_id

@dp.message_handler(Command('sendall'))
async def send_all(message: Message):
    if message.chat.id == admin_id:
        await message.answer('Start')
        for i in users:
            await bot.send_message(i, message.text[message.text.find(' '):])

        await message.answer('Done')

    else:
        await message.answer('Error')

@dp.message_handler(Command('sendallwp'))
async def send_all(message: Message):
    if message.chat.id == admin_id:
        await message.answer('Start')
        for i in users:
            await bot.send_photo(i, open('laptop.jpg', 'rb'), message.text[message.text.find(' '):])

        await message.answer('Done')

    else:
        await message.answer('Error')
