from fastapi.routing import APIRouter

from src.schema.outputs import CartOutput
from src.schema.shop.cart import CartInput
from src.service.shop.cart import CartService

router = APIRouter(prefix="/cart")


@router.post("/calculate",
             operation_id="calculate_cart",
             response_model=CartOutput,
             responses={400: {"description": "Unknown promo code"}})
async def calculate_cart(body: CartInput) -> CartOutput:
    return CartService.calculate(body)
