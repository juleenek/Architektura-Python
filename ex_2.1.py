#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

def type_logger(func):
    @functools.wraps(func)
    def wrapped_function(*args, **kwargs):

        arg_types = {func.__code__.co_varnames[i]: type(arg).__name__ for i, arg in enumerate(args)}
        kwarg_types = {name: type(value).__name__ for name, value in kwargs.items()}
        combined_types = {**arg_types, **kwarg_types}
        
        print("--------------------------")
        print(f"Argument types for function '{func.__name__}': {combined_types}")
        print("--------------------------")
        
        return func(*args, **kwargs)
    
    return wrapped_function


@type_logger
def demo_function1(a, b, c=3, d='default'):
    print("First function body executed.")
    
@type_logger
def demo_function2(x, y=42, z='hello', *args, **kwargs):
    print("Second function body executed.")

demo_function1(1, 'test', d=[1, 2, 3])
demo_function2(10, 12, 'world', 99, 100, key1='value1', key2='value2')