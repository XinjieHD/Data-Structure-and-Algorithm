def binary_search(arr, target):
    # Define initial left and right pointers for the binary search
    left, right = 0, len(arr) - 1
    
    # Perform binary search until the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2
        
        # If the middle element is the target, return its index
        if arr[mid] == target:
            return mid
        # If the target is greater, move the left pointer to mid + 1
        elif arr[mid] < target:
            left = mid + 1
        # If the target is smaller, move the right pointer to mid - 1
        else:
            right = mid - 1
    
    # Return -1 if the target is not found in the array
    return -1

# Main block
if __name__ == '__main__':
    # Input the array elements as space-separated integers
    arr = [int(x) for x in input().split()]
    
    # Input the target value to search for
    target = int(input())
    
    # Call the binary_search function with the array and target
    res = binary_search(arr, target)
    
    # Print the result (index of the target in the array or -1 if not found)
    print(res)

