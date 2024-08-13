class Terreno:
    
    def calcularAreaTerreno(self, A, B, C):
        areaTriangulo = (B * A) / 2
        areaRectangulo = B * C
        areaTotal = areaTriangulo + areaRectangulo
        
        return areaTotal