import aiohttp
import ujson
from config import Config

BASE_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"


async def get_weather(lat: float, lon: float, config: Config) -> str:
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.get(BASE_WEATHER_URL.format(lat=lat,
                                                       lon=lon,
                                                       api_key=config.weather.api_token), ssl=False) as response:
            weather_obj = await response.json()
            return weather_obj['main']['temp']


if __name__ == '__main__':
    import asyncio
    cfg = Config()
    cfg.load()
    asyncio.run(get_weather(55.751244, 37.618423, cfg))
