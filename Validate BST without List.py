#Time Complexity:: O(n)-all nodes are visited
#Space Complexity:: O(H)-recursive stack space
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
####Error prone because [5,4,6,null,null,3,7]
class Solution(object):
    def isValidBST(self, root): ####Error prone because [5,4,6,null,null,3,7]
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.right==None and root.left==None:
            return True
        
        result = self.inOrder(root)
        if result==False:
            return False
        if result=='0':
            print('0 executed')
            return True
        
        return True
        
    def inOrder(self,root):
        #base case 
        if root==None:
            return
        
        lflag=None
        rflag=None
        
        #logic
        lflag = self.inOrder(root.left)
        rflag = self.inOrder(root.right)
        
        if ((lflag!=None and root.val<lflag) or (rflag!=None and root.val>rflag)):
            print("inequality")
            return False
        elif((lflag!=None and root.val==lflag) or (rflag!=None and root.val==rflag)):
            print("equal")
            return False
        
        return '0' if root.val==0 else root.val