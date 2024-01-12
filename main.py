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
        key = (args, list(set(kwargs.items())))
        key_str = json.dumps(key)
        if key_str in cache:
            return cache[key_str]
        result = func(*args, **kwargs)
        cache[key_str] = result
        with open(cache_file, "w") as file:
            json.dump(cache, file, indent=2)
        return result

    return memoizer


@memoize
def function1():
    print("running func1")
    return 1


@memoize
def function2(input1):
    print(f"running func2 with input: {input1}")
    return input1 + 2


@memoize
def function3(input2):
    print(f"running func3 with input: {input2}")
    return input2 * 3


@memoize
def function4(input3):
    print(f"running func4 with input: {input3}")
    return input3 - 4


def run_pipeline():
    result1 = function1()
    result2 = function2(result1)
    result3 = function3(result2)
    result4 = function4(result3)

    test_result = test_function(result1, result2, result3, result4)
    print("Final result:", test_result)


def test_function(result1, result2, result3, result4):
    print("Running test_function")
    return result1 + result2 + result3 + result4


run_pipeline()
