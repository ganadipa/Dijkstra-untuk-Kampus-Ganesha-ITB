import unittest
import os
from Graph import Graph

class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        g = Graph()
        
        input_files = [f for f in os.listdir('./tests') if f.endswith('.in')]
        expected_files = [f for f in os.listdir('./tests') if f.endswith('.out')]

        length = len(input_files)
        for i in range(length):
            
            inp = []
            with open("tests/" +input_files[i], "r") as f:
                t = int(f.readline())
                for j in range(t):
                    inp.append(int(f.readline()) -1)
            
            
            exp = []
            with open("tests/" + expected_files[i], "r") as f:
                for j in range(t):
                    exp_nearest_musholla, exp_nearest_musholla_distance = map(int, f.readline().strip().split(" "))
                    
                    exp_nearest_canteen, exp_nearest_canteen_distance = map(int, f.readline().strip().split(" "))
                    
                    exp_nearest_musholla -= 1
                    exp_nearest_canteen -= 1
                    
                    exp.append([
                        (exp_nearest_musholla, exp_nearest_musholla_distance),
                        (exp_nearest_canteen, exp_nearest_canteen_distance)
                                ])

            for i in range(t):
                self.assertEqual(g.find_nearest(inp[i], 'dijkstra'), exp[i])

if __name__ == '__main__':
    unittest.main()