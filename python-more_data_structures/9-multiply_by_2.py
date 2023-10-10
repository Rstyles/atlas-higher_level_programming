def multiply_by_2(a_dictionary: dict):
    double_dict = {}
    for key in a_dictionary:
        double_dict[key] = a_dictionary[key] * 2
    return double_dict
