from __future__ import annotations
from exception_handler import NextNodeExpectedStringOrJunctionNodeOrNoneException, PreviousNodeExpectedQueueNodeOrNoneException
from exception_handler import RootNodePreviousExpectedNoneException, AttemptedRootNodeAdditionException
from exception_handler import OperandExpectedStringOrJunctionNode, NodeValueEmptyException
from exception_handler import NodeValueExpectedStringException
from exception_handler import NodeStrengthExpectedIntException, NodeStrengthExpectedGreaterThan1Exception
from exception_handler import NodeChildrenExpectedTupleException, NodeChildrenStructureException

# This is the parent class to all nodes
class Node:

    # Initialiser
    def __init__(self) -> None:
        # To store the type of the node stored
        self.__type = type(self)
        
    # The type property for easy access and so
    # no one can set the type we have no setter for it
    @property
    def type(self):
        # Returning the type of node
        return self.__type

# This class is the parent class to all nodes that will be part of the queue
class QueueNode(Node):

    # Initializer
    def __init__(self) -> None:
        super().__init__() # Initializing the parent class variables
        # To store the next node to the current node
        self.next = None
        # To store the previous node to the current node
        self.prev = None
    
    # The next property to access the next node connected to this node
    @property
    def next(self) -> StringNode | JunctionNode | None:
        return self.__next
    
    # The setter for the next property so we can modify it later
    @next.setter
    def next(self, new_next: StringNode | JunctionNode | None) -> None:
        
        # if the next node to be set is not None, StringNode or JunctionNode
        # raise proper error
        if not isinstance(new_next, (StringNode, JunctionNode)) and new_next is not None:
            raise NextNodeExpectedStringOrJunctionNodeOrNoneException(f"""
Function Call : {self}.next = {new_next}
Provided value {new_next} should be a string node or a junction node or None.
""")

        # if all checks out, set the next node to the next variable
        self.__next = new_next
    
    # The previous property to access the previous node connected to this node
    @property
    def prev(self) -> QueueNode | None:
        return self.__prev
    
    # The setter for the previous property so we can modify it later 
    @prev.setter
    def prev(self, new_prev: QueueNode | None) -> None:
        
        # If the previous node to be set is not a QueueNode or a subclass of it
        # Or if it's not None, raise appropriate error
        if not isinstance(new_prev, QueueNode) and new_prev is not None:
            raise PreviousNodeExpectedQueueNodeOrNoneException(f"""
Function Call : {self}.prev = {new_prev}
Provided value {new_prev} should be a queue node or None.
""")

        # if the node object calling this function is the RootNode
        # And we are assigning it's previous as anything other than None
        # Raise approriate error
        if self.type == RootNode and new_prev is not None:
            raise RootNodePreviousExpectedNoneException(f"""
Function Call : {self}.prev = {new_prev}
Provided value {new_prev} should be None for a RootNode.
""")

        # if all checks out, set previous property to be the previous variable
        self.__prev = new_prev

    # This function will implement the '+' operator between two QueueNode objects
    # that are not RootNodes and return a JunctionNode whose children are the nodes provided
    # Return type -> JunctionNode
    def __add__(self: StringNode | JunctionNode, 
                other: StringNode | JunctionNode) -> JunctionNode:
        
        # if self or other node is a RootNode, raise proper error
        if isinstance(self, RootNode) or isinstance(other, RootNode):
            raise AttemptedRootNodeAdditionException(f"""
Function Call : {self} + {other}
One of the operands is a RootNode, and RootNode addition is not allowed.
""")

        # if other not an instance of QueueNode class, raise proper error
        if not isinstance(other, QueueNode):
            raise OperandExpectedStringOrJunctionNode(f"""
Function Call : {self} + {other}
Provided operand {other} should be a StringNode or JunctionNode. 
""")
        
        # Create a new junction node whose children are self and other
        # and strength is the total strength of self and other
        new_junction = JunctionNode(children=(self, other), 
                                    strength=(self.strength + other.strength))
        
        # Setting previous nodes of self and other to None
        self.prev = None
        other.prev = None
        
        # returning the new junction node
        return new_junction

    # Making a reverse addition function just to make adding comutative
    def __radd__(self: StringNode | JunctionNode, other: StringNode | JunctionNode) -> JunctionNode:
        return self + other

# This class represents root node of the queue
class RootNode(QueueNode):
    
    # the initializer
    def __init__(self) -> None:
        super().__init__() # initializing the parent class
    
    # This function will create a string representation of the object
    # Return type -> str
    def __repr__(self) -> str:
        return "Root Node"

    # This function will convert the object to string
    # Return type -> str
    def __str__(self) -> str:
        return self.__repr__()

# This class represents a node that contains a string and it's strength
# for the priority queue
class StringNode(QueueNode):
    
    # The Initializer
    def __init__(self, value: str, strength: int) -> None:
        super().__init__() # Initializing the parent class

        # if the value to be set is not a string, raise proper error
        if not isinstance(value, str):
            raise NodeValueExpectedStringException(f"""
Function Call : StringNode({value = }, {strength = })
Provided Value {value = } is not a string.
""")
        
        # if the value to be set is empty, raise proper error
        if not value:
            raise NodeValueEmptyException(f"""
Function Call : StringNode({value = }, {strength = })
Provided Value {value = } is empty.
""")

        # if the strength to be set is not an integer, raise proper error
        if not isinstance(strength, int):
            raise NodeStrengthExpectedIntException(f"""
Function Call : StringNode({value = }, {strength = })
Provided Value {strength = } is not an integer.
""")
        
        # if the strength is less than 0, raise proper error
        if strength < 1:
            raise NodeStrengthExpectedGreaterThan1Exception(f"""
Function Call : StringNode({value = }, {strength = })
Provided Value {strength = } is less than 1.
""")
        
        # if everything is correct, initialize the object with the value and strength provided
        self.__value = value
        self.__strength = strength

    # The property to access the value attribute of the object
    @property
    def value(self) -> str:
        return self.__value
    
    # The property to access the strength attribute of the object
    @property
    def strength(self) -> int:
        return self.__strength
    
    # This function will create a string representation of the object
    # Return type -> str
    def __repr__(self) -> str:
        return 'String Node'

    # This function will convert the object to string
    # Return type -> str
    def __str__(self) -> str:
        return self.__repr__() + f' ( value : {self.value} , strength : {self.strength} )'

# This class represents a node that forms the junction between 2 nodes
# that contains children and their total strength, for the priority queue
class JunctionNode(QueueNode):
    
    # The initializer
    def __init__(self, 
                 children: tuple[StringNode | JunctionNode, StringNode | JunctionNode], 
                 strength: int) -> None:
        super().__init__() # Initializing the parent class

        # if the children are not stored in a tuple, raise proper error
        if not isinstance(children, tuple):
            raise NodeChildrenExpectedTupleException(f"""
Function Call : JunctionNode({children = }, {strength = })
Provided value {children = } is not a tuple.
""")

        # If the length of the children is not 2, raise proper error
        if not len(children) == 2:
            raise NodeChildrenStructureException(f"""
Function Call : JunctionNode({children = }, {strength = })
Provided value {children = } is not a tuple of length 2.
""")
        
        # looping in the children
        for i in children:
            # if the current child is not a StringNode or a JunctionNode, raise proper error
            if not isinstance(i, (StringNode, JunctionNode)):
                raise NodeChildrenStructureException(f"""
Function Call : JunctionNode({children = }, {strength = })
Provided value {children = } has an element {i} which is not a String Node or a Junction Node.
""")
        
        # if the strength is not integer, raise proper error
        if not isinstance(strength, int):
            raise NodeStrengthExpectedIntException(f"""
Function Call : JunctionNode({children = }, {strength = })
Provided value {strength = } is not an integer.
""")
        
        # if the strength is less than 1, raise proper error
        if strength < 1:
            raise NodeStrengthExpectedGreaterThan1Exception(f"""
Function Call : JunctionNode({children = }, {strength = })
Provided value {strength = } is less than 1.
""")
        
        # if everything is perfect set the values to strength and children attributes
        self.__strength = strength
        self.__children = children
    
    # The property to access the children of the junction node
    @property
    def children(self) -> tuple[StringNode | JunctionNode, StringNode | JunctionNode]:
        return self.__children

    # The property to access the strength of the junction node
    @property
    def strength(self) -> int:
        return self.__strength

    # This function will create a string representation of the object
    # Return type -> str
    def __repr__(self) -> str:
        return 'Junction Node'

    # This function will convert the object to string
    # Return type -> str
    def __str__(self) -> str:
        return self.__repr__() + f' ( children : {self.children} , strength : {self.strength} )'

# This class represents a TreeNode
# that is a connection between two other Nodes (Leaf or Tree)
# It is like JunctionNode, except it does not have the properties are not useful in a Tree
# so converting to a TreeNode from JunctionNode will save space when dealing with a Tree
class TreeNode(Node):

    # The initializer
    def __init__(self) -> None:
        super().__init__() # Initializing the parent class

        # If the type of self is StrictNode
        # we don't need to initialize a children variable for this class
        if not self.type == StrictTreeNode:
            self.__children = [None]*2 # But if it is TreeNode, we initialize it to [None, None]

    # The property to access the children of the TreeNode
    @property
    def children(self) -> list[None | LeafNode | TreeNode, None | LeafNode | TreeNode]:
        return self.__children

    # This function will create a string representation of the object
    # Return type -> str
    def __repr__(self):
        return 'Tree Node'

    # This function will convert the object to string
    # Return type -> str
    def __str__(self) -> str:
        return self.__repr__() + f' ( children : {self.children} )'
    
    
# This class represents a Strict Tree Node that
# Restricts the children attribute to be assigned as particular type only
class StrictTreeNode(TreeNode):

    # The initializer
    def __init__(self, children: tuple[StrictTreeNode | LeafNode, StrictTreeNode | LeafNode]) -> None:
        super().__init__() # Initializing the parent class

        # Similar checking for the children atribute as JunctionNode
        # However this time we are checking for StrictTreeNode and LeafNode as potential children
        if not isinstance(children, tuple):
            raise NodeChildrenExpectedTupleException(f"""
Function Call : StrictTreeNode({children = })
Provided value {children = } is not a tuple.
""")
        if not len(children) == 2:
            raise NodeChildrenStructureException(f"""
Function Call : StrictTreeNode({children = })
Provided value {children = } is not a tuple of length 2.
""")
        for i in children:
            if not isinstance(i, (StrictTreeNode, LeafNode)):
                raise NodeChildrenStructureException(f"""
Function Call : StrictTreeNode({children = })
Provided value {children = } has an element {i} which is not a StrictTreeNode or a LeafNode.
""")
        
        # If everything is perfect, initialize the object with the children provided
        self.__children = children
    
    # The property to access the children of the TreeNode
    @property
    def children(self) -> tuple[StrictTreeNode | LeafNode, StrictTreeNode | LeafNode]:
        return self.__children
    
    # This function will create a string representation of the object
    # Return type -> str
    def __repr__(self) -> str:
        return 'Strict Tree Node'

# This class represents the Leaf Node that is the last node of a chain
# It is like StringNode, except it does not have the properties that are not useful in a Tree
# so converting to a LeafNode from StringNode will save space when dealing with a Tree
class LeafNode(Node):

    # The initializer
    def __init__(self, value: str) -> None:
        super().__init__() # Initializing the parent class

        # If the value is not a string raise a proper error
        if not isinstance(value, str):
            raise NodeValueExpectedStringException(f"""
Function Call : LeafNode({value = })
Provided Value {value = } is not a string.
""")
        
        # if the value to be set is empty, raise proper error
        if not value:
            raise NodeValueEmptyException(f"""
Function Call : LeafNode({value = })
Provided Value {value = } is empty.
""")
        
        # If everything is perfect initialize the object with the given value
        self.__value = value
    
    # The property to access the value of the LeafNode
    @property
    def value(self) -> str:
        return self.__value
    
    # This function will create a string representation of the object
    # Return type -> str
    def __repr__(self) -> str:
        return 'Leaf Node'
    
    # This function will convert the object to string
    # Return type -> str
    def __str__(self) -> str:
        return self.__repr__() + f' ( value : {self.value} )' 