import asyncio

class AsyncIterator:
    def init(self):
        self.counter = 0

    def aiter(self):
        return self

    async def anext(self):

        if self.counter >= 10:
            raise StopAsyncIteration

        self.counter += 1

        await asyncio.sleep(1)

        return self.counter

async def main():

    async for item in AsyncIterator():
        print(item)

asyncio.run(main())