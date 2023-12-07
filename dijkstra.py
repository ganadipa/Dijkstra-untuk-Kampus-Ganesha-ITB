from typing import List, Tuple



class Graph():
    
    adj: List[List[Tuple[int]]]
    
    def __init__(self):
        with open("graph.txt", 'r') as src:
            line = src.readline()
            numnode = int(line)
            
            self.adj = [list() for i in range(numnode)]
            
            line = src.readline()
            while line != "":
                
                start, dest, weight = map(float, line.split())
                start, dest = map(int, (start,dest))
                
                start -= 1
                dest -= 1 # File is 1=indexed, We will use 0-indexed
                
                self.adj[start].append((dest, weight))
                
                line = src.readline()
        
        self.print_graph()
    
    def print_graph(self):
        print(self.adj)
                
                
                
                
        
        