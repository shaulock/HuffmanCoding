from nodes import RootNode, StringNode, JunctionNode
from exception_handler import NonIntegerQueueSizeException, NegativeQueueSizeException
from exception_handler import QueueIndexOutOfRangeException, QueueIndexExpectedIntException
from exception_handler import QueueItemExpectedStringJunctionNodeException, EmptyQueueException

# This class represents a queue, which is the parent class to a priority queue
class Queue:
    
    # The initializer
    def __init__(self) -> None:
        # Set the initial size of the queue, which is 0 (without counting root)
        self.size: int = 0
        # Set the head of the queue as a rootnode
        self.__head: RootNode = RootNode()
    
    # The property to access the size of the queue
    @property
    def size(self) -> int:
        return self.__size

    # The setter for the size property of the queue
    @size.setter
    def size(self, size: int) -> None:

        # If the new size is not integer raise proper error
        if not isinstance(size, int):
            raise NonIntegerQueueSizeException(f"""
Function Call : {self}.size = {size}.
Provided Value {size} is not an integer.
""") # Change this
        
        # If the new size is less than 0 raise proper error
        if size < 0:
            raise NegativeQueueSizeException(f"""
Function Call : {self}.size = {size}.
Provided Value {size} should not be negative as a queue with negative size does not make sense.
""") # Change this
        
        # If all is correct set the size to new size
        self.__size = size

    # This function will implement the built-in len() function and 
    # return the size of the queue
    # Return type -> int
    def __len__(self) -> int:
        return self.size

    # The property to access the head of the queue
    @property
    def head(self) -> RootNode:
        return self.__head

    # This generator will allow users to loop on the queue like a normal Iterable
    # Return type -> StringNode or JunctionNone or NoneType
    def __iter__(self) -> StringNode | JunctionNode | None:
        
        # If the length the queue is 0, return
        if len(self) == 0:
            return None

        # Set the pointer initially to the next node to the head
        pointer = self.head.next
        # Loop until the pointer is not None
        while pointer:
            # Yield the pointer and wait for next call to the function
            yield pointer
            # When the function is next called, update pointer to the next pointer
            pointer = pointer.next
    
    # This function will implement the [] notation to access the elements in the queue
    # Return type -> StringNode or JunctionNode
    def __getitem__(self, key: int) -> StringNode | JunctionNode:
        
        # if the key provided is not an integer, raise proper exception
        if not isinstance(key, int):
            raise QueueIndexExpectedIntException(f"""
Function Call : {self}[{key}]
Provided Value {key = } is not an integer.
""")

        # We dont allow negative indexing for the queue to reduce confusion
        # So when the index is out of bounds we raise proper error
        if key < 0 or key >= self.size:
            raise QueueIndexOutOfRangeException(f"""
Function Call : {self}[{key}]
Provided Value {key = } is not within the range of available values.
""")
        
        # if the key was valid, we loop over the queue
        # (this is where __iter__() comes in handy)
        for index, value in enumerate(self):
            # If the index matches the key
            if index == key:
                return value # Return the value

    # This function implements [] notation to change elements in the queue
    # Return type -> None
    def __setitem__(self, key: int, value: StringNode | JunctionNode) -> None:
        
        # If the value is not StringNode or JunctioNode, raise proper error
        if not isinstance(value, (StringNode, JunctionNode)):
            raise QueueItemExpectedStringJunctionNodeException(f"""
Function Call : {self}[{key}] = {value}
Provided value {value} should be a String Node or a Junction Node.
""")

        # if the value was valid, change the value at key given
        self[key] = value
    
    # This function will properly delete an element at the given key in the queue 
    # implementing the [] notation
    # Return type -> None
    def __delitem__(self, key: int) -> None:
        # First get the element at the key
        item = self[key]

        # if the item was the last element in the queue
        if item.next is None:
            # set the penultimate element's next to None
            item.prev.next = None
        # If the item wasn't the last element
        else:
            # Get the element next to the item
            next_node = item.next
            # Get the element prev to the item
            previous_node = item.prev
            # 'Stitch' the next and previous element together
            previous_node.next = next_node
            next_node.prev = previous_node
        
        # Reduce the size of the queue by 1
        self.size -= 1

    # This function will enqueue an item to the back of the queue
    # Return type -> None
    def enqueue(self, item: StringNode | JunctionNode) -> None:
        
        # if the item is not a StringNode or JunctionNode, raise proper error
        if not isinstance(item, (StringNode, JunctionNode)):
            raise QueueItemExpectedStringJunctionNodeException(f"""
Function Call : {self}.enqueue({item = })
Provided value {item = } should be a String Node or Junction Node.
""")
        
        # if the queue is empty, set it to be the next element to the head
        if self.size == 0:
            self.head.next = item
            item.prev = self.head
        # else get the last element using the [] notation and 
        # set the next of that to be the item and items previous to be the last element
        else:
            self[len(self) - 1].next = item
            item.prev = self[len(self) - 1]
        # increase the size by 1 after adding the element
        self.size += 1

    # This function will dequeue the first element in the queue
    # Return type -> StringNode or JunctionNode
    def dequeue(self) -> StringNode | JunctionNode:
        
        # If the queue is empty raise proper error
        if self.size == 0:
            raise EmptyQueueException(f"""
Function Call : {self}.dequeue()
Queue object {self} is empty, dequeue not possible.
""")
        
        # else get the first element of the queue and delete its record from the queue
        # using the [] notation
        to_return = self[0]
        del self[0]

        # Return the extracted element
        return to_return

    # This function will convert queue to a str
    # Return type -> str
    def __str__(self) -> str:
        
        # If the queue is empty return empty message
        if self.size == 0:
            return ' Queue is Empty '
        
        # Else, we start at root
        string = 'root'
        
        # and add other elements with the arrow notation
        for i in self:
            string += f' -> {str(i)}'
        
        # return the string formed
        return string

# This class represents a priority queue where
# the lowest strength elements are present first
class Priority_Queue(Queue):
    
    # The initializer
    def __init__(self) -> None:
        super().__init__() # Initializing the parent class

    # Overriding the enqueue function in the super class to arrange the data priority wise
    # Return type -> None
    def enqueue(self, item: StringNode | JunctionNode) -> None:
        
        # If item is not a string node or junction node, raise proper error
        if not isinstance(item, (StringNode, JunctionNode)):
            raise QueueItemExpectedStringJunctionNodeException(f"""
Function Call : {self}.enqueue({item = })
Provided value {item = } should be a String Node or Junction Node.
""")

        # if the queue is empty, call the function in the parent class
        if len(self) == 0:
            super().enqueue(item)
        # else we proceed with our logic
        else:
            # Loop over the elements of the queue
            for i in self:
                # Setting the type of the element, for ease of use
                i: StringNode | JunctionNode
                # if the strength of the current element is more than the strength
                # of the item to be added we add the item before this element
                if i.strength > item.strength:
                    item.prev = i.prev
                    i.prev = item
                    item.next = i
                    item.prev.next = item
                    # and break the loop
                    break
            # if the for loop never encountered a break
            # it means the item to be added is the 'strongest' so we add it at the back
            else:
                i.next = item
                item.prev = i
            # And then we increase the size of the queue by 1
            self.size += 1