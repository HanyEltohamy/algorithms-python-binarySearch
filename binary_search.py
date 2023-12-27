def binary_search(lst, item):
  leftIndex =0 
  rightIndex=len(lst)-1
  while(leftIndex<=rightIndex ):
    midIndex = (leftIndex+rightIndex)// 2
    if(lst[midIndex]>item): 
      # Move right index to the left 
      # Ignore all elemnts to the right 
      rightIndex = midIndex-1 
    elif (lst[midIndex]<item): 
      #move left index to the right 
      # Ignore all eelemnts to the left 
      leftIndex = midIndex+1
    else :
      return midIndex
  return -1

lst = [2,3,5,7,9]
x = 9
result = binary_search(lst, x)
print(result)


# def binary_search(list, item):
#   low = 0
#   high = len(list)-1
#   while low <= high:
#     mid = (low + high)
#     guess = list[mid]
#     if guess == item:
#       return mid
#     if guess > item:
#       high = mid - 1
#     else:
#       low = mid + 1
#   return None

# my_list = [1, 3, 5, 7, 9]
# print (binary_search(my_list, 3)) # => 1
# print (binary_search(my_list, -1)) # => None