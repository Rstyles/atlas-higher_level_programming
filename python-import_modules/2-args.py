#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if len(args) > 0:
        if len(args) == 1:
            print("{} argument:".format(len(args)))
        else:
            print("{} arguments:".format(len(args)))

        for i, arg in enumerate(args):
            print("{}: {}".format(i + 1, arg))
    else:
        print("0 arguments.")
