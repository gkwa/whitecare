import functools
import json


def memoize(func):
    cache_file = "cache.json"

    try:
        with open(cache_file, "r") as file:
            cache = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        cache = {}

    @functools.wraps(func)
    def memoizer(*args, **kwargs):
        key = (args, list(frozenset(kwargs.items())))
        key_str = json.dumps(key)
        if key_str in cache:
            return cache[key_str]
        result = func(*args, **kwargs)
        cache[key_str] = result
        with open(cache_file, "w") as file:
            json.dump(cache, file)
        return result

    return memoizer


@memoize
def function1():
    print("Running function1")
    return 1


@memoize
def function2():
    print("Running function2")
    return 2


@memoize
def function3():
    print("Running function3")
    return 3


def run_pipeline():
    result1 = function1()
    result2 = function2()
    result3 = function3()
    test_result = test_function(result1, result2, result3)
    print("Final result:", test_result)


def test_function(result1, result2, result3):
    print("Running test_function")
    return result1 + result2 + result3


run_pipeline()
