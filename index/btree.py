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
        path=[]
        node=self.root
        while not node.is_leaf:
            i=0
            while i<len(node.key) and node.key[i]<key:
                i+=1
            if i<=len(node.key):
                i-=1
            path.append(node)
            node=node.children[i]
        return  node ,path
    #insert the value in leaf node
    def insert_value_in_leaf(self,node,value,key):
        i=0
        while i<len(node.key) and node.key[i]<key:
            i+=1
        #if item key is equal so we are updating the value
        if i<len(node.key) and node.key[i]==key:
            print(f'updated: {node.value[i]} ---> {value}')
            node.key[i]=key
            node.value[i]=value
            return 
        node.key.insert(i,key)
        node.value.insert(i,value)
    #inserting functoin 
    def insert(self,value,key):
        node,path=self.find_leaf(key)
        self.insert_value_in_leaf(node,value,key)
        if len(node.key)>self.max_leaf:
            node,new_node=self.split(node)
            new_node_parent_key=new_node.key[0]
            node_parent_key=node.key[0]
            temp_path=path
            if path!=[]:
                while temp_path:
                    last_parent=temp_path.pop()
            else:
                self.root=Node()
                self.root.key.append(node_parent_key)
                self.root.key.append(new_node_parent_key)
                self.root.children.append(node)
                self.root.children.append(new_node)
            print(new_node.key)
            print(new_node.value)
            print(self.root.key)
            print(self.root.children)
        print(node.key)
        print(node.value)
        print(f"path:{path}")
    #function for spliting parent node
    def split_node(self,node):
        mid_key=len(node.key)//2
        new_node=Node()
        new_node.key=node.key[mid_key::]
        new_node.children=node.children[mid_key+1::]
        node.key=node.key[:mid_key]
        node.children=node.children[:mid_key+1]
        return node,new_node
    #function for spliting leaf node
    def split_leaf_node(self,node):
        mid_key=len(node.key)//2
        new_node=Node(True)
        new_node.key=node.key[mid_key::]
        new_node.value=node.value[mid_key::]
        node.key=node.key[:mid_key]
        node.value=node.value[:mid_key]
        new_node.next=node.next
        node.next=new_node
        return node,new_node
    #function which check what node have to split
    def split(self,root):
        if root.is_leaf:
            node,new_node=self.split_leaf_node(root)
            print(node.key,new_node.key)
            return node,new_node
        node,new_node=self.split_node(root)
        print(node.key,new_node.key)
        return node,new_node
storage=btree()
storage.insert('astitva',5)
storage.insert('arya',15)
storage.insert('mummy',25)
storage.insert('dady',35)
storage.insert('mudit',5)
storage.insert('gojo',45)
storage.insert('falak',99)
storage.insert('sukuna',20)