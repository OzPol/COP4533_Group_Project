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

#    if len(heights) != n or len(widths) != n:
#        raise ValueError("The number of heights and widths must match the number of sculptures.")

#    if not all(heights[i] >= heights[i + 1] for i in range(valley)) or \
#        not all(heights[i] <= heights[i + 1] for i in range(valley, n - 1)):
#        raise ValueError("Heights must be unimodal (increase to a peak and then decrease).")

    # Find the valley (local minimum) in the unimodal sequence
    valley = find_valley(heights)
    
    # Try to fit all sculptures on a single platform if possible
    total_width = sum(widths)
    max_height = max(heights)
    if total_width <= W:
        # All sculptures fit on one platform
        return 1, max_height, [n]

    platforms = []  # Store the number of sculptures on each platform
    sculptures_per_platform = []  # Track sculptures on the current platform
    current_width = 0  # Track the width used on the current platform
    current_max_height = 0  # Track the max height on the current platform
    current_count = 0
    valley_added = False  # Track if the valley was added to the left side
    
    def add_platform():
        """Finalize the current platform only if it contains sculptures."""
        nonlocal current_width, current_max_height, current_count
        if current_count > 0:  # Only add non-empty platforms
            platforms.append(current_max_height)
            sculptures_per_platform.append(current_count)
        current_width, current_max_height, current_count = 0, 0, 0

    # Traverse the left side of the valley (non-increasing)
    for i in range(valley + 1):
        if current_width + widths[i] > W:
            add_platform()
        current_width += widths[i]
        current_max_height = max(current_max_height, heights[i])
        current_count += 1
    add_platform()  # Finalize the last platform on the left side

    # Traverse the right side of the valley (non-decreasing)
    for i in range(valley + 1, n):
        if current_width + widths[i] > W:
            add_platform()
        current_width += widths[i]
        current_max_height = max(current_max_height, heights[i])
        current_count += 1
    add_platform()  # Finalize the last platform on the right side
    

    total_height = sum(platforms)
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