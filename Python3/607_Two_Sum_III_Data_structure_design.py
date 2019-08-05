# Time: O(N)
# Space: O(N)
"""
Design and implement a TwoSum class. It should support the following operations: add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:
add(1); add(3); add(5);
find(4) // return true
find(7) // return false

设计b并实现一个 TwoSum 类。他需要支持以下操作:add 和 find。
add -把这个数添加到内部的数据结构。
find -是否存在任意一对数字之和等于这个值

样例 1:
add(1);add(3);add(5);
find(4)//返回true
find(7)//返回false
"""


class TwoSum:

    # 思路: 字典存储
    # Time: O(N)
    # Space: O(N)

    def __init__(self):
        self.counts = {}

    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.counts[number] = self.counts.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.counts:
            if value - num in self.counts:
                #增加判断，当value是2的倍数时，会出现误判：[2, 3] 4，而[2,2 ,3]则没有问题
                if num != value - num or self.counts[num] > 1:
                    return True
        return False


class TwoSum2:

    # 思路: 列表存储
    # Time: O(N)
    # Space: O(N)

    def __init__(self):
        self.nums = []

    """
    @param: number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.nums.append(number)

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        _hash = {}
        for i in self.nums:
            if value - i in _hash:
                return True
            _hash[i] = i
        return False



if __name__ == "__main__":
    a = TwoSum()
    a.add(1)
    a.add(3)
    a.add(50)
    result = [a.find(4), a.find(7)]
    print(result)

    b = TwoSum2()
    b.add(1)
    b.add(3)
    b.add(5)
    result2 = [b.find(4), b.find(7)]
    print(result2)