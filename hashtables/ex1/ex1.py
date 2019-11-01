#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length-1):
        hash_table_insert(ht, i, weights[i])
    
    # loop through all nos to find the write addition
    # get the index of the no from the weight and return as a set
    # while False:
    for i in range(0, length):
        for j in range(i+1, length):
            value1 = hash_table_retrieve(ht, i)
            value2 = hash_table_retrieve(ht, j)
            if value1 + value2 == limit:
                print(value1,value2)
                if value1 == value2:
                    return (max(i, j), min(i, j))
                # if value1 < value2:
                #     value2, value1 = value1, value2
                #     print(weights.index(value1), weights.index(value2))
                return (max(weights.index(value1), weights.index(value2)), min(weights.index(value1), weights.index(value2)))
                # return (weights.index(value1), weights.index(value2))
    """
    YOUR CODE HERE
    """

    return None

# the issue of having no of the same value 
# they override each other in the hash table

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights_3 = [4, 4]
print(get_indices_of_item_weights(weights_3, 2, 8))