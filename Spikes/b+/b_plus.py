#bb+ practice 
class Error(Exception):
    pass
class Node:
    def __init__(self):
        self.keys=[]
        self.children=[]
        self.is_leaf=False
        self.next=None

root=Node()
root.keys=[30]
child1=Node()
child1.is_leaf=True
child2=Node()
child2.is_leaf=True
child1.keys=[10,20]
child2.keys=[30,40]
child1.next=child2
root.children=[child1,child2]
def display(node):
    print("Keys:", node.keys)

    if not node.is_leaf:
        for child in node.children:
            display(child)
display(root)
def travel(node,value):
    while not node.is_leaf:
        i=0
        while i<len(node.keys) and value>=node.keys[i]: 
            i+=1
        node=node.children[i]
    i=0
    while i<len(node.keys) and  node.keys[i]!=value:
        i+=1
    if i>=len(node.keys):
        raise Error('your value is not present in the b+ tree ') 
    return node.keys[i]
print(travel(root,30))
print(travel(root,40))
# print(travel(root,50))


#now we create a tree in which we can store value in leaf_node
class Node_leaf:
    def __init__(self,is_leaf:bool=False):
        self.keys=[]
        self.childern=[]
        self.value=[]
        self.is_leaf=is_leaf
        self.next=None
        self.parent=None

max_node=4

root=Node_leaf()
root.keys=[30]
child1=Node_leaf(is_leaf=True)
child1.is_leaf=True
child2=Node_leaf(is_leaf=True)
child2.is_leaf=True
child1.keys=[10,20]
child2.keys=[30,40]
child1.value=['astitva','arya']
child2.value=['udit','om']
child1.next=child2
root.children=[child1,child2]
child1.parent=root
child2.parent=root

def split_node(node):
    new_node=Node_leaf()
    new_node.parent=node.parent
    node.next=new_node
    old_node_length_key=len(node.value)
    old_node_length_value=len(node.keys)

    mid_value=old_node_length_value//2
    mid_keys=old_node_length_key//2

    new_node.value=node.value[mid_value::]
    new_node.keys=node.keys[mid_keys::]

    node.value=node.value[:mid_value]
    node.keys=node.keys[:mid_keys]


    return node,new_node

def insert(node,value,key_value):
    while not node.is_leaf:
        i=0
        while i<len(node.keys) and key_value>=node.keys[i]: 
            i+=1
        node=node.children[i]
    i=0
    while i<len(node.keys) and  node.keys[i]<key_value:
        i+=1
    node.keys.insert(i,key_value)
    node.value.insert(i,value)
    print(node.keys,node.value)
    if len( node.value )>max_node:
        node1,node2=split_node(node)
        print(node1.value,node1.keys)
        print(node2.value,node2.keys)
        new_parent_key=node2.keys[0]
        parent=node1.parent
        j=0
        while parent.keys<new_parent_key:
            j+=1
            
        return 
    return node.keys[i],node.value[i]
insert(root,'falak',25)
insert(root,'joker',5)
insert(root,'mummy',45)
insert(root,'daddy',35)
insert(root,'sukuna',55)