
from OopsDemo import Calculator


class childClass(Calculator):
    num2 =200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getData(self):
        return self.num2 + self.num + self.summation()


obj = childClass()
print(obj.getData())


