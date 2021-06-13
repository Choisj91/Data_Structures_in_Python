# 링크드 리스트(Linked List)

# 링크드 리스트(Linked List) 구조
# 연결 리스트. 무한정으로 데이터가 뻗어나갈 수 있음
# 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
