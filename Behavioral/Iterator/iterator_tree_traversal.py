class Node:
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value

    self.parent = None

    if left:
      self.left.parent = self
    if right:
      self.right.parent = self

  def __iter__(self):
    return InOrderIterator(self)


class InOrderIterator:
  def __init__(self, root):
    self.root = self.current = root
    self.yielded_start = False

    while self.current.left: # while there exists a node on the left
      self.current = self.current.left

  def __next__(self):
    if not self.yielded_start:
      self.yielded_start = True
      return self.current

    if self.current.right:
      self.current = self.current.right
      while self.current.left:
        self.current = self.current.left
      return self.current
    else:
      p = self.current.parent
      while p and self.current == p.right:
        self.current = p
        p = p.parent
      self.current = p
      if self.current:
        return self.current
      else:
        raise StopIteration

def traverse_in_order(root):
  def traverse(current):
    # Do the left child traversal first
    if current.left:
      for left in traverse(current.left): 
        yield left # yield left recursively
    yield current

    # Then do the right child traversal next
    if current.right:
      for right in traverse(current.right):
        yield right # yield right recursively

  for node in traverse(root):
    yield node



if __name__ == '__main__':
  # Tree #1:
  #
  #      1
  #     / \
  #    2   3
  #   / \ / \
  #  4  5 6  7

  # in-order: 4251637
  # pre-order: 
  # post-order: 

  # Tree #2:
  #
  #      1
  #     / \
  #    2   3

  # in-order: 213
  # pre-order: 123
  # post-order: 231

  tree1 = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
  tree2 = Node(1, Node(2), Node(2))

  it = iter(tree1)

  print([next(it).value for x in range(7)])
  print()

  for x in tree1:
    print(x.value)
  print()


  # More effective and readable way to traverse instead of manipulating `__iter__` and `__next__`
  for y in traverse_in_order(tree1):
    print(y.value)
  print()