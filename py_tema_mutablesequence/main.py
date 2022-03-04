from utils import print_header
from CrayonsBox import crayons_box

print_header('__init__')
print(crayons_box)

print_header('__list__')
print(list(crayons_box))

print_header('__len__')
print(len(crayons_box))

print_header('__getitem__')
print(crayons_box[5])

print_header('__delitem__')
print(crayons_box.__delitem__(1))

print_header('__setitem__')
print(crayons_box.__setitem__(5, 'Color'))

print_header('__insert__')
print(crayons_box.insert(4, 'Multicolor'))
