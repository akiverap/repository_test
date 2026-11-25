import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

from src.config import APP_VERSION, settings
from src.route.general_info.app_info import router as app_info_router
from src.route.shop.cart import router as cart_router

if settings.ENVIRONMENT == 'DEVELOPMENT':
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=APP_VERSION,
        openapi_url=f"{settings.BASE_ROUTE_PATH}/openapi.json",
        docs_url=f"{settings.BASE_ROUTE_PATH}/docs",
    )
else:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=APP_VERSION,
        openapi_url=None,
        docs_url=None,
        redoc_url=None,
    )

router = APIRouter(prefix=settings.BASE_ROUTE_PATH)

router.include_router(app_info_router, tags=['App info'])
router.include_router(cart_router, tags=['Cart'])

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        host='localhost',
        port=8000,
        reload=True,
    )
