# Time: O(N^2·logN)
# Space: O(1)
"""
Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose
three edges length is the three numbers that we find?

Example 1:
Input: [3, 4, 6, 7]
Output: 3
Explanation:
They are (3, 4, 6),
         (3, 6, 7),
         (4, 6, 7)

Example 2:
Input: [4, 4, 4, 4]
Output: 4
Explanation:
Any three numbers can form a triangle.
So the answer is C(3, 4) = 4

给定一个整数数组，在该数组中，寻找三个数，分别代表三角形三条边的长度，问，可以寻找到多少组这样的三个数来组成三角形？

样例 1:
输入: [3, 4, 6, 7]
输出: 3
解释:
可以组成的是 (3, 4, 6),
           (3, 6, 7),
           (4, 6, 7)

样例 2:
输入: [4, 4, 4, 4]
输出: 4
解释:
任何三个数都可以构成三角形
所以答案为 C(3, 4) = 4
"""


class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    # 思路: 双指针

    def triangleCount(self, S):
        # write your code here
        S.sort()
        result = 0

        for i in range(2, len(S)):
            left, right = 0, i - 1

            while left < right:
                if S[left] + S[right] > S[i]:
                    result += right - left
                    right -= 1
                else:
                    left += 1

        return result


if __name__ == "__main__":
    result = Solution().triangleCount([4, 4, 4, 4])
    print(result)