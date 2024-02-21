# -*- coding: utf-8 -*-

import asyncio
import time

async def read_books():
    print("----------------读书协程开始-------------")
    for i in range(10):
        await read_book(i)
    print("----------------读书协程关闭-------------")
    

async def read_book(book_id):
    await asyncio.sleep(1)
    print('done reading:', book_id)

#为了标识执行代码的入口和避免文件被导入时被执行，我们可以将执行代码放入main函数中。
if __name__ == '__main__':
    asyncio.run(read_books())
