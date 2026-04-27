class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjacency_map = {}

        for e in edges:
            if e[0] not in adjacency_map:
                adjacency_map[e[0]] = set()

            if e[1] not in adjacency_map:
                adjacency_map[e[1]] = set()

            adjacency_map[e[0]].add(e[1])
            adjacency_map[e[1]].add(e[0])

        print(adjacency_map)

        # Try dfs
        visited = set()
        components = 0

        for curnode in range(n):

            # We have no edges here
            if curnode not in adjacency_map:
                components += 1
                continue

            if curnode in visited:
                continue

            edges = adjacency_map[curnode]
            q = deque(edges)
            visited.add(curnode)

            print("Doing node",curnode,"with edges",edges)


            i = 5
            while q:

                edge = q.pop()
                print("Doing edge", edge)

                if edge in visited:
                    continue

                if edge not in adjacency_map:
                    print("Dead end",edge)
                    continue

                visited.add(edge)
                new_nodes = adjacency_map[edge]
                print("Edges", new_nodes)

                # For each edge
                for new_node in new_nodes:

                    print("Visiting edge", new_node)
                    
                    # DFS append edges in order
                    if new_node not in visited:
                        # Adding to visited
                        print("Enqueuing new edge", new_node)
                        q.append(new_node)
                    else:
                        print("Already visited")
            
            print("Edges exausted")

            components += 1

        return components
                




            


            
        

        







