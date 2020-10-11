import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # results = [executor.submit(do_something, sec) for sec in secs]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)


    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
