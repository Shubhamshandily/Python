#**********Class Decorator**************
print("\n***************Class Decorator***************")
class square:
    def __init__(self,side):
        self._side=side
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self, value):
        if value>=0:
            self._side=value
        else:
            print("Error")
    @property
    def area(self):
        return self._side**2
    @classmethod
    def unit_square(cls):
        return(1)
s=square(5)
print(s.side)
print(s.area)
