# 트리(Tree) 자료구조 중에서 가장 복잡한 것

# Node와 Branch를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None   #None으로 주소값이 없는 상태

class NodeMgmt:
    def __init__(self, head):
        self.head = head      #Root Node를 head라고 지칭해서 직접 Head를 생성
    
    def insert(self, value):
        self.current_node = self.head
        while True:                             #While true로 다시 돌아가서 여기서부터 다시 시작해서 반복!
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:                                          #branch끝에 Node가 없다면 새로운 branch를 만들어서 연결
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

head = Node(1)
BST = NodeMgmt(head)  #Root Node를 강제로 만들어서 여기 넣음 => 이로서 Root Node를 가진 BST데이터 구조 객체!를 만든 것
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)
