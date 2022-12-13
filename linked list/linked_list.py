"""
linked list implementation
"""


class Node:
    def __init__(self, data=None, next_item=None):
        self.data = data
        self.next_item = next_item


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)  # point head to the next item
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        # reach at the end
        while itr.next_item:
            itr = itr.next_item
        itr.next_item = Node(data, None)

    def insert_values(self, data_list):
        self.head = None  # a fresh linkedlist
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next_item
        return count

    def remove_at(self, index):
        # remove at a particular index
        if index < 0 or index >= self.get_length():
            raise Exception("Index is out of range")
        if index == 0:
            self.head = self.head.next_item
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # need to get the pointer of previous value
                itr.next_item = itr.next_item.next_item  # remove the index item
                break
            itr = itr.next_item
            count += 1

    def insert_at(self, index, data):
        # insert at a particular index
        if index < 0 or index >= self.get_length():
            raise Exception("Index is out of range")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next_item)
                itr.next_item = node
                break
            itr = itr.next_item
            count += 1


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        linked_list = ''
        while itr:
            linked_list += str(itr.data) + '-->'
            itr = itr.next_item
        print(linked_list)


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(3)
    # ll.insert_at_beginning(2)
    # ll.insert_at_beginning(1)
    # ll.insert_at_end(10)
    # ll.insert_at_end(11)
    # ll.insert_at_beginning(5)
    ll.insert_values([1, 2, 3, 4, 5])
    # ll.print()
    # ll.remove_at(3)
    ll.print()
    ll.insert_at(3, 11)
    ll.print()
    print(f'length of the linked list is {ll.get_length()}')


