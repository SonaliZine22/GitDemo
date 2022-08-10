from collections1 import Counter

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.values())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

from collections1 import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)

from collections1 import OrderedDict
ordered_dict = {}
ordered_dict['a'] = 5
ordered_dict['b'] = 4
ordered_dict['c'] = 2
ordered_dict['d'] = 3
ordered_dict['e'] = 1
print(ordered_dict)


from collections1 import defaultdict
d = defaultdict(int)
d['a'] =1
d['b'] =2
print(d['a'])
print(d['c'])

from collections1 import deque
d = deque()

d.append(1)
d.append(2)
d.append(4)
d.appendleft(3)
print(d)

d.pop()
print(d)

d.extendleft([7, 8, 9])
print(d)
d.rotate(-1)
print(d)

