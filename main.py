import asyncio
import time

from fastapi import FastAPI, Path, Query, HTTPException, Depends
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel,Field

#创建 FastAPI 实例
#启动项目    uvicorn main:app --reload
app = FastAPI()

#中间件
#为每个请求添加统一的处理逻辑（记录日志、身份认证、跨域、设置响应头、性能监控等）
#执行顺序  按照代码顺序  “自下而上”

@app.middleware("http")
async def middleware1(request, call_next):
    print(f'[middleware1] start')
    response = await call_next(request)
    print(f'[middleware1] end')
    return response
@app.middleware("http")
async def middleware2(request, call_next):
    print(f'[middleware2] start')
    response = await call_next(request)
    print(f'[middleware2] end')
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}

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

#请求体参数

class User(BaseModel):
    username: str = Field(min_length=8, max_length=20, description='用户名')
    password: str = Field(min_length=8, max_length=20, description='密码')
    isAdmin: bool = Field(default=False, description='是否管理员')

@app.post("/register")
async def login(user: User):
    return user

#响应 html 格式
@app.get("/html", response_class=HTMLResponse)
async def html():
    return "<h1>Hello World</h1>"

#响应 文件 格式
@app.get("/file")
async def file():
    return FileResponse("./files/dog_and_girl.jpeg", media_type="image/jpeg")

#自定义响应格式
class News(BaseModel):
    id : int
    title: str
    content: str = Field(None)
@app.get("/news/{news_id}", response_model=News)
async def news(news_id : int):
    return News(id=news_id, title='标题')

#异常处理
@app.get("/news_details/{news_id}")
async def news(news_id : int):
    news_id_list = [1,2,3,4,5,6]
    if news_id not in news_id_list:
        raise HTTPException(status_code=404,detail='id不存在！')
    return {"id": news_id}

#分页参数共享
#1、依赖项
#2、 from fastapi import Depends
async def common_parameters(
        skip: int = Query(0, gt=0),
        limit: int = Query(10, gt=0, lt=101),
):
    return {"skip": skip, "limit": limit}

#3、依赖注入
@app.get("/depends1")
async def depends1(commons = Depends(common_parameters), name: str = Query(default=None,description="名称")):
    return commons
@app.get("/depends2")
async def depends2(commons = Depends(common_parameters)):
    return commons






























































