# Iterative Binary Search Function
# It returns index of searchItem in a given list searchList if present,
# else returns -1
def binarySearch(searchList, searchItem):
    start = 0
    end = len(searchList) - 1 #find length of list (-1 because index starts at 0 not 1)
 
    #iterate through the list
    while start <= end:
        
        #find the midpoint of the list
        midPoint = (end + start) // 2
 
        #if searchItem is greater than the item at this position then searchItem is in second half
        if searchList[midPoint] < searchItem:
            start = midPoint + 1
 
        #if searchItem is smaller than the item at this position then searchItem is in first half
        elif searchList[midPoint] > searchItem:
            end = midPoint - 1
 
        #means searchItem is present at midPoint
        else:
            return midPoint
 
    #If we reach here then the item was not found in the list
    return -1
 
 
#test data
searchList = [ 2, 5, 9, 12, 15, 19, 32 ]
searchItem = 5
 
#Call binary search function
result = binarySearch(searchList, searchItem)
 
if result != -1:
    print("Item found at index", str(result))
else:
    print("Item not present in the list")

