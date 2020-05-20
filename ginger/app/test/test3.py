


class Man:
    name = 'Ken'
    age = 18

    def __init__(self):
        self.gender = '女'

    def keys(self):
        return ['name','age']

    def __getitem__(self, item):
        return getattr(self,item)



man = Man()
print(type(man))
t =dict(man)
print(t)
print(man.__dict__)
