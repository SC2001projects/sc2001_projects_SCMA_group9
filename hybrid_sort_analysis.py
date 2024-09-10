import random
import matplotlib.pyplot as plt

# Define the threshold for switching to Insertion Sort
S = 5
num_cmp = 0

def generate_random_array(n, max_value):
    """Function to generate a random array"""
    return [random.randint(0, max_value) for _ in range(n)]

def insertion_sort(arr, left, right):
    """Function to perform Insertion Sort"""
    global num_cmp
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left:
            num_cmp += 1
            if key >= arr[j]:
                break
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return num_cmp

def merge(arr, left, mid, right):
    """Function to merge two sorted halves"""
    global num_cmp
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        num_cmp += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def hybrid_merge_sort(arr, left, right):
    """Function to implement the hybrid Merge-Insertion Sort"""
    if right - left + 1 <= S:
        return insertion_sort(arr, left, right)
    else:
        mid = left + (right - left) // 2
        hybrid_merge_sort(arr, left, mid)
        hybrid_merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Function to run the hybrid algorithm for increasing array sizes
def run_experiment_fixed_S():
    global num_cmp
    sizes = [1000, 10000, 100000, 1000000, 10000000]
    comparisons = []
    for n in sizes:
        arr = generate_random_array(n, 1000000)
        num_cmp = 0
        hybrid_merge_sort(arr, 0, len(arr) - 1)
        comparisons.append(num_cmp)
    return sizes, comparisons

# Function to run the hybrid algorithm for different S values with fixed n
def run_experiment_fixed_n(n=10000):
    global num_cmp
    S_values = range(2, 50, 2)
    comparisons = []
    for s in S_values:
        arr = generate_random_array(n, 1000000)
        num_cmp = 0
        hybrid_merge_sort(arr, 0, len(arr) - 1)
        comparisons.append(num_cmp)
    return S_values, comparisons

# Plot for (i) comparisons vs. n (with fixed S)
def plot_comparisons_vs_n():
    sizes, comparisons = run_experiment_fixed_S()
    plt.figure()
    plt.plot(sizes, comparisons, marker='o')
    plt.title("Comparisons vs. Input Size n (S fixed)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Number of Comparisons")
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

# Plot for (ii) comparisons vs. S (with fixed n)
def plot_comparisons_vs_S():
    S_values, comparisons = run_experiment_fixed_n()
    plt.figure()
    plt.plot(S_values, comparisons, marker='o')
    plt.title("Comparisons vs. Threshold S (n fixed)")
    plt.xlabel("Threshold S")
    plt.ylabel("Number of Comparisons")
    plt.show()

# Run the plots
plot_comparisons_vs_n()
plot_comparisons_vs_S()
