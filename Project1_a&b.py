# Define the threshold for switching to Insertion Sort
S = 5
num_cmp = 0

def print_array(arr):
    """Function to print the array"""
    print(" ".join(map(str, arr)))

def generate_random_array(n, max_value):
    """Function to generate a random array"""
    import random
    return [random.randint(0, max_value) for _ in range(n)]

def insertion_sort(arr, left, right):
    """Function to perform Insertion Sort"""
    global num_cmp
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        while j >= left:
            num_cmp += 1 # num_cmp is incremented here
            if key >= arr[j]:
                 break
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return num_cmp

def merge(arr, left, mid, right):
    """Function to merge two sorted halves"""
    n1 = mid - left + 1
    n2 = right - mid
    global num_cmp

    # Create temporary arrays
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    # Merge the temp arrays back into arr[left..right]
    i = 0
    j = 0
    k = left
    while i < len(L) and j < len(R):
        num_cmp += 1 # num_cmp is incremented here
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def hybrid_merge_sort(arr, left, right):
    """Function to implement the hybrid Merge-Insertion Sort"""
    if right - left + 1 <= S:
        # If subarray size is less than or equal to S, use Insertion Sort
        return insertion_sort(arr, left, right)
    else:
        # Otherwise, use Merge Sort
        mid = left + (right - left) // 2

        # Recursively sort the two halves
        hybrid_merge_sort(arr, left, mid)
        hybrid_merge_sort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, mid, right)

# Main code
if __name__ == "__main__":
    for i in range(1, 6):
        # Generate a random array
        arr = generate_random_array(2**(i), 100)

        # Print the original array
        print("Original array: ")
        print_array(arr)

        # Apply hybrid merge sort
        hybrid_merge_sort(arr, 0, len(arr) - 1)

        # Print the sorted array
        print("Sorted array: ")
        print_array(arr)
        print("Number of comparisons: ", num_cmp)
        num_cmp = 0 
        print (generate_random_array(2**(i), 100))
