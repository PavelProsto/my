class Triangle():
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.h = (a ** 2 + b ** 2) ** (1/2)