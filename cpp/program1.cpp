#include <iostream>
#include <vector>
#include <tuple>
#include <cstdlib>  
using namespace std;
/* Solution to program 1
* @param n the number of sculptures
* @param W the maximum width of the platform
* @param heights the heights of the sculptures
* @param widths the widths of the sculptures
* @return a tuple containing the number of platforms used, the optimal total height, and the number of statues on each platform
*/
std::tuple<int, int, std::vector<int>> program1(int n, int W, std::vector<int> heights, std::vector<int> widths){

    // Input validation: Make sure non-negative values
    if (n < 0 || W < 0) {
        std::cerr << "Error: The number of sculptures and platform width must be non-negative." << std::endl;
        exit(1);
    }

    // Input consistency check: Number of heights and widths must match the number of sculptures
    if (heights.size() != n || widths.size() != n) {
        std::cerr << "Error: The number of heights and widths must match the number of sculptures." << std::endl;
        exit(1);
    }

    // Check for non-negative heights and widths
    for (int h : heights) {
        if (h < 0) {
            std::cerr << "Error: Heights must be non-negative." << std::endl;
            exit(1);
        }
    }
    for (int w : widths) {
        if (w < 0) {
            std::cerr << "Error: Widths must be non-negative." << std::endl;
            exit(1);
        }
    }

    // Check for monotonically non-increasing heights
    for (int i = 0; i < n - 1; ++i) {
        if (heights[i] < heights[i + 1]) {
            std::cerr << "Error: Heights must be in non-increasing order for ProblemS1." << std::endl;
            exit(1);
        }
    }

    vector<int> sculptures_per_platform;  // Stores the number of sculptures on each platform
    int total_height = 0;                 // Stores the total height of all platforms
    int current_width = 0;                // Tracks the current width used on the platform
    int current_max_height = 0;           // Tracks the tallest sculpture on the current platform
    int platforms_used = 0;               // Tracks the total number of platforms used
    int sculptures_on_current_platform = 0;  // Counts the sculptures on the current platform

    // Traverse each sculpture and try to place it on a platform
    for (int i = 0; i < n; ++i) {
        if (current_width + widths[i] <= W) {
            // If adding the sculpture doesn't exceed the width limit
            current_width += widths[i];  // Add the sculpture's width to the current platform
            current_max_height = max(current_max_height, heights[i]);  // Update the max height
            sculptures_on_current_platform++;  // Increment the sculpture counter
        }
        else {
            // If the width limit is exceeded, finalize the current platform
            sculptures_per_platform.push_back(sculptures_on_current_platform);  // Store the count
            total_height += current_max_height;  // Add the max height of this platform to the total
            platforms_used++;  // Increment the platform counter

            // Start a new platform with the current sculpture
            current_width = widths[i];  // Reset the width for the new platform
            current_max_height = heights[i];  // Set the new platform's max height
            sculptures_on_current_platform = 1;  // Reset the sculpture counter to 1
        }
    }

    // Finalize the last platform after the loop ends
    sculptures_per_platform.push_back(sculptures_on_current_platform);  // Store the last platform count
    total_height += current_max_height;  // Add the last platform's height to the total
    platforms_used++;  // Increment the platform counter for the last platform


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