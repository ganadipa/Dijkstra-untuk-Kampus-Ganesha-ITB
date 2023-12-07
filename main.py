from constants import *
from utils import *
from Graph import Graph
from time import time

class Application():
    current_location: int
    
    
    
    @staticmethod
    def start():
        print("*** Dimana lokasi Anda sekarang? ***\n")
        for i in range(len(ganesha_map)):
            print(f'{i+1}. {ganesha_map[i]}')
        
        Application.get_current_location()
        Application.get_nearest()
        
        
    @staticmethod
    def get_current_location():
        inp = int_input(f"\nSilakan masukkan angka yang mewakili lokasimu sekarang. (1-{len(ganesha_map)}) ", force = True)
        if (inp > len(ganesha_map) or inp < 1):
            print(f'Input bukan merupakan angka yang telah dibatasi (1-{len(ganesha_map)}). Ulangi\n\n');
            Application.get_current_location()
        else:
            Application.current_location = inp - 1
    
    @staticmethod
    def get_nearest():
        print("\nSearching...\n")
        start_time = time()
        
        g = Graph()
        loc = Application.current_location
        
        for i in range(1):
            nodes = g.find_nearest(loc, method = 'dijkstra')
            
        
        print(f"Musholla terdekat : {ganesha_map[nodes[0][0]]} ({nodes[0][1]} detik.)")
        print(f"Kantin terdekat   : {ganesha_map[nodes[1][0]]} ({nodes[1][1]} detik.)")
        print(f"\n\nFinished searching in {time() - start_time:.4f} seconds.")
        
        
        

if __name__ == '__main__':
    Application.start()