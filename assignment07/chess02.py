import time
import asyncio

my_compute_time = 0.1  
opponent_compute_time = 0.5  
opponents = 24  
move_pairs = 30 

async def game(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f"Board {x} ({i+1}) Judit move.")
        
        await asyncio.sleep(opponent_compute_time)
        print(f"Board {x} ({i+1}) Opponent move.")
        
    print(f"Board {x+1} Finished  {round(time.perf_counter() - board_start_time)} secs\n")
    return round(time.perf_counter() - board_start_time)

async def main():
    start_time = time.perf_counter()
    board_time = 0
    tasks = [game(board) for board in range(opponents)]
    results = await asyncio.gather(*tasks)
    board_time = sum(results)
    
    print(f"Exhibition finished in {board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")

asyncio.run(main())