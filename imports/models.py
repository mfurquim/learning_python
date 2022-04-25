class ModelA:
    def __init__(self, a):
        self._a = a

    def __repr__(self):
        return f"ModelA (a: {self._a})"


class ModelB:
    def __init__(self, b):
        self._b = b

    def __repr__(self):
        return f"ModelA (b: {self._b})"
