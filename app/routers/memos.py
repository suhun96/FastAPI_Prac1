from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session
from typing         import List

from models     import Memo
from connection import get_db
from schema     import *

router = APIRouter(
    prefix="/memos",
    tags=["memos"]   
)

@router.get('/memos', response_model = List[MemoCreated])
async def get_memo(db: Session = Depends(get_db)):
    memos = db.query(Memo).all()
    return memos

# @router.post('/memos', response_model = MemoCreated)
# async def register_memo(
#     req: MemoRequestCreate = Depends(MemoRequestCreate), 
#     db: Session = Depends(get_db)):

#     memo = Memo(
#         title = req.title,
#         content = req.content,
#         is_favorite = req.is_favorite
#     )

#     db.add(memo)

#     db.commit()
#     db.refresh(memo)
#     return memo

@router.post('/memos')
async def resister_memo_2(input_data : MemoRequestCreate, db: Session = Depends(get_db)):
    
    memo = Memo(
        title = input_data.title,
        content = input_data.content,
        is_favorite = input_data.is_favorite
    )
    db.add(memo)
    db.commit(),
    db.refresh(memo)
    
    return memo