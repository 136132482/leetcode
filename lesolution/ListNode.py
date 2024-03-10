# 两数相加
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    # 创建链表数组
    def create_linked_list_array(self,values):
        lists = []
        for value in values:
            current_list = []
            for num in value:
                node = ListNode(num)
                if not current_list:
                    current_list.append(node)
                else:
                    last_node = current_list[-1]
                    last_node.next = node
                    current_list.append(node)
            lists.append(current_list)
        return lists

        # 链表
    def traverse(self, num,node,list):
            for index,linked_list in enumerate(node):
                     curr = linked_list
                     while curr:
                        # print(curr.val, end=" ")
                        #     print(curr.val)
                            if index==0:
                              num.append(curr.val)
                            curr = curr.next
                     if index==0:
                        list.append(num)

    def convert_to_list(slef,head):
        result = []
        node = head
        while node:
            result.append(node.val)
            node = node.next
        return result

    def addTwoNumbers(self, l1, l2):
        arrays=[]
        arrays.append(l1)
        arrays.append(l2)
        linked_list_array = ListNode().create_linked_list_array(arrays)
        list = []
        for index, node in enumerate(linked_list_array):
            num = []
            ListNode().traverse(num, node, list)
        num_list = []
        for num in list:
            my_list = []
            for i in range(len(num)):
                size = num[len(num) - i - 1]
                print(size)
                my_list.append(str(size))
            # my_list =[ str(num) for num in  num[::-1]
            number = int("".join(my_list))
            print(number)
            num_list.append(number)
        total = 0
        for num in num_list:
            total += num
        print(total)
        return total

if __name__ == '__main__':
    # 示例使用
    ListNode().addTwoNumbers([2,4,3],[5,6,4])