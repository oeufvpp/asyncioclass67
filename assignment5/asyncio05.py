# assignment 5
from random import random
import asyncio

async def task_rice():
    value = 1+random()
    print("Rice cooking for ",value)
    await asyncio.sleep(value)
    print(value)
async def task_noodle():
    value = 1+random()
    print("Noodle cooking for ",value)
    await asyncio.sleep(value)
    print(value)
async def task_curry():
    value = 1+random()
    print("Curry cooking for ",value)
    await asyncio.sleep(value)
    print(value)
async def main():
    #create many tasks
    task1 = asyncio.create_task(task_curry(), name='Curry')
    task2 = asyncio.create_task(task_noodle(), name='Noodle')
    task3 = asyncio.create_task(task_rice(),name='rice')

    all_tasks = [task1,task2,task3]
    # wait for all tasks to complete
    done, pending = await asyncio.wait(all_tasks,return_when=asyncio.FIRST_COMPLETED)
    first = done.pop()
    print(first.get_name(),"finished cooking first")
    # report results

    

# start the asyncio program
asyncio.run(main())