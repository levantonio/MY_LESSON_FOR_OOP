class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for k, v in self.class_attrs.items():
            self.__dict__[k] = v

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Woman(metaclass=Meta):
    title = 'Заголовок'  # логика формирования свойств из метода Meta
    comtent = "контент"
    photo = "Путь к фото"


w = Woman()
print(w.__dict__)
