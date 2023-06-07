import random
import math
random.seed(42)

class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def __str__(self) -> str:
        return str(self.value)

    def add_child(self, node) -> None:
        self.children.append(node)

    def is_leaf(self):
        return len(self.children) == 0

    def get_depth(self) -> int:
        if self.is_leaf():
            return 1
        
        depth_list = [child.get_depth() for child in self.children]
        return max(depth_list) + 1
    
    def dfs(self)  -> list:
        if self.is_leaf():
            return [self.value]
        
        result_list = []
        for child in self.children:
            result_list += child.dfs()
        result_list.append(self.value)
        return result_list
    
    def get_paths(self)  -> list:
        list_path = [self.value]
        if not self.is_leaf():
            new_list_path = []
            for child in self.children:
                retour_child = child.get_paths()
                copy_path = (list_path.copy() + retour_child)
                new_list_path += copy_path
            return new_list_path
        return list_path



    # def get_paths(self)  -> list:
    #     list_path = [self.value]
    #     if not self.is_leaf():
    #         new_list_path = []
    #         for child in self.children:
    #             copy_path = (list_path.copy() + child.get_paths())
    #             new_list_path += copy_path
    #         return new_list_path
    #     return list_path

    # def get_paths(self)  -> list:
    #     list_path = self.value
    #     if not self.is_leaf():
    #         new_list_path = {}
    #         for child in self.children:
    #             list_path = list_path.copy()
    #             list_path.update(child.get_paths())
    #             new_list_path.update(list_path)
    #         return new_list_path
    #     return list_path

    def bfs(self) -> list:
        queue = [self]
        result = []
        while len(queue) != 0:
            elt = queue.pop(0)
            result.append(elt.value)
            for child in elt.children:
                queue.append(child)
        return result
    
    def add_floor(self, positions):
            for elt in positions:
                new_node = Tree(elt)
                self.add_child(new_node)
                new_positions = positions.copy()
                new_positions.remove(elt)
                if len(new_positions) > 0:
                    new_node.add_floor(new_positions)

    def create_tree(self, nb_nodes):
        positions = []

        for i in range(nb_nodes):
            positions.append({i + 1: (random.randrange(5000), random.randrange(5000))})
        self.add_floor(positions)

    
root = Tree({0: (0, 0)})
root.create_tree(3)
print(root.get_paths())









# for key in self.value.values():
#             value = key
#         if self.is_leaf():
#             return [value]
        
#         result_list = []
#         for child in self.children:
#             result_list += child.dfs()
#         result_list.append(value)
#         return result_list