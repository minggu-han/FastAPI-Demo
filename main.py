import asyncio
import time

from fastapi import FastAPI, Path, Query
from pydantic import BaseModel,Field

class User(BaseModel):
    username: str = Field(min_length=8, max_length=20, description='用户名')
    password: str = Field(min_length=8, max_length=20, description='密码')
    isAdmin: bool = Field(default=False, description='是否管理员')

#创建 FastAPI 实例
#启动项目    uvicorn main:app --reload
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


#请求体参数
@app.post("/register")
async def login(user: User):
    return user

@app.get("/sync")
def func_sync():
    start = time.time()
    for i in range(10):
        time.sleep(1)
    end = time.time()
    return {"consume": f'{end - start:.2f}s'}

@app.get("/async")
async def func_async():
    start = time.time()
    tasks = [asyncio.sleep(1) for i in range(10)]
    await asyncio.gather(*tasks)
    end = time.time()
    return {"consume": f'{end - start:.2f}s'}

#路径参数
#Path 函数
#... 表示必填

#http://127.0.0.1:8000/book/1
@app.get("/book/{book_id}")
async def func_book(book_id: int = Path(..., gt=0, lt=101, description='书籍的编号')):
    return {"book_id": book_id}

#查询参数

#http://127.0.0.1:8000/books/book_list?bookName=%E5%AE%8C%E7%BE%8E%E4%B8%96%E7%95%8C&pageIndex=1&pageSize=10
@app.get("/books/book_list")
async def func_books(
        bookName: str = Query(description="书名")
        , pageIndex: int = Query(1, gt=0, lt=101, description="页码")
        , pageSize: int = Query(10, description="页数")
):
    return {"bookName": bookName, "pageIndex": pageIndex, "pageSize": pageSize}