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

    if len(heights) != n or len(widths) != n:
        raise ValueError("The number of heights and widths must match the number of sculptures.")

    # Find the valley (local minimum) in the unimodal sequence
    valley = find_valley(heights)

    platforms = []  # Store the number of sculptures on each platform
    current_platform = []  # Track sculptures on the current platform
    current_width = 0  # Track the width used on the current platform
    current_max_height = 0  # Track the max height on the current platform

    # --- Traverse Left Side of the Valley (non-increasing) ---
    for i in range(valley + 1):
        if current_width + widths[i] <= W:
            current_platform.append(i + 1)  # Store 1-based index of sculpture
            current_width += widths[i]
            current_max_height = max(current_max_height, heights[i])
        else:
            # Finalize the current platform
            platforms.append((current_max_height, len(current_platform)))
            # Start a new platform
            current_platform = [i + 1]
            current_width = widths[i]
            current_max_height = heights[i]

    # Add the last platform on the left side
    platforms.append((current_max_height, len(current_platform)))

    # Reset for the right side traversal
    current_platform = []
    current_width = 0
    current_max_height = 0

    # --- Traverse Right Side of the Valley (non-decreasing) ---
    for i in range(valley + 1, n):
        if current_width + widths[i] <= W:
            current_platform.append(i + 1)  # Store 1-based index of sculpture
            current_width += widths[i]
            current_max_height = max(current_max_height, heights[i])
        else:
            # Finalize the current platform
            platforms.append((current_max_height, len(current_platform)))
            # Start a new platform
            current_platform = [i + 1]
            current_width = widths[i]
            current_max_height = heights[i]

    # Add the last platform on the right side
    platforms.append((current_max_height, len(current_platform)))

    # Calculate total height and number of sculptures per platform
    total_height = sum(platform[0] for platform in platforms)
    num_statues = [platform[1] for platform in platforms]

    return len(platforms), total_height, num_statues


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