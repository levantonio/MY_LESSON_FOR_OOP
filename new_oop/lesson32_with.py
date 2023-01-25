class DefenderVector:
    def __init__(self, vector):
        self.__vector = vector

    def __enter__(self):
        self.__temp = self.__vector[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__vector[:] = self.__temp

        return False


v1 = [1, 2, 3]
v2 = [2, 3]

try:
    with DefenderVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Error")

print(v1)
