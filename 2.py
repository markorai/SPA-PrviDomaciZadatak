class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self,head=None):
    self.head = head

  def append(self,new_node):
    current = self.head
    if self.head:
      while current.next:
        current = current.next
      current.next = new_node
    else:
      self.head = new_node

  def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

# 2C - Napisati funkciju koja na osnovu ulazne liste l1, kreira i štampa novu listu l2, a koja se sastoji od neparnih elemenata iz liste l1 koje je potrebno kvadrirati
def squared_odd_nodes_list(l1):
  l2 = LinkedList()
  current = l1.head
  if l1.head:
    while current:
      if current.value % 2 == 1:
        l2.append(Node(pow(current.value,2)))
      current = current.next
  else:
    return None
  l2.print_list()

# 2E- Napisati funkciju koja na osnovu ulazne liste l1, kreira i štampa novu listu l2, a koja se sastoji od negativnih elemenata iz liste l1 koje je potrebno kvadrirati

def squared_neg_nodes_list(l1):
  l2 = LinkedList()
  current = l1.head
  if l1.head:
    while current:
      if current.value < 0:
        l2.append(Node(pow(current.value,2)))
      current = current.next
  else:
    return None
  l2.print_list()

# 2H - Napisati funkciju koja iz liste l1 uklanja svaki drugi element, počevši od prvog elementa
def remove_evr_sec(l1):
  current = l1.head
  prev = None
  while current.next:
    prev = current
    current = current.next
    prev.next = current.next
  
  return l1

# 2J - Napisati funkciju koja nalazi drugi najmanji element liste i vraća taj element
def second_min_node(l1):
    current = l1.head
    min = l1.head.value
    second_min = l1.head.value
    temp = 0
    while current.next:
      if(current.value < min):
        min = current.value
      current = current.next

    current = l1.head
    while current.next and temp == 0:
      if(current.value != min):
        second_min = current.value
        temp = 1
      current = current.next

    current = l1.head
    while current.next:
      if current.value < second_min and min < current.value:
        second_min = current.value
      current = current.next

    return second_min

# 2R - Data je jednostruko olančana lista. Transformisati postojeću ili kreirati
#novu jednostruko olančanu listu tako da prvi dio liste čine negativni
#brojevi, a ostatak pozitivni brojevi. Elemente čija je vrijednost 0 smjestiti
#na kraj liste. Potrebno je očuvati raspored iz originalne liste.
def task_2_r(l1):
  l2 = LinkedList()
  if l1.head:
    current = l1.head
    while current:
      if current.value < 0:
        l2.append(Node(current.value))
      current = current.next

    current = l1.head
    while current:
      if current.value > 0:
        l2.append(Node(current.value))
      current = current.next

    current = l1.head
    while current:
      if current.value == 0:
        l2.append(Node(current.value))
      current = current.next

    return l2

  else:
    return None