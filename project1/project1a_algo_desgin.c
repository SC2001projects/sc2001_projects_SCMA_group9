#include <stdio.h>

#define S 5  // Threshold for switching to Insertion Sort

void printArray(int arr[], int size);
void hybridMergeSort(int arr[], int left, int right);
void insertionSort(int arr[], int left, int right);
void merge(int arr[], int left, int mid, int right);

int main() {
    int arr[] = {7, 11, 17, 5, 2, 7, 1, 4, 55, 15, 2};
    int size = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: \n");
    printArray(arr, size);

    hybridMergeSort(arr, 0, size - 1);

    printf("Sorted array: \n");
    printArray(arr, size);

    return 0;
}

// Function to perform Insertion Sort (1)
void insertionSort(int arr[], int left, int right) {
    for (int i = left + 1; i <= right; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Function to merge two sorted halves (2)
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];  // Temporary arrays

    // Copy data to temp arrays L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Merge the temp arrays back into arr[l..r]
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], if any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], if any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Function to implement the hybrid Merge-Insertion Sort (3)
void hybridMergeSort(int arr[], int left, int right) {
    if (right - left + 1 <= S) {
        // If subarray size is less than or equal to S, use Insertion Sort
        insertionSort(arr, left, right);
    } else {
        // Otherwise, use Merge Sort
            int mid = left + (right - left) / 2;

            // Recursively sort the two halves
            hybridMergeSort(arr, left, mid);
            hybridMergeSort(arr, mid + 1, right);

            // Merge the sorted halves
            merge(arr, left, mid, right);
        
    }
}

// Function to print the array (4)
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}


