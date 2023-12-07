from typing import List, Tuple
from utils import *
from constants import *
import heapq
import math



class Graph():
    
    adj: List[List[Tuple[int, int]]]
    
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
                dest -= 1 # File is 1-indexed, We (program) will use 0-indexed
                
                self.adj[start].append((dest, weight))
                self.adj[dest].append((start, weight))
                
                line = src.readline()
    
    def print_graph(self):
        print(self.adj)
        
    def find_nearest(self, start, method = 'dijkstra'):
        if (method == 'dijkstra'):
            return self.dijkstra(start)
            
    def dijkstra(self, start: int) -> List[Tuple[int, int]]:
        num_nodes = len(self.adj)
        distances = [float('inf')] * num_nodes
        distances[start] = 0

        priority_queue = [(0, start)]
        
        nearest_mushola = -1
        nearest_canteen = -1
        nearest_mushola_distance = float('inf')
        nearest_canteen_distance = float('inf')
        
        
        count = 0
        while priority_queue:
            count+= 1
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue
            
            
            if (is_in(current_node+1, mushola_node)) and current_distance < nearest_mushola_distance: # mushola_node is 1-indexed
                nearest_mushola = current_node
                nearest_mushola_distance = current_distance
            
            if (is_in(current_node+1, canteen_node)) and current_distance < nearest_canteen_distance:
                nearest_canteen = current_node
                nearest_canteen_distance = current_distance
                

            # if (current_node+1) in mushola_node:
            #     nearest_mushola = current_node
            #     count += len(mushola_node)
            
            # if (current_node+1) in canteen_node:
            #     nearest_canteen = current_node
            #     count += len(mushola_node)
                
                
            if (nearest_mushola != -1 and nearest_canteen != -1):
                break

            for neighbor, weight in self.adj[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return [(nearest_mushola, nearest_mushola_distance), (nearest_canteen, nearest_canteen_distance)]
            
                
                
                
                
        
        