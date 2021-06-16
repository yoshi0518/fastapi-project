from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routers import comments, posts, users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    comments.router,
    prefix="/comments",
    tags=["comments"],
)

app.include_router(
    posts.router,
    prefix="/posts",
    tags=["posts"],
)

app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
)


@app.get("/")
def root():
    return {"message": "v1 root"}