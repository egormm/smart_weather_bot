from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin
from yamldataclassconfig.config import YamlDataClassConfig


@dataclass
class TelegramConfig(DataClassJsonMixin):
    api_token: str = None


@dataclass
class WeatherConfig(DataClassJsonMixin):
    api_token: str = None


@dataclass
class Config(YamlDataClassConfig):
    telegram: TelegramConfig = field(
        default=None,
        metadata={"dataclasses_json": {'mm_field': TelegramConfig}})
    weather: WeatherConfig = field(
        default=None,
        metadata={"dataclasses_json": {'mm_field': WeatherConfig}})
