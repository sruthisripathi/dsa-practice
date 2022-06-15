from typing import List

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.nxt = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def construct_from_lot(self, node_list: List) -> None:
        if len(node_list) > 0:
            queue = list()
            queue.append(Node(node_list[0]))
            idx = 1
            while len(queue) > 0:
                node = queue.pop(0)
                if self.root is None:
                    self.root = node
                left = Node(node_list[idx]) if idx < len(node_list) and node_list[idx] is not None else None
                node.left = left
                idx += 1
                right = Node(node_list[idx]) if idx < len(node_list) and node_list[idx] is not None else None
                node.right = right
                idx += 1
                if left is not None:
                    queue.append(left)
                if right is not None:
                    queue.append(right)

    # def level_order_traversal(self, return_nodes=False):
    #     queue = [[self.root]]
    #     if return_nodes:
    #         res = [[self.root]]
    #     else:
    #         res = [[self.root.val]]
    #     while len(queue) > 0:
    #         nodes = queue.pop(0)
    #         level = []
    #         level_vals = []
    #         for node in nodes:
    #             if node.left:
    #                 level.append(node.left)
    #                 level_vals.append(node.left.val)
    #             if node.right:
    #                 level.append(node.right)
    #                 level_vals.append(node.right.val)
    #         if level:
    #             queue.append(level)
    #             if return_nodes:
    #                 res.append(level)
    #             else:
    #                 res.append(level_vals)
    #     return res

    def level_order_traversal(self, return_nodes=False):
        # Don't have to use queue as we are directly storing levels
        level = [self.root]
        if return_nodes:
            lot = [level]
        else:
            lot = [[self.root.val]]
        while level:
            curr = []
            for node in level:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            level = curr
            if level:
                if return_nodes:
                    lot.append(level)
                else:
                    lot.append([node.val for node in level])
        return lot

    def left_view(self):
        lot = self.level_order_traversal()
        return [el[0] for el in lot]
    
    def right_view(self):
        lot = self.level_order_traversal()
        return [el[-1] for el in lot]
