
import sys
import os
import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import List, Tuple

# --- Import Programs Dynamically ---
# Adjust the path to include the folder where 'program1.py', 'program2.py', etc., are located
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
python_folder_path = os.path.join(script_dir, "../python")

# Add 'python' folder to sys.path
if python_folder_path not in sys.path:
    sys.path.insert(0, python_folder_path)

try:
    from program1 import program1
    from program2 import program2
    # from program3 import program3
    from program4 import program4
    from program5A import program5A
    from program5B import program5B

    print("Modules imported successfully.")
except ModuleNotFoundError as e:
    print(f"Error: {e}. Check if the files exist and the path is correct.")

# --- Data Generation Functions ---
def generate_random(n: int, max_height: int, max_width: int) -> Tuple[List[int], List[int]]:
    heights = [random.randint(1, max_height) for _ in range(n)]
    widths = [random.randint(1, max_width) for _ in range(n)]
    return heights, widths

def generate_monotonic_decreasing(n: int, max_height: int, max_width: int) -> Tuple[List[int], List[int]]:
    heights = sorted([random.randint(1, max_height) for _ in range(n)], reverse=True)
    widths = [random.randint(1, max_width) for _ in range(n)]
    return heights, widths

def generate_unimodal(n: int, max_height: int, max_width: int) -> Tuple[List[int], List[int]]:
    peak_index = random.randint(1, n - 2)
    decreasing_part = sorted([random.randint(1, max_height) for _ in range(peak_index)], reverse=True)
    increasing_part = sorted([random.randint(1, max_height) for _ in range(n - peak_index)])
    heights = decreasing_part + increasing_part
    widths = [random.randint(1, max_width) for _ in range(n)]
    return heights, widths

# --- Timing Function ---
def time_algorithm(algorithm, n, W, heights, widths):
    start_time = time.time()
    algorithm(n, W, heights, widths)
    return time.time() - start_time

# --- Parameters for Experiment ---
test_sizes = [1000, 2000, 3000, 4000, 5000]
max_height, max_width = 1000, 100
platform_width = 100

# --- Collect Results ---
results = []
for size in test_sizes:
    # Generate datasets
    random_heights, random_widths = generate_random(size, max_height, max_width)
    monotonic_heights, monotonic_widths = generate_monotonic_decreasing(size, max_height, max_width)
    unimodal_heights, unimodal_widths = generate_unimodal(size, max_height, max_width)
    
    # Test each program and record runtimes
    for program, label in zip(
        # [program1, program2, program3, program4, program5A, program5B],
        # ['Program1', 'Program2', 'Program3', 'Program4', 'Program5A', 'Program5B'],
        [program1, program2, program4, program5A, program5B],
        ['Program1', 'Program2', 'Program4', 'Program5A', 'Program5B']
    ):
        if label == 'Program1':
            runtime = time_algorithm(program, size, platform_width, random_heights, random_widths)
        elif label == 'Program2':
            runtime = time_algorithm(program, size, platform_width, monotonic_heights, monotonic_widths)
        else:
            runtime = time_algorithm(program, size, platform_width, unimodal_heights, unimodal_widths)
        results.append([label, size, runtime])

# Convert results to DataFrame for plotting
results_df = pd.DataFrame(results, columns=['Program', 'Input Size', 'Runtime'])

# --- Plotting ---
# Plot individual runtimes
for program in results_df['Program'].unique():
    subset = results_df[results_df['Program'] == program]
    plt.figure(figsize=(10, 6))
    plt.plot(subset['Input Size'], subset['Runtime'], marker='o', label=program)
    plt.xlabel('Input Size')
    plt.ylabel('Runtime (seconds)')
    plt.title(f'Runtime of {program}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{program}_runtime.png')
    plt.show()

# Combined Plot (Plot7)
plt.figure(figsize=(12, 8))
for program in results_df['Program'].unique():
    subset = results_df[results_df['Program'] == program]
    plt.plot(subset['Input Size'], subset['Runtime'], marker='o', label=program)
plt.xlabel('Input Size')
plt.ylabel('Runtime (seconds)')
plt.title('Combined Runtime Comparison (Programs 1-5B)')
plt.legend()
plt.grid(True)
plt.savefig('Combined_Runtime_Comparison.png')
plt.show()
