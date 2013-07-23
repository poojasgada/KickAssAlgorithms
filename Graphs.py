'''
Created on Jul 13, 2013

@author: psgada
'''

'''
Using a adjacency list, traverse a graph using adjacency list for graph representation
'''
import Queue

graph_adj_list = {
                  1: [2,3,4],
                  2: [1,3],
                  3: [1,2,7,8],
                  4: [1,5,6],
                  5: [4],
                  6: [4],
                  7: [3],
                  8: [3]
                  }

def bfs():
    bfs_q = Queue.Queue()
    visited = set()
    source = 1
    
    visited.add(source)
    bfs_q.put(source)
    
    while not bfs_q.empty():
        cur = bfs_q.get()
        for node in graph_adj_list[cur]:
            if node not in visited:
                print node
                visited.add(node)
                bfs_q.put(node)
        
    #print visited

def bfs_shortest_path():
    bfs_q = Queue.Queue()
    visited = set()
    source = 1
    dist = { 1:0, 2:0, 3:0 , 4:0, 5:0, 6:0, 7:0, 8:0}
    
    visited.add(source)
    bfs_q.put(source)
    count = 1
    while not bfs_q.empty():
        cur = bfs_q.get()       
        for node in graph_adj_list[cur]:
            if node not in visited:
                dist[node] = dist[cur] + 1
                visited.add(node)
                bfs_q.put(node)
                
                
    print dist[3]
     
def dfs():
    visited = set()
    dfs_l = []
    source = 1
    visited.add(source)
    dfs_l.append(source)
    
    while len(dfs_l) > 0:
        cur = dfs_l.pop()
        print cur
        for node in graph_adj_list[cur]:
            if node not in visited:
                dfs_l.append(node)
                visited.add(node)
                
def dfs_recursive(cur, visited):
    
    print cur
    visited.add(cur)
    
    for node in graph_adj_list[cur]:
        if node not in visited:
            dfs_recursive(node, visited)

bfs()
print "\n\n"

dfs()

print "Recursive"
dfs_recursive(1, set())

print "Shortest path"
bfs_shortest_path()
