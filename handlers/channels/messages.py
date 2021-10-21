from config import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ContentType


@dp.message_handler()
async def echo(message: Message):
    await message.answer(f'ответ: {message.text} в чате {message.chat.id}')
