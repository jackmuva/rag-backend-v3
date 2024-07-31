from fastapi import APIRouter

healthcheck_router = r = APIRouter()

@r.get("")
async def returnStatus():
    return "Healthy"