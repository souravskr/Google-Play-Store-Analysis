import argparse
parser = argparse.ArgumentParser()
# List of arguments #
parser.add_argument("x", type=int, help="The base number")
parser.add_argument("square", type=int, help="display square of a given number")
parser.add_argument("-v", "--verbosity", help="increases output verbosity", action="count",default=0)

# With the following option, verbosity doesn't need any arguments
# parser.add_argument("-v", "--verbosity", help="increases output verbosity", action="store_true")

args = parser.parse_args()
answer = args.square**2

if args.verbosity >= 2:
    print("The square of {} equals {}".format(args.square,answer))
elif args.verbosity == 1:
    print("{}^2 = {}".format(args.square,answer))
else:
    print(answer)
