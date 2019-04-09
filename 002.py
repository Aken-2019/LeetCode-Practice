
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def getVal(myl):
            if myl.next is not None:
                val = myl.val + 10*getVal(myl.next)
                return val
            else:
                return myl.val

        l1val = getVal(l1)
        l2val = getVal(l2)
        ansVal = l1val+l2val
        print(ansVal)
        
        def getNext(ansVal):
            if ansVal//10 !=0:
                tmpL = ListNode(ansVal%10)
                tmpL.next = getNext(ansVal//10)
                return tmpL
            else:
                tmpL = ListNode(ansVal%10)
                tmpL.next = None
                return tmpL
        
        return getNext(ansVal)


if __name__ == '__main__':

    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next=ListNode(3)

    l2 = ListNode(1)
    l2.next = ListNode(2)
    l2.next.next=ListNode(3)

    solu = Solution()
    solu_ans = solu.addTwoNumbers(l1, l2)
    print(solu_ans.val, solu_ans.next.val, solu_ans.next.next.val)

'''
Runtime: 84 ms, faster than 90.88% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.5 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.
'''


