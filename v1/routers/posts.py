from fastapi import APIRouter
import requests

from ..utils import logging

router = APIRouter(route_class=logging.LoggingContextRoute)

url = 'https://jsonplaceholder.typicode.com/posts/'
response = requests.get(url)
status_code = response.status_code
posts = response.json()


@router.get("/")
async def read_posts():
    return {
        "status_code": status_code,
        "posts": posts,
    }
