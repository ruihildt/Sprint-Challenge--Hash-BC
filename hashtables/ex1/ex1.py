#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    """
    YOUR CODE HERE
    """
    # check if length bigger than 1
    if length > 1:
        # for each weight
        for i in range(length):
            # Fill hashtable with weight as key and index as value
            hash_table_insert(ht, weights[i], i)

        for i in range(length):
            retrieved = hash_table_retrieve(ht, limit - weights[i])
            # Check if the sum of limit - weight is a valid key in the hashtable
            if retrieved is not None:
                return(retrieved, i)

    # return none
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
