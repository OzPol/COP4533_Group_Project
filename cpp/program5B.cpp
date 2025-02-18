#include <iostream>
#include <vector>
#include <tuple>
/* Solution to program 5B
* @param n the number of sculptures
* @param W the maximum width of the platform
* @param heights the heights of the sculptures
* @param widths the widths of the sculptures
* @return a tuple containing the number of platforms used, the optimal total height, and the number of statues on each platform
*/
std::tuple<int, int, std::vector<int>> program5B(int n, int W, std::vector<int> heights, std::vector<int> widths){
    /************************
    * ADD YOUR CODE HERE *
    ***********************/
//    return std::make_tuple(0, 0, std::vector<int>()); // replace with your own result.
    return std::make_tuple(n, 0, heights);
}
int main(){
    int n, W;
    std::cin >> n >> W;
    std::vector<int> heights(n);
    std::vector<int> widths(n);
    for(int i = 0; i < n; i++){
        std::cin >> heights[i];
    }
    for(int i = 0; i < n; i++){
        std::cin >> widths[i];
    }
    auto result = program5B(n, W, heights, widths);

    std::cout << std::get<0>(result) << std::endl;
    std::cout << std::get<1>(result) << std::endl;
    for(int i = 0; i < std::get<0>(result); i++){
        std::cout << std::get<2>(result)[i] << std::endl;
    }
    return 0; 
}