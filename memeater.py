#!/usr/bin/python3
# MemEater
# Copyright (C) 2023 Xina. All rights reserved
from ctypes import *

setEatenMem = int(input("How much memory should we eat? (Kilobyte in integer):"))
while setEatenMem <= 0:
    print("Invalid input, please input an integer.")
    setEatenMem = int(input("How much memory should we eat? (Kilobyte in integer):"))

eatenMem = create_string_buffer(setEatenMem*1024)
print(str(setEatenMem) + " Kilobytes of memory has ben eaten!")

releaseEatenMem = str(input("Release eaten memories now?(y/n):"))
while releaseEatenMem != "y":
    releaseEatenMem = str(input("Release eaten memories now?(y/n):"))

eatenMem = None