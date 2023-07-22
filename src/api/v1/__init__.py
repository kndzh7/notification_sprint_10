from fastapi import APIRouter

from .email import router as sched_router
from .websocket import router as manager_router

router = APIRouter(prefix="/v1")
router.include_router(sched_router)
router.include_router(manager_router)
