import time

def game():
    start_time = time.time()
    total_time = time.time()
    for x in range(3):
        print(f"Board {x+1} start")
        for i in range(30):
            time.sleep(0.1)
            print(f"Judit moved.")
            time.sleep(0.5)
            print(f"Opponent move")
        end_time = time.time()
        elapse_time = end_time - start_time
        print(f"Board {x+1} ends Time: {elapse_time}")
    return elapse_time,total_time


if __name__ == "__main__":
    game()
    print(f"Total time: {time.perf_counter()} seconds")