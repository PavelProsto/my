class Vektor3D():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    def __str__(self, x, y, z) -> str:
        return str(self.x + ', ' + self.y + ', ' + self.z)
    def __add__(self, x, y, z):
        return (self.x + x, self.y + y, self.z + z)
        
