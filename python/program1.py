from typing import List, Tuple

def program1(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 1
    
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

    platforms = []
    current_platform = []
    current_width = 0
    current_max_height = 0
    
    for i in range(n):
        if current_width + widths[i] <= W:
            # Add to current platform
            current_platform.append(i + 1)  # Store the index of the sculpture (1-based index)
            current_width += widths[i]
            current_max_height = max(current_max_height, heights[i])
        else:
            # Finalize current platform
            platforms.append((current_max_height, len(current_platform)))
            # Start new platform
            current_platform = [i + 1]
            current_width = widths[i]
            current_max_height = heights[i]
    
    # Append the last platform
    platforms.append((current_max_height, len(current_platform)))

    # Calculate total height
    total_height = sum(platform[0] for platform in platforms)
    
    # Extract number of sculptures on each platform
    num_statues = [platform[1] for platform in platforms]
    
    # Return the number of platforms, total height, and the number of statues per platform
    return len(platforms), total_height, num_statues

if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_statues = program1(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_statues:
        print(i)

    """
    ProblemS1: Monotonically Non-Increasing Heights
    
    Since the heights are given in a monotonically non-increasing order,
    the tallest sculptures are encountered first, followed by shorter ones.
    A greedy algorithm for this can simply pack the sculptures onto the platforms
    as long as the width allows, and once it exceeds the width, move to a new platform.
    
    Algorithm1 (for ProblemS1):
    
    - Initialize the platform's width and height to zero.
    - Traverse the sculptures from left to right, placing them on the current platform if the width allows.
    - If the width exceeds W, finalize the current platform and move to the next, making sure to reset the width counter.
    - Return the total number of platforms used and the cost (sum of the tallest sculptures on each platform).
    
    """

# Notes: 

# This approach assumes a greedy allocation strategy, which works for the first part of the problem, (Program 1).
# Later, when we implement a dynamic programming approach, the logic will change significantly to handle more complex constraints or optimizations.

# The greedy algorithm attempts to pack sculptures on platforms, maintaining the width constraint W.
# It keeps adding sculptures to the current platform as long as the total width does not exceed W.
# When the width limit is reached, a new platform is started, and the process continues.
# It calculates the height of the tallest sculpture on each platform and sums them to get the total height. 

# Platforms: The platforms list keeps track of the platforms created, storing the tallest height and the number of sculptures per platform.
# current_platform: This temporarily holds sculptures being placed on the current platform.
# current_width: This accumulates the widths of sculptures as they are added to the platform.
# Once adding a new sculpture would exceed W, the current platform is finalized, and a new platform begins.
# current_max_height: Tracks the maximum height of sculptures on the current platform.

# Output:
# m: The number of platforms used.
# total_height: The sum of the tallest sculptures on each platform.
# num_statues: The number of sculptures placed on each platform.


# Test Case 1 (From the GradeScope)(Program 1):
# Input:
#   7 10
#   21 19 17 16 11 5 1
#   7 1 2 3 5 8 1

# Expected:
#   3
#   42
#   3
#   2
#   2