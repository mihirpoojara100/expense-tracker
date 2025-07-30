from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


async def get_users():
    return {"message": "Hello, World!"}


router.get("/")(get_users)
