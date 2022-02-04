import copy
from time import process_time

# Using DFS on a problem tile search space is different to DFS on a normal tree. In normal examples the tree is already generated for you to traverse. However with the state space search we are looking for the path from initial state to goal state and applying operations/moves to these states to take us from one configuration to the other. The 'path' of these configurations from one state to ot another  thus becomes our nodes that make a tree/ or graph. 
def simulate(instanceList, goal):
  
  # This function checks the legal operations/ bounds for the blank tile. Checks if the blank tile can move up, down, left, or right
  def move_blank(i,j,n): 
      if i+1 < n: # move down
          yield (i+1,j)
      if i-1 >= 0: # move up
          yield (i-1,j) 
      if j+1 < n: # move right
          yield (i,j+1)
      if j-1 >= 0: # move left 
          yield (i,j-1)

  def move(state):    
      [i,j,grid]=state
      n = len(grid)
      for pos in move_blank(i, j, n):
          i1,j1 = pos
          grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
          yield[i1,j1,grid]
          grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
  
  def isGoal(state):
    return (state[2] == goal)

  def dfs_rec(path, depth):
    ctMove = 0
    if isGoal(path[-1]):
      return path, ctMove
    elif (depth > 0):
      state = copy.deepcopy(path[-1])
      for nextState in move(state): # Here we are effectively generating the nodes in our tree/graph
        ctMove +=1
        if nextState not in path: # Path is the same as visited ?
          path.append(nextState) # Path is now made longer 
          solution, moveCount = dfs_rec(path, depth-1)
          ctMove += moveCount
          if solution != None: # If path is not empty/ if there is children nodes?
            return solution, ctMove
          path.pop() # no more children, so remove from path, backtrack and traverse a different node
    return None, ctMove

  def DFID(startState):
    path = None
    depth = 0
    ctMove = 0
    while (path == None):
      path, moveCount = dfs_rec([startState], depth)
      ctMove += moveCount
      depth += 1
    return path, ctMove

  solutionList = []
  for instance in instanceList:
    start_time = process_time()
    path, moveCount = DFID(instance)
    elapsed = process_time() - start_time
    solutionList.append((len(path)-1, moveCount, elapsed))

  return solutionList

def main():
    instanceLists = \
        [
            [
                [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]],
                [0, 2, [[5, 6, 0], [1, 3, 8], [4, 7, 2]]],
                [2, 0, [[3, 5, 6], [1, 2, 7], [0, 8, 4]]],
                [1, 1, [[7, 3, 5], [4, 0, 2], [8, 1, 6]]],
                [2, 0, [[6, 4, 8], [7, 1, 3], [0, 2, 5]]]
            ],
            [
                [0, 0, [[0, 1, 8], [3, 6, 7], [5, 4, 2]]],
                [2, 0, [[6, 4, 1], [7, 3, 2], [0, 5, 8]]],
                [0, 0, [[0, 7, 1], [5, 4, 8], [6, 2, 3]]],
                [0, 2, [[5, 4, 0], [2, 3, 1], [8, 7, 6]]],
                [2, 1, [[8, 6, 7], [2, 5, 4], [3, 0, 1]]]
            ]
        ]
    goalList = \
        [
            [[3, 2, 0], [6, 1, 8], [4, 7, 5]],
            [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        ]

    for i in range(2):
        instanceList = instanceLists[i]
        goal = goalList[i]
        solutionList = simulate(instanceList, goal)
        print("\ninstances with goal ", goal, ":\n")
        for rec in solutionList:
            l, m, e = rec
            print("Depth = {:2d} Move = {:10d} Time= {:8.2f}".format(l, m, e))


if __name__ == "__main__":
  main()
 