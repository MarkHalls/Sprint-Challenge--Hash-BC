#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_retrieve,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(0, len(weights)):
        check_weight = limit - weights[i]
        current_index = i
        ht_index = hash_table_retrieve(ht, check_weight)

        if ht_index is not None:
            if ht_index >= current_index:
                return (ht_index, current_index)
            return (current_index, ht_index)

        hash_table_insert(ht, weights[i], current_index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
