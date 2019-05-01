# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 00:16:55 2019
@author: user"""
from datetime import datetime

prog_start_time = datetime.now()
x = 1000000000
ans = 0
epsilon = 0.01
low = 0
high = x
num_guesses = 0
while (abs(ans**2 - x) > epsilon) and (ans < x):
    if ans**2 > x:
        high = ans
    else:
        low = ans
    ans = (low + high)/2
    num_guesses += 1

print(ans)
prog_end_time = datetime.now()
prog_run_time = prog_end_time - prog_start_time
print("run time : " + str(prog_run_time))
