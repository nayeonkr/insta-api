from fastapi import FastAPI
from routers import posts
app = FastAPI()

# 라우터는 여기에 붙인다
# from routers import posts
# app.include_router(posts.router)


app.include_router(posts.router)