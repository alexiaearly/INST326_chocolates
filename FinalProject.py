""" A student class taking enhancer.
"""
from argparse import ArgumentParser
import sys
    
class Notes():
    def __init__(self, file):
        pass
    def add_courses(self):
        pass
    def add_chapter(self):
        pass
    def pull_definition(self):
        pass

class Planner():
    def __init__(self):
        pass
    def to_do(self):
        pass
    def is_assignment_due(self, date):
        pass
 
def main():
    pass

def parse_args(arglist):   
    parser = ArgumentParser()
    parser.add_argument()
    parser.add_argument()
    parser.add_argument()
    args = parser.parse_args(arglist)
    return args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file, args.name1, args.name2)
