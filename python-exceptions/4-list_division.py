#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length: int):
    output = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ArithmeticError:
            result = 0
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            output.append(result)
    return output
