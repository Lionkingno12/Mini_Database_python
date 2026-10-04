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
print(travel(root,50))


#now we create a tree in which we can store value in leaf_node
class Node_leaf:
    def __init__(self,is_leaf:bool=False):
        self.keys=[]
        self.childern=[]
        self.value=[]
        self.is_leaf=is_leaf
        self.next=None

root=Node_leaf()
root.keys=[30]
child1=Node()
child1.is_leaf=True
child2=Node()
child2.is_leaf=True
child1.keys=[10,20]
child2.keys=[30,40]
child1.next=child2
root.children=[child1,child2]

def insert(value,key_value):
    while not node.is_leaf:
        i=0
        while i<len(node.keys) and key_value>=node.keys[i]: 
            i+=1
        node=node.children[i]
    i=0
    while i<len(node.keys) and  node.keys[i]!=key_value:
        i+=1
    if i>=len(node.keys):
        raise Error('your value is not present in the b+ tree ') 
    node.keys.insert(i,key_value)
    node.value.insert(i,value)
    return node.keys[i],node.value.insert[i]