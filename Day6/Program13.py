def segregate0and1(arr, size): 
  
    type0 = 0
    type1 = size - 1
      
    while(type0 < type1): 
        if(arr[type0] == 1): 
            (arr[type0],  
             arr[type1]) = (arr[type1], 
                            arr[type0]) 
            type1 -= 1
        else: 
            type0 += 1
      
# Driver Code 
arr = [0, 1, 0, 1, 1, 1] 
arr_size = len(arr) 
segregate0and1(arr, arr_size) 
print("Array after segregation is",  
                         end = " ") 
for i in range(0, arr_size): 
        print(arr[i], end = " ") 
