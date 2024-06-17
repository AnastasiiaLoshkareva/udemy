#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(nums):
  if nums[0] > nums[-1]:
    change_val = nums[0]
    #use list comprehension
    filled_list = [change_val for _ in nums]
  else:
    change_val = nums[-1]
    #use list comprehension
    filled_list = [change_val for _ in nums]
  return filled_list
