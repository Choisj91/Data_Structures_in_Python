class Heap:
    def __init__(self, data):
        self.heap_array = list()         #자료 구조를 배열로 가지고 감
        self.heap_array.append(None)    #맨처음 데이터를 None으로 설정해서 1부터 인덱스 시작하게 하기
        self.heap_array.append(data)

heap = Heap(1)
print(heap.heap_array)

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)
        
    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)  #리스트의 맨끝에 데이터를 추가하는 것이 append인데, append로 하면 정확한 이진 트리 구조를 따름
        return True  

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

print(heap.heap_array)


