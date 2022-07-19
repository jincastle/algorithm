class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        total = []
        a = 0
        b = 0
        while a < len(list1) and b < len(list2):
            if list1[a] < list2[b]: 
                total.append(list1[a])
                a+=1
            else:
                total.append(list2[b])
                b+=1
                
        return total + list1[a:] + list2[b:]

## 한줄로 해결 list(merge(list1,list2)) 대신 from heapq import merge 선언을 해줘야한다
## sorted(list1 + list2) 이렇게도 된다