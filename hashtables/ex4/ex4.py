def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    neg_dict = {}
    result = []

    for entry in a:
        if -entry in neg_dict:
            result.append(entry if entry >= 0 else -entry)
        neg_dict[entry] = entry
    # print(neg_dict)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
