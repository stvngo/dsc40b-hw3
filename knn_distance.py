import random

def knn_distance(arr, q, k):

    def quickselect_inplace(arr, left, right, k):
        if left == right:
            return arr[left]
        
        # Partition and get pivot index
        pivot_index = partition(arr, left, right)
        
        # Check where k falls
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect_inplace(arr, left, pivot_index - 1, k)
        else:
            return quickselect_inplace(arr, pivot_index + 1, right, k)


    def partition(arr, left, right):
        # Choose random pivot and move to end
        pivot_index = random.randint(left, right)
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        pivot = arr[right]
        
        # Partition
        i = left
        for j in range(left, right):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        # Move pivot to its final position
        arr[i], arr[right] = arr[right], arr[i]
        return i

    # aim for O(n) time complexity
    distances = []

    for i in range(len(arr)):
        dist = abs(arr[i] - q)
        distances.append((dist, arr[i]))

    result = quickselect_inplace(distances, 0, len(distances) - 1, k - 1) # find the k-th smallest distance

    return (result[0], result[1]) # return the distance and the element

