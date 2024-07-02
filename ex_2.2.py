#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PowerGenerator:
    def __init__(self, n, a):
        self.n = n
        self.a = a
        self.current = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.n:
            result = self.a ** self.current
            self.current += 1
            return result
        else:
            raise StopIteration

a = 20
n = 3
generator = PowerGenerator(a, n)

for power in generator:
    print(power)
