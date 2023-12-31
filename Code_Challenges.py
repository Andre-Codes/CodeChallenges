# Merge Strings Alternately
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s

class Solution:
    def mergeAlternately(self, word1, word2):
        merged_words = []
        i = 0
        extra_chars = ""
        if len(word1) != len(word2):
            if len(word1) > len(word2):
                extra_chars = word1[-(len(word1) - len(word2)):]
                common_len = len(word1) - len(extra_chars)
            else:
                extra_chars = word2[-(len(word2) - len(word1)):]
                common_len = len(word2) - len(extra_chars)
        else:
            common_len = len(word1)
        while i < common_len:
            merged_words.append(word1[i])
            merged_words.append(word2[i])
            i += 1
        if len(extra_chars) > 0:
            merged_words.append(extra_chars)

# ____________________________________

# Greatest Common Divisor of Strings
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# ** work in progress

class Solution:
    def gcd_of_strings(self, str1, str2):
        min_len = min(len(str1), len(str2))
        for i in range(min_len + 1):
            if str2[:i+1] == str1[:i+1]:
                match = str2[:i+1]
            if match == str1[len(match):len(match)+len(match)]:
                break
        print(match)


test = Solution()

test.gcd_of_strings("ABABZABAB", "ABABZBBBB")

# ____________________________________

# There are n kids with candies. You are given an integer array candies, 
# where each candies[i] represents the number of candies the ith kid has, 
# and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, 
# after giving the ith kid all the extraCandies, they will have the greatest number of 
# candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.

class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        maxCandy = max(candies)
        result = []
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxCandy)
        return result


test = Solution()
candy_list = [3, 5, 6, 5, 2]
test.kidsWithCandies(candy_list, 3)

# ____________________________________

# Can Place Flowers
# Can n number of 1s be planted where there are no adjacent 1s next to it

class Solution:
    def canPlaceFlowers(self, flowerbed, n: int):
        if sum(flowerbed[:2]) == 0:
            n -= 1
            flowerbed[0] = 1
        if sum(flowerbed[-2:]) == 0:
            n -= 1
            flowerbed[-1] = 1
        for i in range(1, (len(flowerbed)-1), 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0

test = Solution()
answer = test.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2)
print(answer)

# ____________________________________

# Challenge: Middle Slice
# Given a list nums of integers, write a function to return a new list containing 
# only the middle elements. If the length of the list is even, return the two middle elements.
# Examples:
# nums = [1, 2, 3, 4, 5]
## print(middle_slice(nums))  # Output: [3]

# nums = [1, 2, 3, 4, 5, 6]
## print(middle_slice(nums))  # Output: [3, 4]

def middle_slice(nums):
    mid = nums[(len(nums)//2)] if len(nums) % 2 == 1 else nums[(len(nums)//2)-1:(len(nums)//2)+1]
    return mid

# The code directly accesses the middle element(s) using indexing and slicing operations, which are efficient operations.
# The code uses a small amount of memory by not creating any additional data structures 
# or allocating memory beyond the input list and the result.

# ____________________________________

# Challenge: Given a list of strings, in a single line of code, reutrn the list reversed as a single string

strings = ['elb', 'isn', 'ehe', 'rpm', 'ocn', 'i']

''.join([i[::-1] for i in strings[::-1]]) # Result: 'incomprehensible'

# ____________________________________

# Challenge: Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# Examples:
    # summer_69([1, 3, 5]) --> 9
    # summer_69([4, 5, 6, 7, 8, 9]) --> 9
    # summer_69([2, 1, 6, 9, 11]) --> 14

# Solution 1
def summer_69(arr):
    if 6 in arr:
        del arr[arr.index(6):(arr.index(9))+1]
    return sum(arr)

# Solution 2 (less memory)
def summer_69(arr):
    if 6 in arr:
        return sum(list(filter(lambda n:arr.index(n) < arr.index(6) or arr.index(n) > arr.index(9), arr)))
    return sum(arr)

# ____________________________________
