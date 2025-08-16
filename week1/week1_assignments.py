#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]

def twoSum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
      need = target - x
      if need in seen:
        return [seen[need], i]
        seen[x] = i
    raise ValueError("There is no nums that sums Target")#your code goes here
    pass

#time complexity: O(n)
#space complexity: O(n)

#Question 2:
#Given some arrays with strings on them, find the most common longest prefix among them.
#Example: ["flower","flow","flight"] output = "fl"

def findMostCommonPrefix(arr):
    if not arr:
        return ""
    pref = arr [0]
    for w in arr[1:]:
        while not w.startswith(pref):
            pref = pref[:-1]
            if not pref:
                return ""
    return pref
    pass

#time complexity: O(n*m)
#space complexity: O(1)

#Question 3:
#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [2, 3, 4]

def threeSum(nums):
    if len(nums) < 3:
        return []
    n = len(nums)
    for i in range(n):
        need = -nums[i]
        seen = {}
        for j in range(i+1, n):
            need2 = need - nums[j]
            if need2 in seen:
                return [nums[i], nums[j], need2]
            seen[nums[j]] = j
    return []
    pass

#time complexity: O(n^2)
#space complexity: O(n)

#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printList(head):
    while head:
        print(head.data)
        head = head.next

head = Node(1)
middle = Node(2)
tail = Node(3)

head.next = middle
middle.next = tail
tail.next = None

printList(head)

def reverseList(head):
    def reverseList(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
    pass

#time complexity: O(n)
#space complexity: O(1)
