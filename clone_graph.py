"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned_nodes: Dict[Node, Node] = {}

        def dfs(original_node: 'None') -> 'None':
            if original_node in cloned_nodes:
                return cloned_nodes[original_node]
            
            clone = Node(original_node.val)
            cloned_nodes[original_node] = clone

            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
