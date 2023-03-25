class Posicion:

    def __init__(self, x, y):

        self.columna = x
        self.fila = y

    def __str__(self):
        return "({0}, {1}".format(self.columna, self.fila)

    def __eq__(self, pt2):
        return (self.columna == pt2.columna) and (self.fila == pt2.fila)