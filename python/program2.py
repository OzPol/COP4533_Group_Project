from typing import List, Tuple

# Helper function to find the valley (local minimum)
def find_valley(heights: List[int]) -> int:
    """
    Finds the index of the local minimum (valley) in the sequence.
    The valley is where the sequence transitions from non-increasing to non-decreasing.
    """
    n = len(heights)

    # Look for the transition from decreasing to increasing
    for i in range(1, n):
        if heights[i] > heights[i - 1]:  # Found the transition point
            return i - 1  # Index of the local minimum (valley)

    # If no transition is found, the last element is the minimum
    return n - 1

def program2(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 2
    
    Parameters:
    n (int): number of sculptures
    W (int): width of the platform
    heights (List[int]): heights of the sculptures
    widths (List[int]): widths of the sculptures

    Returns:
    int: number of platforms used
    int: optimal total height
    List[int]: number of statues on each platform
    """
    ############################
    # Add you code here
    ############################

    # --- Constraints Checks ---
    if any(h < 0 for h in heights) or any(w < 0 for w in widths) or n < 0 or W < 0:
        raise ValueError("All inputs must be non-negative.")

    # Find the valley (local minimum) in the unimodal sequence
    valley = find_valley(heights)
    
    platforms = []  # Store the number of sculptures on each 
    platforms2 = []  # Store the number of sculptures on each on second platform
    sculptures_per_platform = []  # Track sculptures on the current platform
    sculptures_per_platform2 = [] #on second platform
    current_width = 0  # Track the width used on the current platform
    current_width2 = 0  
    current_max_height = 0  # Track the max height on the current platform
    current_max_height2 = 0 
    current_count = 0
    current_count2 = 0
    current_platform_start=0
    current_platform2_start=n-1
    stophere = 0 #Store where 
    Valley_reached1=1 #store if valley is reached from front
    Valley_reached2=1 #store if valley is reached from end
    missile=0 #a testing probe

#check if valley is at the end
    if valley==n-1:
        Valley_reached2=0
    elif valley==0:
        Valley_reached1=0

#go through the sculptures from front and back same time
    for i in range(n):
        if current_width + widths[i] > W:
            if i<=valley:
                platforms.append(current_max_height) #add the platform highest to the end of platforms list 1
                sculptures_per_platform.append(current_count) #store the number of sculpture on platform to 
                current_width, current_max_height, current_count = 0, 0, 0 #reset cursor
                current_platform_start=i #store the beginning index of next platform
            else:
                Valley_reached1=0 #will force front treversing list not adding new ones
                current_width, current_max_height, current_count = 0, 0, 0
        current_width += widths[i]*Valley_reached1 #if valley reached, all goes to 0
        current_max_height = max(current_max_height, heights[i])*Valley_reached1 
        current_count += 1
    # treverse from end stop after pass valley
        if current_width2 + widths[n-1-i] > W:
            if n-1-i>valley: 
                platforms2.insert(0,current_max_height2) #put the newly added platform at the front of platform list2
                sculptures_per_platform2.insert(0,current_count2) #store newly added playform sculpture count at the front of list2
                #missile=current_count2
                current_width2, current_max_height2, current_count2 = 0, 0, 0 #reset
                current_platform2_start=n-1-i
            else:
                Valley_reached2=0 #if valley reached from the backward treverse
                current_width2, current_max_height2, current_count2 = 0, 0, 0
        current_width2 += widths[n-1-i]*Valley_reached2 #capture current platform width, if valley reached will set to 0 and not be added
        current_max_height2 = max(current_max_height2, heights[n-1-i])*Valley_reached2
        current_count2 += 1

    added=False #check if the last platform is added

    #add sculptures in the ambiguous to platform that minimize total height
    if heights[current_platform_start]>=heights[current_platform2_start]: #front higher, front takes all it can
        current_width, current_max_height, current_count = 0, 0, 0
        current_width2, current_max_height2, current_count2 = 0, 0, 0
        for j in range(current_platform_start,current_platform2_start+1):#loop through the ambiguous area and add 1 platform
            if current_width + widths[j]>W:
                platforms.append(current_max_height)
                sculptures_per_platform.append(current_count)
                stophere = j
                added=True #flag for added, so not going to add beyond stophere in the catch
                break
            current_width += widths[j]
            current_max_height = max(current_max_height, heights[j])
            current_count += 1
        if current_count>0 and not added: #catch if all scultptures in the area added but not a full platform
            platforms.append(current_max_height)
            sculptures_per_platform.append(current_count)
        if len(sculptures_per_platform)!=0 and sculptures_per_platform[-1]<current_platform2_start-current_platform_start+1: #if there are remaining, insert to front of list 2
            platforms2.insert(0,heights[current_platform2_start])
            sculptures_per_platform2.insert(0,current_platform2_start-stophere+1)
        platforms+=platforms2 #concatnate two list
        sculptures_per_platform+=sculptures_per_platform2 #concatnate two list
    else: #end has higher height
        current_width, current_max_height, current_count = 0, 0, 0
        current_width2, current_max_height2, current_count2 = 0, 0, 0
        for j in range(current_platform2_start,current_platform_start-1,-1):#loop through the ambiguous area and from back add 1 platform
            if current_width2 + widths[j]>W:
                platforms2.insert(0,current_max_height2)
                sculptures_per_platform2.insert(0,current_count2)
                stophere = j
                added=True #catch if all scultptures in the area added but not a full platform
                break
            current_width2 += widths[j]
            current_max_height2 = max(current_max_height2, heights[j])
            current_count2 += 1
        if current_count2>0 and not added:
            platforms2.insert(0,current_max_height2)
            sculptures_per_platform2.insert(0,current_count2)
        if len(sculptures_per_platform2)!=0 and sculptures_per_platform2[0]<current_platform2_start-current_platform_start+1:
            platforms.append(heights[current_platform_start])
            sculptures_per_platform.append(stophere-current_platform_start+1)#fix me here
        platforms+=platforms2 #concatnate two list
        sculptures_per_platform+=sculptures_per_platform2 #concatnate two list

    total_height = sum(platforms)
    #sculptures_per_platform.append([current_platform_start,current_platform2_start,missile, platforms])
    return len(platforms), total_height, sculptures_per_platform


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_statues = program2(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_statues:
        print(i)


"""
ProblemS2: Unimodal Heights
In this case, the heights follow a unimodal pattern.
The heights decrease up to a certain point and then increase again.
The greedy strategy here needs to respect the unimodal structure
by treating the sequence as two separate parts: one where the heights decrease,
and one where they increase. Sculptures from the left side are packed first,
followed by sculptures from the right side.

Keyword arguments:
argument -- description
Return: return_description

Algorithm2 (for ProblemS2):
1. Identify the peak point k where the heights stop decreasing and begin increasing.
2. Traverse the left portion (before the peak), packing sculptures as long as width permits.
3. Then, traverse the right portion (after the peak) using a similar packing strategy.
4. Return the total platforms and the minimized cost.

"""


# Notes: 
# This greedy algorithm works by iterating through the sculptures and placing them on platforms as long as their widths fit. 
# When the width limit is exceeded, a new platform is created.
# The goal is to minimize the total number of platforms and the total height.

# 1. Platforms: A list to store the details of each platform.
# 2. current_platform: Tracks the sculptures on the current platform.
# 3. current_width: Tracks the sum of widths of the sculptures on the current platform.
# 4. current_max_height: Keeps the height of the tallest sculpture on the current platform.
# 5. When the width limit is exceeded, the current platform is "finalized," and a new platform is started.


"""
Program1 handles the monotonically non-increasing heights (ProblemS1), where it simply packs sculptures from left to right.
Program2 deals with the unimodal heights (ProblemS2), first packing sculptures before the peak and then handling the sculptures after the peak.
Keep in mind that the heights are unimodal, meaning they increase and then decrease.
"""