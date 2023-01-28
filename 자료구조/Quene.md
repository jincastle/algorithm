# 큐(Quene)

### 큐의 구조

> - 가장 먼저 넣은 데이터를 가장 먼저 꺼낼수 있는 구조

- 줄을 서는 행위와 유사
- FIFO(First-In, First-Out) 또는 LILO(Last-In, Last-Out) 방식으로 스택과 꺼내는 순서가 반대
  >

FIFO = 첫번째로 들어간애가 첫번째로 나간다.
LILO = 마지막에 들어간애가 가장 먼저 나온다

용어

- Enqueue: 큐에 데이터를 넣는 기능
- Dequeue: 큐에서 데이터를 꺼내는 기능

• Visualgo 사이트에서 시연해보며 이해하기 (enqueue/dequeue 만 클릭해보며): [https://visualgo.net/en/list](https://visualgo.net/en/list)

### 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기

- **queue 라이브러리에는 다양한 큐 구조로 Queue(), LifoQueue(), PriorityQueue() 제공**
- 프로그램을 작성할 때 프로그램에 따라 적합한 자료 구조 사용
  - Queue() : 가장 일반적인 큐 자료 구조
  - LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조(스택 구조라고 보면 됨)
  - PriorityQueue(): 데이터마다 우선 순위를 넣어서, 우선순위가 높은 순으로 데이터 출력
- 일반적인 큐 외에 다양한 정책이 적용된 큐들이 있음

큐는 어디에 많이 사용할까?

- • 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨 (운영체제 참조)
  - 큐의 경우에는 장단점 보다는 (특별히 언급되는 장단점이 없음), 큐의 활용 예로 프로세스 스케쥴링 방식을 함께 이해해두는 것이 좋음

```python
import queue

# 큐를 만들고 FIFO
data_queue = queue.Queue()

# 값을 넣고
data_queue.put("funcoding")
data_queue.put(1)

# 개수 확인
data_queue.qsize()

# "funcoding" 가 나옴
data_queue.get()
```

```python
# 큐만들기 LIFO : 늦게 들어간 값이 가장 먼저 나온다
import queue
data_queue = queue.LifoQueue()

# 값을 넣고
data_queue.put("funcoding")
data_queue.put(1)

# 1이 나옴
data_queue.get()
```

```python
import queue

# 우선순위랑 같이 저장 시킴
data_queue = queue.PriorityQueue()

# 값을 넣고 값은 튜플 형태
data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

# 우선수위가 가장빠른 5가 나온다
data_queue.get()
# 그다음은 10번이 나옴
data_queue.get()
```

프로그래밍에서 사용하는 큐

```python
queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

# 1부터 10까지 넣고
for index in range(10):
    enqueue(index)

# 값을 가지고 나온 함수 실행 0이 나옴
dequeue()
```
