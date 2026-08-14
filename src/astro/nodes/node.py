class Node():
    def __init__(self, update_list: list):
        update_list.append(self)
    
    def update(self, delta):
        pass