# 꼭 알아뒤야 할 자료 구조: 스택(Stack)
# 제한적으로 접근할 수 있는 구조
# 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조
# Queue : FIFO 정책
# Stack : LIFO 정책

data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)
data_stack.pop()
print(data_stack)

stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

print(pop())

