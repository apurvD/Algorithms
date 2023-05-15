graph={
    '2':['1','3'],
    '1':['4','5'],
    '3':['6','7'],
    '4':[],
    '5':[],
    '6':[],
    '7':[]
}
visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbor in graph:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("Following is the BFS result:\n")

bfs(visited,graph,'2')