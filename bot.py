from config import Config
from weather import get_weather
from aiogram import Bot, Dispatcher, executor, types

CONFIG: Config = Config()
CONFIG.load()

bot = Bot(token=CONFIG.telegram.api_token)
dp = Dispatcher(bot)


@dp.message_handler(commands='weather')
async def weather_forecast(message: types.Message):
    await message.answer(await get_weather(55.751244, 37.618423, CONFIG))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
