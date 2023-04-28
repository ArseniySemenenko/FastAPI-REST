from fastapi import FastAPI
import sys
sys.path.insert(0,"..")

from routers.user_router import router as user_router

app = FastAPI()

app.include_router(user_router)

