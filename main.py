import time
#from multiprocessing import Pool
import numpy as np


from pebble import ProcessPool as Pool
from concurrent.futures import TimeoutError

def slow_task(params):
    print("process action")
    print(params)
    time.sleep(5)
    print("process completed")
    return params

def slow_task_with_more_params(params, more_params):
    print("process action")
    print(params, more_params)
    time.sleep(5)
    print("process completed")
    return params, more_params


def task_submitter(func, *iterables, n_workers=1, n_tries=1, timeout=None):
    n_tries = int(n_tries)
    while n_tries > 0:
        try:
            with Pool(n_workers) as p:
                result_futures = p.map(func, *iterables, timeout=timeout)
                results = [r for r in result_futures.result()]
                print("Results Done!")
                return results
        except TimeoutError as e:
            n_tries -= 1
            print("Error! {} attempts left".format(n_tries), e)
    print("All attempts timed out. Returning empty list")
    return []


if __name__  == '__main__':
    param = {'a': 1, 'vals': np.random.rand(1, 1)}
    param2 = {'b': 2, 'vals': np.random.rand(1, 1)}
    params = [param]*4
    more_params = [param2] * 4
    task_submitter(slow_task, params, n_workers=4, n_tries=2, timeout=10)

