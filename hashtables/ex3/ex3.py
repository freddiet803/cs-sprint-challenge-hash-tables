def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    intersection_dict = {}

    for each_array in arrays:
        for each_sub_array_value in each_array:
            if each_sub_array_value in intersection_dict:
                intersection_dict[each_sub_array_value] += 1
            else:
                intersection_dict[each_sub_array_value] = 1

            if intersection_dict[each_sub_array_value] == len(arrays):
                result.append(each_sub_array_value)

    return result


if __name__ == "__main__":
    #arrays = []

    arrays = [
        [1, 2, 3, 4, 5],
        [12, 7, 2, 9, 1],
        [99, 2, 7, 1, ]]

    '''arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
        arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
        arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])'''

    print(intersection(arrays))
