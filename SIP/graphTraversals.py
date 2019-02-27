def breadth_first_search_adapted(graph, root):
    visited = []
    tovisit = [root]
    visited_with_distances = {root: 0}
    while len(tovisit) != 0 :
        n = tovisit.pop(0)
        if not n in visited:
            for m in neighbors(graph, n):
                if m in visited :
                    continue
                tovisit.append(m)
                if not m in visited_with_distances :
                    visited_with_distances[m] = visited_with_distances[n] + 1
            visited.append(n)
    return visited_with_distances


adapted_bfs=breadth_first_search_adapted(my_graph,'0')
print(adapted_bfs)

def is_bipartite(graph):
    depth = breadth_first_search_adapted(graph, '0')
    for v in nodes(graph) :
        for n in neighbors(graph, v) :
            if depth[v] == depth[n] :
                return False
    return True

my_graph1=load_graph(graph01)
print("graph01 is bipatite?", is_bipartite(my_graph1))     # >>> False

my_graph2=load_graph(graph02)
print("graph02 is bipatite?", is_bipartite(my_graph2))     # >>> True

##

import math

hameau = {
    'a': {'b': 4, 'f': 8},
    'b': {'a': 4, 'f': 9, 'g': 7, 'h': 3, 'c': 10, 'd': 12},
    'c': {'b': 10, 'd': 3},
    'd': {'c': 3, 'b': 12, 'h': 10, 'e': 6},
    'e': {'f': 7, 'g': 6, 'h': 3, 'd': 6},
    'f': {'a': 8, 'b': 9, 'g': 4, 'e': 7},
    'g': {'f': 4, 'b': 7, 'h': 3, 'e': 6},
    'h': {'b': 3, 'g': 3, 'd': 10, 'e': 3}
}



def dijkstra(graph, start) :
  frontier = set(start)
  state = {v:(math.inf, None) for v in graph}  # pairs (distance, parent)
  state[start] = (0, None)

  while len(frontier) > 0 :
    min_node = min(frontier, key=lambda n: state[n][0])
    frontier.remove(min_node)

    for n in graph[min_node] :
      # Skip start node, we know its distance is 0
      if n == start :
        continue
      # Compute distance to n when coming from min_node
      new_dist = state[min_node][0] + graph[min_node][n]
      # Add newly touched vertices to the frontier
      if state[n][1] == None:
        frontier.add(n)
        state[n] = (new_dist, min_node) # update distance
      elif new_dist < state[n][0] :  # If the new one is smaller
        state[n] = (new_dist, min_node) # update distance

  return state

print(dijkstra(hameau, 'g'))



def prim(graph, start) :
  # The initial frontier is the neighbors of the start node
  frontier = set(graph[start].keys())
  # The initial spanning tree has just start as root
  state = {start:(0, None)} # pairs (distance, parent)

  while len(frontier) > 0 :
    # Look for a node in the frontier with a minimal distance to a node of the tree
    (min_node, from_node, min_dist) = (None, None, math.inf)
    for n in frontier :
      for m in graph[n] :
        if m in state and graph[n][m] < min_dist :
          (min_node, from_node, min_dist) = (n, m, graph[n][m])
    # We remove the min node from the frontier
    frontier.remove(min_node)
    # And we add it to the spanning tree
    state[min_node] = (min_dist, from_node)
    # We add the neighbors of the min_node to the frontier
    for n in graph[min_node].keys() :
      if not n in state :
        frontier.add(n)

  return state

print(prim(hameau, 'g'))



def kruskal(graph):
  # Edges sorted by increasing value
  edges = sorted([(graph[i][j], i, j) \
                    for i in list(graph.keys()) \
                    for j in graph[i] if i < j])

  # Connex components for each node. Initially, each node is in its own component
  components = {i:i for i in graph}
  mst = []

  for e in edges :
    c1 = components[e[1]]
    c2 = components[e[2]]
    if c1 != c2 : # if e connects two different components
      mst.append((e[1], e[2]))  # append it to the MST
      for i in components:  # Update the components
        if components[i] == c2 :
          components[i] = c1
      if len(set(components.values())) == 1 :
        break
  return mst

print(kruskal(hameau))

##

stock = [ ('lemonde', 2),
          ('lefigaro', 1),
                    ('liberation',4),
                    ('lesechos',3),
                    ('lequipe',5)
]

def get_dicho(stock, prod):
    begin, end = 0, len(stock)-1
    while begin <= end:
        middle = begin + int((end-begin)/2)
        if stock[middle][0] == prod:
            return stock[middle][1]
        elif (stock[middle][0] > prod): # lexicographic comparison
            end = middle - 1
        else:
            begin = middle + 1
    return None

stock.sort()

print(get_dicho(stock, 'lesechos'))

##

def Link(value, next) :
    return {'value': value, 'next': next}

def LinkedList() :
    return {'first': None}

def listAppend(list, value) :
    return {'first': Link(value, list['first'])}

def printList(list) :
    res = '['
    cur = list['first']
    first = True
    while cur != None :
        if first :
            first = False
        else :
            res += ', '
        res += str(cur['value'])
        cur = cur['next']
    res += ']'
    return res


##
class Link :
    def __init__(self, value, next) :
        self.value = value
        self.next = next

class LinkedList :
    def __init__(self):
        self.first = None

    def append(self, value):
        self.first = Link(value, self.first)

    def get(self, index) :
        idx = 0
        cur = self.first
        while cur != None :
            if idx == index :
                return cur.value
            cur = cur.next
            idx += 1
        return None

    def remove(self, index) :
        idx = 0
        prev = None
        cur = self.first
        while cur != None :
            if idx == index :
                if prev == None :
                    self.first = cur.next
                else :
                    prev.next = cur.next
                return
            prev = cur
            cur = cur.next
            idx += 1

    def removeValue(self, value) :
        prev = None
        cur = self.first
        while cur != None :
            if cur.value == value :
                if prev == None :
                    self.first = cur.next
                else :
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

    def __str__(self) :
        res = '['
        cur = self.first
        while cur != None :
            if cur != self.first :
                res += ', '
            res += str(cur.value)
            cur = cur.next
        res += ']'
        return res


##

graph = {   1: {2:1, 3:2},
            2: {3:1, 4:4},
            3: {4:1, 5:1},
            4: {5:1, 6:2},
            5: {6:1, 7:6},
            6: {7:1, 8:2},
            7: {8:1, 9:2},
            8: {9:1, 10:4},
            9: {10:1,11:1},
           10: {11:1,12:4},
           11: {12:1},
           12: {}
         }

import math

# https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford
def bellman_ford(graph):
    # dist[t, k] = (distance, parent) from the source to t with at most k arcs
    # Initial value is infinite
    dist = {v:[(math.inf, None) for _ in range(len(graph))] for v in graph}
    # Excepted for the starting vertex
    dist[list(graph.keys())[0]][0] = (0, None)

    # We compute the distance for growing k
    for k in range(1,len(graph)) :
        for t in graph :
            # We start with the distance with k-1 arcs
            dist[t][k] = dist[t][k-1]
            # And we check with incoming arcs
            for u in graph :
                if t in graph[u] :
                    # We take the opposite of the log of the cost so that the
                    # shortest path corresponds to the maximum multiplicative gain
                    nd = dist[u][k-1][0]+(-math.log(graph[u][t]))
                    if nd < dist[t][k][0] :
                        dist[t][k] = (nd, u)
    # We compute the gain from the log before returning the result
    return {v:(math.exp(-dist[v][len(graph)-1][0]), dist[v][len(graph)-1][1]) for v in graph}

print(bellman_ford(graph))

def best_path(dist) :
    path = []
    best = max(dist, key=lambda v: dist[v][0])
    while best != None :
        path.insert(0, best)
        best = dist[best][1]
    return path

print(best_path(bellman_ford(graph)))

##

weights = [4, 4, 5, 5, 5, 4, 4, 6, 6, 2, 2, 3, 3, 7, 7, 2, 2, 5, 5, 8, 8, 4, 4, 5]
capacity = 10

def check_packing(items, bags, capacity, max_bags) :
  if len(bags) > max_bags :
    return False
  packed_items = [item for bag in bags for item in bag]
  if sorted(items) != sorted(packed_items) :
    return False
  for bag in bags :
    if sum(bag) > capacity :
      return False
  return True

def NextFit(items, capacity) :
  bags = [[]]
  for item in items :
    if sum(bags[-1]) + item > capacity :
      bags.append([item])
    else :
      bags[-1].append(item)
  return bags

def FirstFit(items, capacity) :
  bags = []
  for item in items :
    placed = False
    for bag in bags :
      if sum(bag) + item <= capacity :
        placed = True
        bag.append(item)
        break
    if not placed :
      bags.append([item])
  return bags

def FirstFitDecreasing(items, capacity) :
  return FirstFit(sorted(items, reverse=True), capacity)

def BestFit(items, capacity):
  bags = []
  for item in items :
    best_bag = None
    min_space = None
    for idx in range(len(bags)):
      space = capacity - sum(bags[idx])
      if item <= space and (min_space is None or space < min_space) :
        best_bag = idx
        min_space = space
    if best_bag is None:
      bags.append([item])
    else:
      bags[best_bag].append(item)
  return bags

def BestFitDecreasing(items, capacity) :
  return BestFit(sorted(items, reverse=True), capacity)

for algo in [NextFit, FirstFit, BestFit, FirstFitDecreasing, BestFitDecreasing] :
  bags = algo(weights, capacity)
  print(algo.__name__)
  print(bags)
  print("# bags = ", len(bags),
        ", check packing: ", check_packing(weights, bags, capacity, len(bags)))
  print()
