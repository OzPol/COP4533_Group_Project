from typing import List, Tuple

    
def program5B(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5B
    
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

    min_cost = [float('inf')] * n # DP array to track the minimum cumulative height cost up to each sculpture added  
    platforms = [0] * n  # To track the number of platforms used to get each minimum height cost in min_cost
    sculptures_on_last_platforms = [0] * n  # To track the number of sculptures placed on the *last* platform used to reach each min_cost
   
    # precompute cumulative widths up to each sculpture
    # we have one extra element (0) to simplify the calculations of subarray widths and keep consistency across all cases
    cumulative_width = [0] * (n + 1)
    for i in range(1, n+1):
        cumulative_width[i] = cumulative_width[i-1] + widths[i-1] 

    for i in range(n): 
        # loops through every sculpture, starting at position 0
        # i represents the last sculpture on the current platform
        # base case: First sculpture is on a single platform with height equal to its height
        platform_max_height = 0

        for j in range(i, -1, -1):
            # j represents the first sculpture on the current platform that ends at positon i
            # here we explore all different possible subarrays in this range 
            # and determine which one of them produces the minimum height cost
            platform_max_height = max(platform_max_height, heights[j])
                
            if cumulative_width[i+1] - cumulative_width[j] <= W:
                if j == 0: 
                    if min_cost[i] > platform_max_height:
                        min_cost[i] = platform_max_height
                        platforms[i] = 1
                        sculptures_on_last_platforms[i] = i + 1
                else:
                    if min_cost[i] > min_cost[j-1] + platform_max_height:
                        min_cost[i] = min_cost[j-1] + platform_max_height
                        platforms[i] = platforms[j-1] + 1
                        sculptures_on_last_platforms[i] = i - j + 1 

    # retrieve the number of sculptures per platform based on sculptures_on_last_platform
    # return the reversed array to keep the order of platforms

    sculptures_per_platform = []
    i = n - 1
    while i >= 0:
        sculptures_per_platform.append(sculptures_on_last_platforms[i])
        i -= sculptures_on_last_platforms[i]

    return platforms[-1], min_cost[-1], sculptures_per_platform[::-1]

if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_statues = program5B(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_statues:
        print(i)
    
