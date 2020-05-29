import sys 
  
# Function to find a maximum  
# product of a triplet in array 
# of integers of size n 
def maxProduct(arr, n): 
  
    # if size is less than 3, 
    # no triplet exists 
    if n < 3: 
        return -1
  
    # will contain max product 
    max_product = -(sys.maxsize - 1) 
      
    for i in range(0, n - 2): 
        for j in range(i + 1, n - 1): 
            for k in range(j + 1, n): 
                max_product = max( 
                    max_product, arr[i] 
                    * arr[j] * arr[k]) 
  
    return max_product 
  
# Driver Program 
arr = [10, 3, 5, 6, 20] 
n = len(arr) 
  
max = maxProduct(arr, n) 
  
if max == -1: 
    print("No Tripplet Exits") 
else: 
    print("Maximum product is", max) 
