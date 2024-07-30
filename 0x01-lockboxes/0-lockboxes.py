#!/usr/bin/python3
def canUnlockAll(boxes):
  """
  Determines if all boxes can be opened.

  Args:
    boxes: A list of lists, where each inner list contains keys to other boxes.

  Returns:
    True if all boxes can be opened, False otherwise.
  """

  n = len(boxes)
  visited = [False] * n
  visited[0] = True  # The first box is unlocked

  def dfs(box_index):
    for key in boxes[box_index]:
      if 0 <= key < n and not visited[key]:
        visited[key] = True
        dfs(key)

  dfs(0)
  return all(visited)

