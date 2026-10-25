
from ast import And
from operator import index
from turtle import width
from unittest import skip


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
answer = 49

def max_water(height: list):
    L = 0
    R = L + 1
    length = len(height) - 1
    max_water = 0
    print("max_water:", max_water)


    while( L < length ):

        shorter = min(height[L], height[R])
        print("shorter:", shorter)
        width = R - L
        print("width", width)
        water = width * shorter

        if water > max_water:
            max_water = water

        if R == length:
            L = L + 1
            R = L + 1

        elif R < length:
            R = R + 1
        
        else:
            ValueError("L is greater than R")

    return max_water


def max_water_optimized(height: list):
    length = len(height) - 1
    L = 0
    R = length

    max_water = 0

    while (L < R):

        if height[L] < height[R]:
            smaller = height[L]
            width = R - L
            water = smaller * width
            if water > max_water:
                max_water = water
            L = L + 1

        else:
            smaller = height[R]
            width = R - L
            water = smaller*width
            if water > max_water:
                max_water = water
            R = R - 1

    return max_water
        
print(max_water_optimized(height))