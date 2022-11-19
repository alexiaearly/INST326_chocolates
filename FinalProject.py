""" A student class taking enhancer.
"""
from argparse import ArgumentParser
import sys
    
class Notes():
    """This is a class thats takes a students notes uploaded as text file
    
    Attributes:
        file: text file containing students notes for their desired course
    """


    def __init__(self, file):
        pass
    def add_courses(self):
        pass
    def add_chapter(self):
        pass
    def pull_definition(self):
        pass

class Planner():
    """Creates a schedule for students to know their uncomplete tasks and 
    changes their schedule to accomadate to assignments that will soon be due. 
    
    Attributes:
        date(datetime): stores an instant in time 
    """
    def __init__(self):
        """ Initializes a planner object. 
        
        Side Effects:
        Sets a new value to the object's attribute. 
        """
        pass
    def to_do(self, need_to_complete):
        """ Creates a list for the user on what they need to complete. 
        Args:
         need_to_complete(file): Contains are necessary tasks that are still 
         undone
        Returns:
        A list containing all assignments that the user needs to complete. 
        """
        pass
    def is_assignment_due(self, date):
        """ Creates a list that will compare the current date with the due 
        date of an assignment to see which ones need to be completed as soon as
        possible. 
        
        Args:
        date(datetime): stores an instant in time
        
        Returns:
        A list with the assignments due closer to the current date at the top 
        of the list. 
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