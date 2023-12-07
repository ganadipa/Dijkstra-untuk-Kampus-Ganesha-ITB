from constants import ganesha_map
from utils import *
from dijkstra import Graph

class Application():
    current_location: int
    
    
    
    @staticmethod
    def start():
        print("*** Dimana lokasi Anda sekarang? ***\n")
        print("Buka 'map.jpg' dan masukkan angka yang mewakili tempat mu sekarang.\n")
        for i in range(len(ganesha_map)):
            print(f'{i+1}. {ganesha_map[i]}')
        
        Application.get_current_location()
        Application.get_nearest()
        
        
    @staticmethod
    def get_current_location():
        inp = int_input(f"\nSilakan masukkan angka yang mewakili lokasimu sekarang. (1-{len(ganesha_map)}) ", force = True)
        if (inp > len(ganesha_map) or inp < 1):
            print('Input tidak valid. Ulangi\n\n');
            Application.get_current_location()
        else:
            current_location = inp
    
    @staticmethod
    def get_nearest():
        g = Graph()
        
        

if __name__ == '__main__':
    Application.start()