# 대표적인 데이터 구조4: 큐 (Queue)

# 큐 구조
# 줄을 서는 행위와 유사
# 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
# 음식점에서 가장 먼저 줄을 선 사람이 제일 먼저 음식점에 입장하는 것과 동일
# FIFO(First-In, First-Out) 또는 LILO(Last-In, Last-Out) 방식으로 스택과 꺼내는 순서가 반대

import queue

data_queue = queue.Queue()
# data_queue = queue.LifoQueue()
# data_queue = queue.PriorityQueue()

data_queue.put("funcoding")
data_queue.put(1)

data_queue.qsize()

print(data_queue.qsize())

queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

len(queue_list)
dequeue()

print(len(queue_list))

