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
Explanation:

This program arranges sculptures with unimodal heights (first decreasing, then increasing)
onto platforms while minimizing the total height and the number of platforms.

Algorithm Steps:
1. Find the Valley:
- Identify the index where the heights transition from decreasing to increasing.
- This is done using the find_valley function.

2. Process Left Partition (Before the Valley):
- Iterate from index 0 to valley - 1.
- Add sculptures to the current platform until the width limit W is exceeded.
- When the limit is exceeded, finalize the current platform and start a new one.
- Keep track of the maximum height on each platform.

3. Process Right Partition (After the Valley):
- Iterate from index n - 1 down to valley + 1, in reverse to maintain order.
- Similar to the left partition, add sculptures to platforms based on width constraints.
- Reverse the lists at the end to restore the original order.

4. Handle the Valley Sculpture:
- Attempt to add the valley sculpture to the last left platform if possible.
- Conditions: Total width does not exceed W.
- If not possible, attempt to add it to the first right platform.
- If neither is possible, the valley sculpture gets its own platform.

5. Combine Platforms and Calculate Total Height:
- Merge the left and right platforms.
- Compute the total height by summing the maximum heights of all platforms.
- Return the number of platforms, total height, and the number of sculptures on each platform.

Key Points:
- Order Preservation: The sculptures are arranged in their original order.
- Width Constraint: No platform exceeds the maximum width W.
- Height Minimization: By grouping sculptures carefully, the total height is minimized.
- Valley Handling: Special care is taken to place the valley sculpture efficiently.

Variables:
- left_platforms: Stores platforms from the left partition.
- right_platforms: Stores platforms from the right partition (reversed to maintain order).
- current_width: Tracks the cumulative width of sculptures on the current platform.
- current_max_height: Tracks the maximum height on the current platform.
- current_count: Counts the number of sculptures on the current platform.
- platforms: Combined list of all platforms.
- sculptures_per_platform: Number of sculptures on each platform.
- total_height: Sum of the tallest sculptures on each platform.

Usage:
- Run the program and input n and W.
- Provide the list of heights and widths.
- The program outputs the number of platforms, total height, and sculptures per platform.
"""