from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import Config
from weather import get_weather
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


CONFIG: Config = Config()
CONFIG.load()

bot = Bot(token=CONFIG.telegram.api_token)
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


class WeatherFlow(StatesGroup):
    getting_location = State()
    gpc_location = State()


@dp.message_handler(commands="set_location", state="*")
async def gps_detection_step_1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton(text="Share location", request_location=True)
    keyboard.add(button)
    await message.answer("Please, share your location", reply_markup=keyboard)
    await WeatherFlow.getting_location.set()


@dp.message_handler(state=WeatherFlow.getting_location, content_types=types.ContentTypes.LOCATION)
async def gps_detection_step_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gpc_location'] = {'lat': message.location.latitude,
                                'lon': message.location.longitude}
    await message.answer("Your location detected! Now you can check your weather forecast with command /cur_weather")
    await WeatherFlow.gpc_location.set()


@dp.message_handler(commands='cur_weather', state=WeatherFlow.gpc_location)
async def weather_forecast(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(await get_weather(data['gpc_location']['lat'], data['gpc_location']['lon'], CONFIG))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
