class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data} {self.next}'


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.length = 1 if node else 0

    def insert_beginning(self, data=None):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert_end(self, data=None):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = new_node
        self.length += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr.next:
            if itr.data == data_after:
                break
            itr = itr.next
        if not itr or itr.data != data_after:
            raise Exception('Data cannot be found')
        else:
            new_node = Node(data_to_insert)
            if not itr.next:
                itr.next = new_node
            else:
                new_node.next = itr.next
                itr.next = new_node
            self.length += 1

    def get_length(self):
        return self.length

    def print_list(self):
        if self.head is None:
            print('head => none')
        else:
            tmp = self.head
            list_str = 'head => '
            while tmp:
                list_str += str(tmp.data) + ' => '
                tmp = tmp.next
            list_str += 'None'
            print(list_str)

    def insert_values(self, values=None):
        for item in values:
            self.insert_end(item)

    def remove_at(self, index):
        if index >= self.length or index < 0:
            print('index out  of renge.')
            return
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            itr = self.head
            while index-1 > 0:
                itr = itr.next
                index -= 1
            itr.next = itr.next.next
            self.length -= 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_beginning(225)
    ll.insert_beginning(3325)
    ll.insert_beginning(44425)
    values = ['banana', 'apple', 'mango', 'jackfruit', 'lichi', 'coconut']
    ll.insert_values(values)
    ll.print_list()
    print(ll.get_length())

    # testing new methods
    ll.insert_after_value('applsde', 2652)
    ll.print_list()
    print(ll.get_length())