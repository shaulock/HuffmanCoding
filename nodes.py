from __future__ import annotations

class Node:
    
    def __init__(self) -> None:
        self.__type = type(self)
        self.next = None
        self.prev = None
    
    @property
    def type(self):
        return self.__type
    
    @property
    def next(self) -> Node | tuple[Node, Node] | type(None):
        return self.__next
    
    @next.setter
    def next(self, next: Node | type(None)) -> None:

        if not isinstance(self, Node):
            raise ValueError # Change this
        
        if not isinstance(next, (Node, type(None))):
            raise ValueError # Change this

        self.__next = next
    
    @property
    def prev(self) -> Node | type(None):
        return self.__prev
    
    @prev.setter
    def prev(self, prev: Node | type(None)):
        if not isinstance(prev, (Node, type(None))):
            raise ValueError # change this
        if self.type == RootNode and not prev == None:
            raise ValueError # change this too
        self.__prev = prev

    def __add__(self: StringNode | JunctionNode, other: StringNode | JunctionNode) -> JunctionNode:
        if not isinstance(other, (StringNode, JunctionNode)) or not isinstance(self, (StringNode, JunctionNode)):
            raise ValueError # Change this
        new_junction = JunctionNode(children=(self,other), strength=(self.strength + other.strength))
        self.prev = new_junction
        other.prev = new_junction
        return new_junction
    
    def __radd__(self : StringNode | JunctionNode, other: StringNode | JunctionNode) -> JunctionNode:
        if not isinstance(other, (StringNode, JunctionNode)) or not isinstance(self, (StringNode, JunctionNode)):
            raise ValueError # Change this
        new_junction = JunctionNode(children=(self,other), strength=(self.strength + other.strength))
        self.prev = new_junction
        other.prev = new_junction
        return new_junction

class RootNode(Node):
    
    def __init__(self) -> None:
        super().__init__()
    
    def __repr__(self) -> str:
        return " Root Node "

    def __str__(self) -> str:
        return " Root Node "

class StringNode(Node):
    
    def __init__(self, value: str, strength: int) -> None:
        super().__init__()
        if not isinstance(value, str):
            raise ValueError # Change this
        if not isinstance(strength, int):
            raise ValueError # Change this
        if not value:
            raise ValueError
        if strength < 1:
            raise ValueError # Change this
        self.__value = value
        self.__strength = strength

    @property
    def value(self) -> str:
        return self.__value
    
    @property
    def strength(self):
        return self.__strength
    
    def __str__(self) -> str:
        return f' String Node ( value : {self.value} , strength : {self.strength} ) '
    
    def __repr__(self) -> str:
        return f' String Node ( value : {self.value} , strength : {self.strength} ) '

class JunctionNode(Node):
    
    def __init__(self, children: tuple[StringNode | JunctionNode, StringNode | JunctionNode], strength: int) -> None:
        super().__init__()
        if not isinstance(children, tuple):
            raise ValueError
        if not len(children) == 2:
            raise ValueError
        if not children[0].type in [StringNode, JunctionNode] or not children[1].type in [StringNode, JunctionNode]:
            raise ValueError
        if not isinstance(strength, int):
            raise ValueError
        if strength < 1:
            raise ValueError
        self.__strength = strength
        self.__children = children
        
    @property
    def children(self):
        return self.__children

    @property
    def strength(self):
        return self.__strength

    def __str__(self) -> str:
        return f' Junction Node ( children : {self.children} , strength : {self.strength} ) '
    
    def __repr__(self) -> str:
        return f' Junction Node ( children : {self.children} , strength : {self.strength} ) '