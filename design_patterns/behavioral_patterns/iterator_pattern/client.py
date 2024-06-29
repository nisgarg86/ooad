"""
client class for the iterator pattern
"""

from collection import NumericCollection


def main():

    collection = NumericCollection()
    collection.add(1)
    collection.add(2)
    collection.add(3)
    collection.add(4)
    collection.add(5)

    for item in collection:  # this uses the iterator returnned by __iter__ method in collection
        print(item)

    print('----------------')

    alternate_iterator = collection.get_alternate_iterator()
    while alternate_iterator.has_next():
        print(alternate_iterator.__next__())


if __name__ == '__main__':
    main()

