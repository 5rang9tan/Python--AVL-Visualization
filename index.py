import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import networkx as nx

# 한글 폰트 설정 (맥OS)
plt.rcParams['font.family'] = 'AppleGothic'  # MacOS에서 한글 지원 폰트

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        # 1. 일반 이진 탐색 트리 삽입
        if not root:
            return Node(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. 조상의 높이 업데이트
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # 3. 균형 인수 계산
        balance = self.getBalance(root)

        # 4. 노드가 불균형해지면, 4가지 경우 처리
        if balance > 1:  # 왼쪽 서브트리가 더 높음
            if key < root.left.value:  # 왼쪽-왼쪽 경우
                print(f"왼쪽-왼쪽 경우가 {root.value}에서 감지되었습니다. 오른쪽 회전을 수행합니다.")
                self.visualize(root, [root.value])  # 회전 전 시각화
                return self.rotateRight(root)
            else:  # 왼쪽-오른쪽 경우
                print(f"왼쪽-오른쪽 경우가 {root.value}에서 감지되었습니다. 왼쪽 자식에서 왼쪽 회전을 수행합니다.")
                self.visualize(root, [root.left.value])  # 왼쪽 자식 회전 전 시각화
                root.left = self.rotateLeft(root.left)
                print(f"{root.value}에서 오른쪽 회전을 수행합니다.")
                self.visualize(root, [root.value])  # 회전 전 시각화
                return self.rotateRight(root)

        if balance < -1:  # 오른쪽 서브트리가 더 높음
            if key > root.right.value:  # 오른쪽-오른쪽 경우
                print(f"오른쪽-오른쪽 경우가 {root.value}에서 감지되었습니다. 왼쪽 회전을 수행합니다.")
                self.visualize(root, [root.value])  # 회전 전 시각화
                return self.rotateLeft(root)
            else:  # 오른쪽-왼쪽 경우
                print(f"오른쪽-왼쪽 경우가 {root.value}에서 감지되었습니다. 오른쪽 자식에서 오른쪽 회전을 수행합니다.")
                self.visualize(root, [root.right.value])  # 오른쪽 자식 회전 전 시각화
                root.right = self.rotateRight(root.right)
                print(f"{root.value}에서 왼쪽 회전을 수행합니다.")
                self.visualize(root, [root.value])  # 회전 전 시각화
                return self.rotateLeft(root)

        return root

    def delete(self, root, key):
        # 1. 일반 이진 탐색 트리 삭제
        if not root:
            return root

        if key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            # 노드가 하나의 자식을 가질 때
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # 두 자식을 가진 경우: 오른쪽 서브트리에서 가장 작은 값 찾기
            temp = self.getMinValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        # 조상의 높이 업데이트
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # 균형 인수 계산
        balance = self.getBalance(root)

        # 불균형 상태에서 회전 수행
        if balance > 1:
            if self.getBalance(root.left) < 0:  # 왼쪽-오른쪽 경우
                root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)

        if balance < -1:
            if self.getBalance(root.right) > 0:  # 오른쪽-왼쪽 경우
                root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def getMinValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rotateRight(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def visualize(self, root, imbalance_keys=None):
        G = nx.DiGraph()
        self._add_edges(G, root)
        pos = self._get_positions(root, 0, 0, 1)

        # 각 노드의 균형 인수에 따라 색상 결정
        node_colors = []
        for node in G.nodes():
            balance = self.getBalance(self.find_node(root, node))
            if balance < -1 or balance > 1:
                node_colors.append('red')  # 불균형 노드
            else:
                node_colors.append('lightblue')  # 균형 노드

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=False, arrows=True, node_size=2000, font_size=12, font_weight='bold', node_color=node_colors)

        # 각 노드의 값, 깊이, 균형 인수 및 설명을 표시
        for node in G.nodes():
            depth = self.get_depth(root, node)
            balance = self.getBalance(self.find_node(root, node))
            left_height = self.getHeight(self.find_node(root, node).left)
            right_height = self.getHeight(self.find_node(root, node).right)
            plt.text(pos[node][0], pos[node][1], f"{node}\n(D: {depth}, BF: {balance})\nL: {left_height}, R: {right_height}", fontsize=10, ha='center')

        plt.axis('off')
        plt.title("AVL 트리 시각화")
        plt.show()

    def get_depth(self, node, value, depth=0):
        if node is None:
            return -1
        if node.value == value:
            return depth
        left_depth = self.get_depth(node.left, value, depth + 1)
        if left_depth != -1:
            return left_depth
        return self.get_depth(node.right, value, depth + 1)

    def find_node(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        left_node = self.find_node(node.left, value)
        if left_node:
            return left_node
        return self.find_node(node.right, value)

    def _add_edges(self, G, node):
        if node is not None:
            if node.left is not None:
                G.add_edge(node.value, node.left.value)
                self._add_edges(G, node.left)
            if node.right is not None:
                G.add_edge(node.value, node.right.value)
                self._add_edges(G, node.right)

    def _get_positions(self, node, x, y, layer):
        pos = {}
        if node is not None:
            pos[node.value] = (x, y)
            pos.update(self._get_positions(node.left, x - 1 / (2 ** layer), y - 1, layer + 1))
            pos.update(self._get_positions(node.right, x + 1 / (2 ** layer), y - 1, layer + 1))
        return pos

# 메인 함수
if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    # 다양한 회전 상황을 테스트하기 위한 값
    values_to_insert = [10, 20, 30, 25, 40, 50, 5, 15] 
    print("불균형 AVL 트리를 생성하기 위해 값을 삽입합니다:")
    for value in values_to_insert:
        print(f"{value}를 삽입합니다.")
        root = avl_tree.insert(root, value)
        avl_tree.visualize(root)  # 시각화
