cups = [int(char) for char in '459672813']

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class CircularList:
    def __init__(self, node):
        self.head = node
        self.head.next = self.head
        self.head.previous = self.head
        self.nodes = {}
        self.nodes[self.head.value] = self.head

    def insert(self, value):
        new_node = Node(value)
        node = self.head
        while node.next is not self.head:
            node = node.next

        new_node.next = node.next
        new_node.previous = node
        node.next.previous = new_node
        node.next = new_node

        self.nodes[value] = new_node

    def insert_after(self, value, value_to_insert):
        new_node = Node(value_to_insert)
        node = self.nodes[value]

        new_node.next = node.next
        new_node.previous = node
        node.next.previous = new_node
        node.next = new_node
        self.nodes[value_to_insert] = new_node
        
    def delete(self, value):
        node = self.nodes[value]

        node.previous.next = node.next
        node.next.previous = node.previous
        if node is self.head: self.head = self.head.next
        del self.nodes[value]

    def pick_three(self, node):
        picked_up = []

        for _ in range(3):
            picked_up.append(node.next.value)
            node = node.next

        for cup in picked_up:
            self.delete(cup)

        return picked_up
    

head_node = Node(cups[0])
linked_cups = CircularList(head_node)

for cup in cups[1:]:
    linked_cups.insert(cup)

linked_cups.insert(10)
i = 10
while i < 1000000:
    i += 1
    linked_cups.insert_after(i - 1, i)

picked_up = []
current_cup = linked_cups.head
for i in range(10000000):
    picked_up.clear()

    picked_up = linked_cups.pick_three(current_cup)
    current_cups = linked_cups.nodes.keys()

    destination_cup = current_cup.value - 1
    if destination_cup <= 0: destination_cup = max(current_cups)
    while destination_cup not in current_cups:
        destination_cup -= 1
        if destination_cup <= 0: destination_cup = max(current_cups)

    for cup in reversed(picked_up):
        linked_cups.insert_after(destination_cup, cup)

    current_cup = current_cup.next

print(linked_cups.nodes[1].next.value * linked_cups.nodes[1].next.next.value)