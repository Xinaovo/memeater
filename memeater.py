#!/usr/bin/python3
# MemEater: Eat your memories with this python script!
# Copyright (C) 2023  Xina
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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