from typing import ClassVar, Final

from pydantic_settings import BaseSettings, SettingsConfigDict


class ShopSettings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env',
        env_prefix='SHOP_',
    )
    # Доставка бесплатная, если заказ (после скидки) стоит не меньше этой суммы
    FREE_DELIVERY_FROM: int = 100
    DELIVERY_PRICE: int = 15


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env'
    )
    PROJECT_NAME: str = 'Лавка героя'
    ENVIRONMENT: str = 'PRODUCTION'
    BASE_ROUTE_PATH: str = '/api/v1'
    SHOP: ClassVar[ShopSettings] = ShopSettings()


settings = Settings()

APP_VERSION: Final = '0.17.0'
