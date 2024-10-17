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
    List[int]: number of sculptures on each platform
    """
    # --- Constraints Checks ---
    if any(h < 0 for h in heights) or any(w < 0 for w in widths) or n <= 0 or W <= 0:
        raise ValueError("All inputs must be non-negative.")

    # Find the valley (local minimum) in the unimodal sequence
    valley = find_valley(heights)

    # Try to fit all sculptures on a single platform if possible
    total_width = sum(widths)
    max_height = max(heights)
    if total_width <= W:
        # All sculptures fit on one platform
        return 1, max_height, [n]

    # Initialize variables
    platforms = []  # List of platforms with (max_height, total_width)
    sculptures_per_platform = []  # Number of sculptures on each platform

    # --- Left Partitioning (Left to Valley-1) ---
    current_width = 0
    current_max_height = 0
    current_count = 0
    left_platforms = []
    left_sculptures = []

    for i in range(valley):
        if current_width + widths[i] > W:
            left_platforms.append((current_max_height, current_width))
            left_sculptures.append(current_count)
            current_width = 0
            current_max_height = 0
            current_count = 0
        current_width += widths[i]
        current_max_height = max(current_max_height, heights[i])
        current_count += 1

    if current_count > 0:
        left_platforms.append((current_max_height, current_width))
        left_sculptures.append(current_count)

    # --- Right Partitioning (n-1 down to Valley+1) ---
    current_width = 0
    current_max_height = 0
    current_count = 0
    right_platforms = []
    right_sculptures = []

    for i in range(n - 1, valley, -1):
        if current_width + widths[i] > W:
            right_platforms.append((current_max_height, current_width))
            right_sculptures.append(current_count)
            current_width = 0
            current_max_height = 0
            current_count = 0
        current_width += widths[i]
        current_max_height = max(current_max_height, heights[i])
        current_count += 1

    if current_count > 0:
        right_platforms.append((current_max_height, current_width))
        right_sculptures.append(current_count)

    # Reverse right platform lists to maintain order
    right_platforms.reverse()
    right_sculptures.reverse()

    # --- Handle the Valley ---
    valley_width = widths[valley]
    valley_height = heights[valley]

    # Try to fit the valley onto the last left platform
    if left_platforms and left_platforms[-1][1] + valley_width <= W:
        # Update the last left platform's max_height and total_width
        new_max_height = max(left_platforms[-1][0], valley_height)
        new_total_width = left_platforms[-1][1] + valley_width
        left_platforms[-1] = (new_max_height, new_total_width)
        left_sculptures[-1] += 1
    else:
        # Try to fit the valley onto the first right platform
        if right_platforms and right_platforms[0][1] + valley_width <= W:
            # Update the first right platform's max_height and total_width
            new_max_height = max(right_platforms[0][0], valley_height)
            new_total_width = right_platforms[0][1] + valley_width
            right_platforms[0] = (new_max_height, new_total_width)
            right_sculptures[0] += 1
        else:
            # Valley gets its own platform
            left_platforms.append((valley_height, valley_width))
            left_sculptures.append(1)

    # Combine the left and right platforms
    platforms = left_platforms + right_platforms
    sculptures_per_platform = left_sculptures + right_sculptures

    # Compute total height
    total_height = sum([h for h, w in platforms])

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