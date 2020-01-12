def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Reconstruct integers for l1
          #Reconstruct integers for l1
        
        powersoften = 1
        sumtotalone = 0
        while l1:
            sumtotalone = sumtotalone + l1.val * powersoften
            powersoften = powersoften * 10
            l1 = l1.next
        sumtotaltwo = 0
        powersoften = 1
        while l2:
            sumtotaltwo = sumtotaltwo + l2.val * powersoften
            powersoften = powersoften * 10
            l2 = l2.next
            
        total = list(str(sumtotalone  + sumtotaltwo))
        total = total[::-1]
        total = [int(i) for i in total]
        print(total)
        Head = ListNode(total[0])
        cursor = Head
        for x in range(1,len(total)):
            newNode = ListNode(total[x])
            cursor.next = newNode
            cursor = cursor.next
            
        return Head
