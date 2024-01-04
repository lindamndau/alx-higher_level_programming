#!/usr/bin/python3
for i in range(10):
   for j in range(i+1, 10):
    if i != 0 or j != 0:
        print(f"{i}{j}", end=",")
print("\b\b")
