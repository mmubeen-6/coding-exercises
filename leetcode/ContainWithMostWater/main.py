from typing import List

def container_with_most_water(height : List[int]) -> int:
    if len(height) == 0:
        return 0
    
    max_area = 0
    l, r = 0, len(height) - 1
    
    while (l < r):
        area = (r - l) * min(height[l], height[r])
        max_area = max(area, max_area)
        if (height[l] <= height[r]):
            l += 1
        elif (height[l] > height[r]):
            r -= 1       

    return max_area

if __name__ == "__main__":
    print(container_with_most_water([1,8,6,2,5,4,8,3,7]) == 49)
    print(container_with_most_water([4,3,2,1,4]) == 16)
    print(container_with_most_water([1,2,1]) == 2)
    print(container_with_most_water([1,1]) == 1)