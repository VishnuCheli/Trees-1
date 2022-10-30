#Time Complexity:: O(n)-all nodes are visited
#Space Complexity:: Recursive Stack is used-O(H)+O(n)-a list is used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def isValidBST(self, root): 
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.result = [] #result array to store all the elements
        self.inOrder(root) 
        for i in range(1,len(self.result)): #starting the node comparison with i-1 nodes
            if self.result[i-1]<self.result[i]:
                pass
            else:
                return False #only if the adjacent nodes aren't ascending 
        return True

    def inOrder(self, root):
        #base case
        if root == None: #return if null node is detected
            return

        #logic action
        self.inOrder(root.left) #traversing all left branches

        self.result.append(root.val) #appending current nodes value to the result when returning

        self.inOrder(root.right) #traversing all right branches
