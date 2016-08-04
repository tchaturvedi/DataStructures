from ds import Stack
from list import UnorderedList


def change_base(number, base):
    digits = "0123456789ABCDEF"
    remStack = Stack()
    b = ''

    while (number != 0):
        rem = number % base
        remStack.push(rem)
        number = number // base

    while not remStack.is_empty():
        b = b + digits[remStack.pop()]

    return b


#
# print(change_base(42, 2))
# print(change_base(11, 2))
# print(change_base(42, 8))
# print(change_base(11, 16))

mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.getSize())
print(mylist.contains(93))
print(mylist.contains(100))

mylist.add(100)
print(mylist.contains(100))
print(mylist.getSize())

mylist.remove(54)
print(mylist.getSize())
mylist.remove(93)
print(mylist.getSize())
mylist.remove(31)
print(mylist.getSize())
print(mylist.contains(93))
