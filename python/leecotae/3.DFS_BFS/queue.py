# 리스트 자료형 이용할 수 있지만 시간복잡도가 더 효율적인 deque 이용 
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.popleft()
queue.append(3)
queue.popleft()
print(queue) # deque([3])

###

stack = deque()

stack.append(1)
stack.append(2)
stack.pop()
print(stack)  # deque([1])

