import math

class Punto(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class TerransSolution(object):
    coordenadas = []
    def distancia_puntos(self, x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def terrans(self):
        x = 0
        y = 1
        t = int(input())
        for x in range(t):
            n = int(input())
            for i in range(n):
                px = int(input())
                py = int(input())
                self.coordenadas.append(Punto(px,py))
            bomba_x = int(input())
            bomba_y = int(input())
            bomba_radio = int(input())
            sum_struct = 0
            for i in range(n):
                if self.distancia_puntos(self.coordenadas[i].x, self.coordenadas[i].y, bomba_x, bomba_y) <= bomba_radio:
                    sum_struct += 1
            print(sum_struct)
        

def main():
    oTerrans = TerransSolution()
    oTerrans.terrans()

 
if __name__ == '__main__':
    main()
                    
