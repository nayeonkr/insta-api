from fastapi import APIRouter
from deps import SessionDep
from sqlalchemy import select
from models import Post
from schemas import PostOut

router = APIRouter(prefix='/api/posts')

@router.get('', response_model=list[PostOut])
def post_list(db: SessionDep):
    posts =  db.scalars(select(Post).order_by(Post.created_at.desc())).all()

    # for post in posts:
    #     print(post.user.username)

    return posts
