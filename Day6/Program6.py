# Function that returns true if string s can be 
# made up of by other two string from the array 
# after concatenating one after another 
def canbuildword(s, isoriginalword, mp): 
  
    # If current string has been processed before 
    if s in mp and mp[s] == 0: 
        return False
  
    # If current string is found in the map and 
    # it is not the string under consideration 
    if s in mp and mp[s] == 1 and isoriginalword == 0: 
        return True
  
    for i in range(1, len(s)): 
  
        # Split the string into two 
        # contiguous sub-strings 
        left = s[:i] 
        right = s[i:] 
  
        # If left sub-string is found in the map and 
        # the right sub-string can be made from 
        # the strings from the given array 
        if left in mp and mp[left] == 1 and canbuildword(right, 0, mp): 
            return True
  
    # If everything failed, we return false 
    mp[s] = 0
    return False
  
# Function to return the longest string 
# that can made be made up from the 
# other string of the given array 
def printlongestword(listofwords): 
  
    # Put all the strings in the map 
    mp = dict() 
    for i in listofwords: 
        mp[i] = 1
  
    # Sort the string in decreasing 
    # order of their lengths 
    listofwords.sort(key=lambda x: len(x), reverse=True) 
  
    # Starting from the longest string 
    for i in listofwords: 
  
        # If current string can be made 
        # up from other strings 
        if canbuildword(i, 1, mp): 
            return i 
  
    return "-1"
  
# Driver code 
if __name__ == "__main__": 
    listofwords = ["geeks", "for", "geeksfor", 
                "geeksforgeeks"] 
  
    print(printlongestword(listofwords)) 
