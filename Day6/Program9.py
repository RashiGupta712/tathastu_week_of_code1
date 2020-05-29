def findElement(arr, n):  
   
    # leftMax[i] stores maximum of arr[0..i-1]  
    leftMax = [None] * n  
    leftMax[0] = float('-inf')  
  
    # Fill leftMax[]1..n-1]  
    for i in range(1, n):  
        leftMax[i] = max(leftMax[i-1], arr[i-1])  
  
    # Initialize minimum from right  
    rightMin = float('inf')  
  
    # Traverse array from right  
    for i in range(n-1, -1, -1):  
       
        # Check if we found a required element  
        if leftMax[i] < arr[i] and rightMin > arr[i]:  
            return i  
  
        # Update right minimum  
        rightMin = min(rightMin, arr[i])  
       
    # If there was no element matching criteria  
    return -1 
  
# Driver program  
if __name__ == "__main__":  
  
    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]  
    n = len(arr)  
    print("Index of the element is", findElement(arr, n)) 
   
