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
    # Fill hashtable with source as key and destination as value
    for i in range(length):
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)

    # Set index
    i = 0
    # Find source airport
    source = hash_table_retrieve(ht, "NONE")
    # Add source airport
    route[i] = source
    # Create next airport
    next_airport = hash_table_retrieve(ht, source)

    for i in range(length-1):
        # add the airport to the route
        route[i + 1] = next_airport
        # set source airport to next
        source = next_airport 
        # find the next airport
        next_airport = hash_table_retrieve(ht, source)
    return route
