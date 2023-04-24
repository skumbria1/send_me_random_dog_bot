from aiogram import types
from utils import FileGetter
from loader import dp


@dp.message_handler()
async def file_getter(message: types.Message):
    file = FileGetter()
    file.get_file()
    if file.extension in ('.mp4', '.MP4', '.webm', '.WEBM', '.gif', '.GIF'):
        await message.answer_video(file.content)
    else:
        await message.answer_photo(file.content)
