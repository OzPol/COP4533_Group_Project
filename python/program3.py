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
    ############################
    # Add you code here
    ############################

    return 0, 0, [] # replace with your code


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_statues = program3(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_statues:
        print(i)
    