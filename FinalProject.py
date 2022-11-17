""" A student class taking enhancer.
"""
from argparse import ArgumentParser
    
class Notes():
    def method1():
        pass
    def method2():
        pass
    def method3():
        pass

class Planner():
    def method1():
        pass
    def method2():
        pass
    def method3():
        pass
 
def parse_args(arglist):   
    parser = ArgumentParser()
    parser.add_argument()
    parser.add_argument()
    parser.add_argument()
    args = parser.parse_args(arglist)
    return args

def main():
    pass

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file, args.name1, args.name2)
