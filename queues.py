from nodes import RootNode, StringNode, JunctionNode
class Queue:
    
    def __init__(self) -> None:
        self.size = 0
        self.__head = RootNode()
    
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        if not isinstance(size, int):
            raise ValueError
        if size < 0:
            raise ValueError
        self.__size = size

    @property
    def head(self) -> RootNode:
        return self.__head

    def __iter__(self) -> StringNode | JunctionNode:
        if len(self) == 0:
            return
        pointer = self.head.next
        while pointer:
            yield pointer
            pointer = pointer.next
    
    def __len__(self) -> int:
        return self.size

    def enqueue(self, item: StringNode | JunctionNode) -> None:
        if not isinstance(item, (StringNode, JunctionNode)):
            raise ValueError # Change this
        if self.size == 0:
            self.head.next = item
            item.prev = self.head
            self.size = 1
            return
        self[len(self) - 1].next = item
        item.prev = self[len(self) - 1]
        self.size += 1

    def __getitem__(self, key: int) -> StringNode | JunctionNode:
        if key < 0 or key >= self.size:
            raise ValueError
        count = 0
        for i in self:
            if count == key:
                return i
            count += 1

    def __setitem__(self, key: int, value: StringNode | JunctionNode) -> None:
        self[key].strength = value
    
    def __delitem__(self, key: int) -> None:
        item = self[key]
        if item.next == None:
            item.prev.next = None
            self.size -= 1
        else: 
            next_node = item.next
            previous_node = item.prev
            previous_node.next = next_node
            next_node.prev = previous_node
            self.size -= 1

    def dequeue(self) -> StringNode | JunctionNode:
        if self.size == 0:
            raise ValueError
        to_return = self[0]
        del self[0]
        return to_return


    def __str__(self) -> str:
        if self.size == 0:
            return ' Queue is Empty '
        string = 'root '
        for i in self:
            string += f' -> {i} '
        return string

class Priority_Queue(Queue):
    
    def __init__(self) -> None:
        super().__init__()

    def enqueue(self, item: StringNode | JunctionNode) -> None:
        queue_len = len(self)
        if queue_len == 0:
            super().enqueue(item)
        else:
            for i in self:
                if i.strength > item.strength:
                    item.prev = i.prev
                    i.prev = item
                    item.next = i
                    item.prev.next = item
                    self.size += 1
                    break
            else:
                i.next = item
                item.prev = i
                self.size += 1