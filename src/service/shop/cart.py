from src.config import settings
from src.const.promo_code import PROMO_CODES
from src.exception.common import BadRequestException
from src.schema.outputs import CartOutput
from src.schema.shop.cart import CartInput


class CartService:

    @classmethod
    def calculate(cls, cart: CartInput) -> CartOutput:
        # Raises: BadRequestException
        subtotal = sum(item.price * item.quantity for item in cart.items)

        discount = 0
        if cart.promo_code is not None:
            if cart.promo_code not in PROMO_CODES:
                raise BadRequestException(f"Unknown promo code: {cart.promo_code}")
            discount = round(subtotal * PROMO_CODES[cart.promo_code] / 100)

        after_discount = subtotal - discount
        delivery = 0 if after_discount >= settings.SHOP.FREE_DELIVERY_FROM else settings.SHOP.DELIVERY_PRICE
        return CartOutput(
            subtotal=subtotal,
            discount=discount,
            delivery=delivery,
            total=after_discount + delivery,
        )
