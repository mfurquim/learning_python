"""Module to test lru_cache"""
import timeit
from functools import lru_cache
from pathlib import Path

import pandas as pd
import redis
from redis_cache import RedisCache


def fibonacci(n):
    if n <= 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache
def fibonacci_cached(n):
    if n <= 1:
        return 1

    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
)

redis_cache = RedisCache(redis_client=redis_client)


@redis_cache.cache()
def fibonacci_redis(n):
    if n <= 1:
        return 1

    return fibonacci_redis(n - 1) + fibonacci_redis(n - 2)


def generate_report(name, function, n=20):
    columns = ["name_function", "number", "time_in_seconds"]
    local_report_df = pd.DataFrame(columns=columns)

    for i in range(n):
        print(f"{name}: {i}")
        function_timed_list = timeit.repeat(
            f"{name}({i})",
            setup=f"from __main__ import {name}",
            repeat=20,
            number=100,
        )

        local_report_df = pd.concat(
            [
                local_report_df,
                pd.DataFrame(
                    {
                        "name_function": name,
                        "number": i,
                        "time_in_seconds": [min(function_timed_list)],
                    },
                    index=None,
                ),
            ]
        )

    return local_report_df


def main():
    all_reports_filename = "all_reports.csv"
    all_reports_filepath = Path(__file__).parent.joinpath(all_reports_filename)

    columns = ["name_function", "number", "time_in_seconds"]
    all_reports_df = pd.DataFrame(columns=columns)

    name = "fibonacci"
    local_report_df = generate_report(name, fibonacci)
    all_reports_df = pd.concat([all_reports_df, local_report_df], ignore_index=True)

    name = "fibonacci_cached"
    local_report_df = generate_report(name, fibonacci)
    all_reports_df = pd.concat([all_reports_df, local_report_df], ignore_index=True)

    name = "fibonacci_redis"
    local_report_df = generate_report(name, fibonacci)
    all_reports_df = pd.concat([all_reports_df, local_report_df], ignore_index=True)

    all_reports_df.to_csv(all_reports_filepath, index=False)
    print(all_reports_df)


if __name__ == "__main__":
    main()
