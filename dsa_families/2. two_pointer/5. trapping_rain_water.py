# Today’s problem: Trapping Rain Water

# Bars of height height[i]. 
# Rain sits on top of bars (not one container between two walls). 
# Water above index i cannot go higher than the shortest of the tallest wall to the left and the tallest wall to the right, minus height[i]. 
# Return total water.


#height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [3,2,3]

def trapping_rain_water(height: list):

    length = len(height) - 1

    M = 1
    L = M - 1
    R = M + 1

    water = 0

    while (M < length):
        tallest_left = height[L]
        tallest_right = height[R]
        while (R <= length):
            if tallest_right < height[R]:
                tallest_right = height[R]
            R = R + 1
        while (L >= 0):
            if tallest_left < height[L]:
                tallest_left = height[L]
            L = L - 1
        
        cap = min(tallest_left, tallest_right)

        water = water + (max((cap - height[M], 0)))

        M = M + 1
        L = M - 1
        R = M + 1

    return water

def trapping_rain_water_optimized(height: list):

    length = len(height) - 1
    i = 0
    j = length
    k = 0

    water = 0

    left = []
    right = []

    t_l = 0
    t_r = 0

    # left pass
    while (i<=length):

        print("t_l:", t_l)

        if i == 0:
            left.append(0)
            i = i+1
        else:
            t_l = max(t_l, height[i-1])
            left.append(t_l)
            i = i+1

    print("left:",left)

    while (j >= 0):

        print("t_r:", t_r)

        if j == length:
            right.append(0)
            j = j-1

        else:
            t_r = max(t_r, height[j+1])
            right.append(t_r)
            j = j-1

    right.reverse()
    print("right:", right)

    while (k<=length):
        cap = min(left[k], right[k])
        temp_water = max((cap - height[k]), 0)
        water = water + temp_water
        print("water:", water)

        k = k + 1

    return water


def trapping_rain_water_for(height: list):
    # Same method as trapping_rain_water_optimized. for idx in range(n) is 0, 1, ..., n-1.
    n = len(height)
    left = []
    right = []
    t_l = 0
    t_r = 0
    water = 0

    for idx in range(n):
        if idx == 0:
            left.append(0)
        else:
            t_l = max(t_l, height[idx - 1])
            left.append(t_l)

    # range(n - 1, -1, -1) is n-1, n-2, ..., 0 (last bar → first bar)
    for idx in range(n - 1, -1, -1):
        if idx == n - 1:
            right.append(0)
        else:
            t_r = max(t_r, height[idx + 1])
            right.append(t_r)
    right.reverse()

    for idx in range(n):
        cap = min(left[idx], right[idx])
        water = water + max(cap - height[idx], 0)

    return water


print(trapping_rain_water_optimized(height))
print(trapping_rain_water_for(height))
            

