from pydantic import BaseModel, ConfigDict, Field


class AppInfoOutput(BaseModel):
    model_config = ConfigDict(title="app_info.AppInfoOutput")

    back_version: str = Field(description="Backend version")


class CartOutput(BaseModel):
    model_config = ConfigDict(title="shop.CartOutput")

    subtotal: int = Field(description="Price of all items")
    discount: int = Field(description="Discount by promo code")
    delivery: int = Field(description="Delivery price")
    total: int = Field(description="Total to pay")
