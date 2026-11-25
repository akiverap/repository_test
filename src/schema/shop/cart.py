from pydantic import BaseModel, ConfigDict, Field


class CartItemInput(BaseModel):
    model_config = ConfigDict(title="shop.CartItemInput", extra='forbid')

    title: str = Field(description="Item title", min_length=1, max_length=100)
    price: int = Field(description="Price in gold", ge=1)
    quantity: int = Field(description="How many items", ge=1, le=100)


class CartInput(BaseModel):
    model_config = ConfigDict(title="shop.CartInput", extra='forbid')

    items: list[CartItemInput] = Field(description="Items in cart", min_length=1)
    promo_code: str | None = Field(description="Promo code", pattern=r"^[A-Z0-9]{4,12}$", default=None)
