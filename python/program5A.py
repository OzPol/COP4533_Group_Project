from typing import List, Tuple

    
def program5A(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5A
    
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
    
        # Base case: if there are no sculptures, return zeroes
    if n == 0:
        return 0, 0, []
    
    # memoization arrays
    min_cost_memo = [-1] * n  # tracks the min cumulative height cost up to each sculpture added
    platforms = [-1] * n  # tracks the number of platforms used to get each min_cost 
    sculptures_on_last_platforms = [-1] * n  # tracks the number of sculptures on the last platform for each min_cost
    
    # precompute cumulative widths up to each sculpture
    # we have one extra element (0) to simplify the calculations of subarray widths and keep consistency across all cases
    cumulative_width = [0] * (n+1)
    for i in range(1, n+1):
        cumulative_width[i] = cumulative_width[i-1] + widths[i-1]

    def find_min_cost(i):
        """Recursive helper function to find the minimum cost up to index i."""
        if i == 0:
            # base case: single sculpture 
            platforms[0] = 1 
            sculptures_on_last_platforms[0] = 1 
            min_cost_memo[0] = heights[0]

            return heights[0]

        if min_cost_memo[i] != -1:
            return min_cost_memo[i]  # return cached result if already computed

        min_cost = float('inf')
        max_height = 0

        # iterate through possible starting points j for the platform ending at i
        for j in range(i, -1, -1):
            max_height = max(max_height, heights[j])
            width = cumulative_width[i + 1] - cumulative_width[j]
            
            if width <= W:  # feasible platform
                curr_cost = max_height
                if j > 0:
                    curr_cost += find_min_cost(j - 1) # recursive call

                # Update the minimum height cost and platform count
                if curr_cost < min_cost:
                    min_cost = curr_cost
                    if j > 0:
                        platforms[i] = platforms[j - 1] + 1 
                    else:
                        platforms[i] = 1
                    sculptures_on_last_platforms[i] = i - j + 1

        min_cost_memo[i] = min_cost
        return min_cost

    total_min_cost = find_min_cost(n-1)

    # retrieve the number of sculptures per platform based on sculptures_on_last_platforms
    sculptures_per_platform = []
    i = n - 1
    while i >= 0:
        sculptures_per_platform.append(sculptures_on_last_platforms[i])
        i -= sculptures_on_last_platforms[i]

    return platforms[-1], total_min_cost, sculptures_per_platform[::-1]

if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_statues = program5A(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_statues:
        print(i)
    
