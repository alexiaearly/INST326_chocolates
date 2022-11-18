""" A student class taking enhancer.
"""
from argparse import ArgumentParser
import sys
    
class Notes():
<<<<<<< HEAD
    """
    
    Attributes:
        name(str): person's name
        gender(str): person's gender
        parents(list of Person): person's parents, may be empty
        spouse(Person): person's spouse, may be empty
    """

    def method1():
=======
    def __init__(self, file):
>>>>>>> ce8f156d9f0ea37c28ea58d87022468da5f88221
        pass
    def add_courses(self):
        pass
    def add_chapter(self):
        pass
    def pull_definition(self):
        pass

class Planner():
    """
    """
    def __init__(self):
        """
        """
        pass
    def to_do(self):
        """
        """
        pass
    def is_assignment_due(self, date):
        """
        """
        pass
 
def main(file, to_dos=None):
    """Creates an instance of Notes class for file. Creates an instance of 
    Planner to create the base of student works.
    
    Args:
        file(txt): a path to the text file
        Optional:
            to_dos(str): string of what user has to do
    
    Side effects:
        Creates instances of Planner and Notes class
    """
    pass

def parse_args(arglist):   
    """Parse command-line arguments.
    
    Expects one (not sure what others) mandatory argument for path to file
    
    Args:
        arglist(list of str): args from the command line
    
    Returns:
        namespace: the parsed args as a namespace
    """
    pass

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)