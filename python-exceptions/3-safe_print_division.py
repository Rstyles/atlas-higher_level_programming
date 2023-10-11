#!/usr/bin/python3
def safe_print_division(a: int, b: int):
    result = 0
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside Result: {}".format(result))
        return result
