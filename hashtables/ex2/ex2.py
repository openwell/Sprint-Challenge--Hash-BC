#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(length): # 1
        hash_table_insert(ht, tickets[i].source, tickets[i].destination )

    first_item = hash_table_retrieve(ht, "NONE") # 2
    route[0] = first_item # 3

    for i in range(1, length): # 4
        next_item = hash_table_retrieve(ht, route[i-1]) # 5
        # if next_item != 'NONE':
        route[i] = next_item # 6
        print("Updated Route: ", route)

    return route # 7
