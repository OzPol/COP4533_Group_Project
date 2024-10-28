from typing import List, Tuple

def program3(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 3
    
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

    """
    Brief explanation of our approach to program3

    We explore all possible ways to arrange the sculptures (in order) into platforms (2^n-1 possible combinations). 
    We only consider the arrangements with no platforms that exceeds W (i.e., feasible arrangements).
    From the set of feasible arrangements, we then pick the arrangement that minimizes the total height as the solution.

    The operations of checking for feasible arrangements and tracking the minimized total height are done as we go through the recursion to keep the time complexity of the program at theta(n*2^n-1). 
    """

    # feasible_arrangements = {} # for debugging

    min_cost = float('inf') # initialize to infinity
    best_arrangement = None # the arrangement with a minimized total height cost

    def generate_arrangements(current, start, current_cost):
        """
        Generates all 2^n-1 possible combinations of sculptures arranged into platforms (in order). 

        Parameters:
        - current: The current list of platforms being constructed.
        - start: The starting index of the current arrangement step.
        - current_cost: The accumulated cost of the current arrangement based on the tallest sculpture in each platform.
        """

        nonlocal min_cost, best_arrangement

        # Base case: end of the sculpture sequence
        if start >= n:
            #feasible_arrangements[current_cost] = current
            if current_cost < min_cost:
                min_cost = current_cost
                best_arrangement = current[:] 
        else:
            platform_width_sum = 0
            platform_max_height = 0

            for i in range(start, n):
                platform_width_sum += widths[i]
                
                # check if arrangement is feasible
                if platform_width_sum <= W:
                    platform_max_height = max(platform_max_height, heights[i])

                    # Update the arrangement cost with the height of this platform
                    cost = current_cost + platform_max_height

                    # Create the next arrangement with the current platform
                    next_arrangement = current + [list(range(start, i + 1))]
                    
                    # Recursively generate arrangements for the remaining elements
                    generate_arrangements(next_arrangement, i + 1, cost)

    generate_arrangements([], 0, 0)

    sculptures_count = [len(platform) for platform in best_arrangement]

    """
    # uncomment when debugging
    print("Feasible Arrangements:")
    for cost, arr in feasible_arrangements.items():
        print(f"Cost: {cost}, Arrangement: {arr}")
    """
    
    """
    # uncomment when debugging
    print(best_arrangement)
    print()
    """

    return len(best_arrangement), min_cost, sculptures_count


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_statues = program3(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_statues:
        print(i)

