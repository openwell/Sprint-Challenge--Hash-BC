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
    for i in range(length):
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)

    first = hash_table_retrieve(ht, 'NONE')
    route[0] = first

    for i in range(1, length):
        data = hash_table_retrieve(ht, route[i-1])
        route[i] = data

    return route
# it was simple you just have to assume its not hard.
# and dont over think it. the trick is in the table and getting the first
# one. which then gets the others

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
output = reconstruct_trip(tickets, len(tickets))

print(output)



