'''
This little program was created using the argparse library tutorial,
as found in the documentation at the following link
https://docs.python.org/3/howto/argparse.html
'''
import argparse
parser = argparse.ArgumentParser(description="This command calculates X to the power of Y", epilog="This is a very basic command")
group = parser.add_mutually_exclusive_group()
# List of arguments #
parser.add_argument("x", type=int, help="The base number")
parser.add_argument("y", type=int, help="The exponent")

# Group of mutuall exclusive options
group.add_argument("-v", "--verbosity", help="increases output verbosity", action="count",default=0)
group.add_argument("-q", "--quiet", help="decreases output verbosity",action="store_true" )

# With the following option, verbosity doesn't need any arguments
# parser.add_argument("-v", "--verbosity", help="increases output verbosity", action="store_true")

args = parser.parse_args()
answer = args.x ** args.y

if args.verbosity >= 3:
    print("Running '{}'".format(__file__))
    print("{} to the power of {} is {}".format(args.x,args.y, answer))
elif args.verbosity == 2:
    print("{} to the power of {} is {}".format(args.x,args.y, answer))
elif args.verbosity == 1:
    print("{}^{} = {}".format(args.x,args.y,answer))
elif args.quiet:
    print(answer)
