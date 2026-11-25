from fastapi.routing import APIRouter

from src.config import APP_VERSION
from src.schema.outputs import AppInfoOutput

router = APIRouter(prefix="/app-info")


@router.get("/versions", operation_id="get_app_info", response_model=AppInfoOutput)
async def get_app_info() -> AppInfoOutput:
    return AppInfoOutput(back_version=APP_VERSION)
