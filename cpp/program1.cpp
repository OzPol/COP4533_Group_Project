#include <iostream>
#include <vector>
#include <tuple>
using namespace std;
/* Solution to program 1
* @param n the number of sculptures
* @param W the maximum width of the platform
* @param heights the heights of the sculptures
* @param widths the widths of the sculptures
* @return a tuple containing the number of platforms used, the optimal total height, and the number of statues on each platform
*/
std::tuple<int, int, std::vector<int>> program1(int n, int W, std::vector<int> heights, std::vector<int> widths){
    /************************
    * ADD YOUR CODE HERE *
    ***********************/
    vector<int> sculptures_per_platform;
    int total_height = 0;
    int current_width = 0;
    int current_max_height = 0;
    int platforms_used = 0;
    
    for (int i = 0; i < n; ++i) {
        if (current_width + widths[i] <= W) {
            // Add to the current platform
            current_width += widths[i];
            current_max_height = max(current_max_height, heights[i]);
        } else {
            // Finalize the current platform
            sculptures_per_platform.push_back(i - platforms_used);
            total_height += current_max_height;
            platforms_used++;
            
            // Start a new platform
            current_width = widths[i];
            current_max_height = heights[i];
        }
    }
    
    // Finalize the last platform
    sculptures_per_platform.push_back(n - platforms_used);
    total_height += current_max_height;
    platforms_used++;

    // Return number of platforms, total height, and number of sculptures per platform
    return make_tuple(platforms_used, total_height, sculptures_per_platform);

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
    auto result = program1(n, W, heights, widths);

    std::cout << std::get<0>(result) << std::endl;
    std::cout << std::get<1>(result) << std::endl;
    for(int i = 0; i < std::get<0>(result); i++){
        std::cout << std::get<2>(result)[i] << std::endl;
    }
    return 0; 
}

// The C++ code follows the same logic as the Python version.
// It iterates through the sculptures, adding them to platforms while respecting the width constraint.
// Once the width exceeds the maximum allowed (W), a new platform is started.
// The maximum height for each platform is tracked, and the total height is calculated.
// It outputs the number of platforms, the total height, and the number of sculptures on each platform.

// The time complexity is O(n) because the code iterates through the sculptures once.