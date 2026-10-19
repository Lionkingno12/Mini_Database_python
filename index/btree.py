#b+ tree
class Error(Exception):
    pass
class Node:
    def __init__(self,is_leaf:bool=False):
        self.key=[]
        self.is_leaf=is_leaf
        if is_leaf:
            self.value=[]
            self.next=None
        else:
            self.children=[]
class btree:
    def __init__(self,max_leaf:int=4):
        self.max_leaf=max_leaf
        self.root=Node(True)
    def find_leaf(self,key):
        node=self.root
        while not node.is_leaf:
            i=0
            while node.key[i]<key:
                i+=1
            node=node.children[i]
        return  node 
    def insert_value_in_leaf(self,node,value,key):
        i=0
        while i<len(node.key) and node.key[i]<key:
            i+=1
        if i<len(node.key) and node.key[i]==key:
            print(f'updated: {node.value[i]} ---> {value}')
            node.key[i]=key
            node.value[i]=value
            return 
        node.key.insert(i,key)
        node.value.insert(i,value)
    def insert(self,value,key):
        node=self.find_leaf(key)
        self.insert_value_in_leaf(node,value,key)
        print(node.key)
        print(node.value)
    def split_node(self,)
storage=btree()
storage.insert('astitva',5)
storage.insert('arya',15)
storage.insert('mummy',25)
storage.insert('dady',35)
storage.insert('mudit',5)