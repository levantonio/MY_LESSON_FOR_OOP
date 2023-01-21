class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")
        return args[0].strip(self.__chars)


s1 = StripChars("-*/!@#$%^&*()?")
res1 = s1("/*-Hello World???")
print(res1)
s2 = StripChars("QWERTYUIOPLKJHGFDSAZXCVBNM")
res2 = s2("HeLlO WoRlD")
print(res2)
