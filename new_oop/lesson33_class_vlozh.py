class Women:
    title = "Обьект класса для поля title"
    photo = "Обьект класса для поля photo"
    ordering = "Обьект класса для поля ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + "@" + psw)

    class Meta:
        ordering = ["id"]

        def __init__(self, access):
            self._access = access


w = Women("root", "12345")

print(w.ordering)
print(w.Meta.ordering)
print(w.__dict__)
