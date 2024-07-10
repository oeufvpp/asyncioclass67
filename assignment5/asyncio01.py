# example of waiting for all tasks to complete
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 1 and 0
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value 
    print(f'>task {arg} done with {random}')

#main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for the program to complete
    done, pending = await asyncio.wait(tasks)
    # report result
    print("All done")

asyncio.run(main())