from typing import List
from DS.BinaryTree import BinaryTree

def connect(node_list: List) -> List:
    """
    Populate each next pointer to point to its next right node.
    If there is no next right node, the next pointer should be set to NULL.
    """
    BT = BinaryTree()
    BT.construct_from_lot(node_list)
    lot = BT.level_order_traversal(return_nodes=True)
    res = []
    for level in lot:
        for i in range(len(level)):
            level[i].nxt = level[i+1] if i+1 < len(level) else None
            res.append(level[i].val)
        res.append(None)
    return res


# node_list = [1,2,3,4,5,None,7]
node_list = [1,2,None,4,5,7,None,8]
BT = BinaryTree()
BT.construct_from_lot(node_list)
print(BT.level_order_traversal())
print(connect(node_list))
