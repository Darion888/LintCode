# Time: O(V+E)
# Space: O(V)
"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

Example 1:
Input: {1,2,3,4}
Output: [1->null,2->3->null,4->null]
Explanation:
        1
       / \
      2   3
     /
    4

Example 2:
Input: {1,#,2,3}
Output: [1->null,2->null,3->null]
Explanation:
    1
     \
      2
     /
    3

给一棵二叉树，设计一个算法为每一层的节点建立一个链表。也就是说，如果一棵二叉树有 D 层，那么你需要创建 D 条链表。

样例 1:
输入: {1,2,3,4}
输出: [1->null,2->3->null,4->null]
解释:
        1
       / \
      2   3
     /
    4

样例 2:
输入: {1,#,2,3}
输出: [1->null,2->null,3->null]
解释:
    1
     \
      2
     /
    3
"""
#import this


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        result = []
        if root is None:
            return result
        queue = [root]
        while len(queue) > 0:
            cur_len = len(queue)
            firstNode = None
            currentNode = None
            for i in range(cur_len):
                treeNode = queue.pop(0)
                # print(treeNode.val)
                listNode = ListNode(treeNode.val)
                if firstNode:
                    currentNode.next = listNode
                    currentNode = listNode
                else:
                    firstNode = listNode
                    currentNode = listNode
                if treeNode.left:
                    queue.append(treeNode.left)
                if treeNode.right:
                    queue.append(treeNode.right)
            result.append(firstNode)
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    result = Solution().binaryTreeToLists(root)
    print(["{0}".format(result[0].val), "{0} -> {1}".format(result[1].val, result[1].next.val), "{0}".format(result[2].val)])