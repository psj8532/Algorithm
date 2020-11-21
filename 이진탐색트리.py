class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None  # 트리의 루트 노드
        self.pre_order_lst = []  # 전위 순회 리스트
        self.post_order_lst = []  # 후위 순회 리스트

    # 루트 노드 설정
    def setRoot(self, data):
        self.root = Node(data)

    # 삽입
    def insert(self, data):
        # 트리의 루트 노드가 존재하는지 아닌지 판단
        if self.root is None:
            self.setRoot(data)  # 루트 노드가 없는 경우(제일 처음에 들어온 데이터가 루트 노드가 됨)
        else:
            self._insert_value(self.root, data)

    def _insert_value(self, cur, data):
        # 부모 노드의 키보다 작으면 좌측, 크면 우측으로 보냄
        if data < cur.data:
            if cur.left:  # 이미 요소가 있다면 삽입 메서드 한번 더
                self._insert_value(cur.left, data)
            else:
                cur.left = Node(data)
        else:
            if cur.right:
                self._insert_value(cur.right, data)
            else:
                cur.right = Node(data)


    # 탐색
    def find(self,data):
        if self._find_node(self.root,data):
            return True
        else:
            return False


    def _find_node(self,cur,data):
        if cur is None:
            return False
        elif data == cur.data:
            return True
        elif data < cur.data:
            return self._find_node(cur.left,data)
        else:
            return self._find_node(cur.right,data)

    # 삭제
    def delete(self,data):
        self._delete_node(self.root,data) # 루트 노드부터 시작하므로 재귀를 시작해야하므로

    def _delete_node(self,cur,data):
        if cur is None:
            return None
        elif data < cur.data:
            cur.left = self._delete_node(cur.left,data) # 왼쪽 자식 노드 정보 제거
            return cur
        elif data > cur.data:
            cur.right = self._delete_node(cur.right,data) # 오른쪽 자식 노드 정보 제거
            return cur
        else: # data == cur.data
            # Node to be removed has no children.
            if cur.left is None and cur.right is None:
                return None
            # Node to be removed has own children.
            elif cur.left is not None and cur.right is None:
                return cur.left
            elif cur.left is None and cur.right is not None:
                return cur.right
            # Node to be removed has two children.
            else:
                # 오른쪽 서브트리에서 가장 작은 값
                min_node = self._successor_node(cur.right)
                cur.data = min_node.data # cur.left 정보는 유지하기 위해 min_node.data만 가져옴
                self._delete_node(cur.right,min_node.data) # cur.right에는 이미 저장하고 있으므로 저장 안해도
                return cur

    # 후계 노드 찾기
    def _successor_node(self,cur):
        while cur.left is not None:
            cur = cur.left
        return cur


    # 전위 순회
    def _pre_order_traverse(self):
        if self.root is not None:  # 루트 노드가 존재한다면 탐색
            self._pre_order(self.root)

    def _pre_order(self, cur):
        self.pre_order_lst.append(cur.data)
        if cur.left is not None:
            self._pre_order(cur.left)
        if cur.right is not None:
            self._pre_order(cur.right)

    # 후위 순회
    def _post_order_traverse(self):
        if self.root is not None:
            self._post_order(self.root)

    def _post_order(self, cur):
        if cur.left is not None:
            self._post_order(cur.left)
        if cur.right is not None:
            self._post_order(cur.right)
        self.post_order_lst.append(cur.data)


arr = [11,10,13,12,15,14,16,17]
bst = BinarySearchTree()
for val in arr:
    bst.insert(val)