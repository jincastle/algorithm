# 링크드 리스트(Linked List) 아직 20%정도만 이해한듯

- 연결 리스트라고도 함
- 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조
- 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 구조

링크드 리스트 기본 구조와 용어

- 노드(node) : 데이터 저장 단위(데이터값, 포인터)로 구성
- 포인터(pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

```python
class Node:
	def __init__(self, data, next=None):
		self.data=data
		self.next=None

node1 = Node(1)
node2 = Node(2)
node1.next=node2
head = node1 # 가장 앞부분
```

데이터 추가하기

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
# 데이터를 추가하는 함수
def add(data):
    node = head
    while node.next: # 마지막 노드를 찾는 방법
        node = node.next
    node.next = Node(data) # 마지막 노드에 연결
# 데이터 추가
node1 = Node(1)
head = node1
for index in range(2, 10):
    add(index)

# 데이터 출력
node = head
while node.next:
    print(node.data)
    node = node.next
print (node.data)
```

## 링크드 리스트의 장단점(예시 C언어)

장점

- 미리 데이터 공간을 미리 할당하지 않아도 됨
  - 배열은 미리 데이터 공간이 할당해야함

단점

- 연결을 위한 별도 데이터 공간이 필요하므로 저장공간 효율이 높지 않음
- 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느리다
  - 이유는 앞에 링크를 타고 타고 들어가야하기 때문에
- 중간 데이터 삭제시 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업이 필요

### 복잡한 기능1(링크드 리스트 데이터 사이에 데이터를 추가)

```python
node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next
node.next = node3 # 1번째 값 next는 node3이 됨
node3.next = node_next # node3의 다음은 원래 1번째 다음값으로 연결

# 출력

node = head
while node.next:
    print(node.data)
    node = node.next
print (node.data)
```

### 객체지향으로 링크드 리스트 구현하기

```python
class Node:
# 링크드 리스트 기본 구조
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data) # head값을 저장

    def add(self, data):
        if self.head == '': # 앞에 값이 없다면
            self.head = Node(data) # head 데이터 추가
        else:
            node = self.head # 값이 있으면 node는 머리
            while node.next: # 마지막 값을 찾는 while문
                node = node.next
            node.next = Node(data) # 마지막 값에 추가

    def desc(self):  # 데이터 출력 함수
        node = self.head
        while node:
            print (node.data)
            node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()

```

### 링크드 리스트의 복잡한 기능2(특정노드 삭제)

```python
# 위에 코드 가져와서
class Node:
# 링크드 리스트 기본 구조
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data) # head값을 저장

    def add(self, data):
        if self.head == '': # 앞에 값이 없다면
            self.head = Node(data) # head 데이터 추가
        else:
            node = self.head # 값이 있으면 node는 머리
            while node.next: # 마지막 값을 찾는 while문
                node = node.next
            node.next = Node(data) # 마지막 값에 추가

    def desc(self):  # 데이터 출력 함수
        node = self.head
        while node:
            print (node.data)
            node = node.next

		# 삭제 함수 추가
		def delete(self, data):
			if self.head =="":
				print("값이 없어")
				return

			if self.head.data == data:
				temp = self.head
				self.head=self.head.next
				del temp
			else:
				node = self.head
				while node.next:
					if node.next.data == data:
						temp = node.next
						node.next = node.next.next
						del temp

# 0값을 head 추가
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
# 삭제
linkedlist1.delete(0)
# 확인
linkedlist1.head

# 0부터 10 추가
for data in range(0, 10):
    linkedlist1.add(data)
linkedlist1.desc()
# 삭제
linkedlist1.delete(4)
# 확인
linkedlist1.desc()

```

### 다양한 링크드 리스트 구조

- 더블 링크드 리스트 기본구조
  - 이중 연결 리스트라고 함
  - 장점 양방향으로 연결되어 있어서 양쪽 노드 탐색이 가능

아직 이해 못함

```python
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev # 앞쪽 값
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next
```
